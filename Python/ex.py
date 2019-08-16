# coding: utf-8
# 
# 程序功能 ：使用 于仕琪 老师的lib，做人脸识别
#     重点 ：调用 C++ 提供的 DLL 接口时，如何处理 指针 类型

import numpy as np
import cv2
from ctypes import *
import types
import sys

if len(sys.argv) < 2:
    print(
        "Call this program like this:\n"
        "  ./ex.py ./jpg/001.jpg\n")
    exit()


Max_Faces = 256
Size_one_Face = 6 + 68 * 2
Size_FaceLandMarks = Size_one_Face * Max_Faces
class FaceResults(Structure): 
    _fields_ = [("face_num", c_int32), 
                ("datas", c_int16 * Size_FaceLandMarks)
               ]


img = cv2.imread(sys.argv[1])
h,w = img.shape[:2]
st = w*3

p_img = img.ctypes.data_as(POINTER(c_ubyte))

dll = CDLL('./dlls/fd-shiqiyu.dll')
dll.shiqi_fd.restype = POINTER(FaceResults)

p_results = dll.shiqi_fd(p_img,w,h,st) 
face_num = p_results.contents.face_num
print(p_results.contents.datas[:Size_one_Face])
print(p_results.contents.datas[Size_one_Face:Size_one_Face*2])

for i in range(face_num):
    j =  Size_one_Face * i
    x = p_results.contents.datas[j]
    y = p_results.contents.datas[j+1]
    w = p_results.contents.datas[j+2]
    h = p_results.contents.datas[j+3]
    confidence = p_results.contents.datas[j+4]
    angle = p_results.contents.datas[j+5]

    print("Face : %d ; [%d,%d]-[%d,%d] ; Conf=%d, Angle=%d"%(i,x,y,w,h,confidence,angle))
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(i),(x, y-10),font, 0.8,  (0,0,0), 1, cv2.LINE_AA)


# show the output image
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
