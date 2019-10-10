# Update @ Oct 10 ，2019
Profartssor Yu update new version. Change the mod from float to long. It's only 915K. すごい<br>
"facedetectcnn-floatdata.cpp" change to "facedetectcnn-int8data.cpp"

So , you have to change the C++ DLL project"
1) Open the fd-shiqiyu.sln
2) Remove "facedetectcnn-floatdata.cpp"
3) Copy all files(*.h and *.cpp) from https://github.com/ShiqiYu/libfacedetection/tree/master/src to your project
4) Add "facedetectcnn-int8data.cpp" into the project
4) Recompile the project to generate "fd-shiqiyu_v2.dll"

-------------------------------------------------------

# pySample-for-ShiqiYu
The DLL inferface &amp; python sample code base on new version of libfacedetection （https://github.com/ShiqiYu/libfacedetection ）by Shiqi.Yu.

于仕琪 老师新版本人脸识别（https://github.com/ShiqiYu/libfacedetection )的DLL接口及Python语言案例。

<b>Step1 : Create a Dll for proivide an interface to python</b>
1) Create a C++ DLL project and named "fd-shiqiyu" in VS2017
2) Copy all files(*.h and *.cpp) from https://github.com/ShiqiYu/libfacedetection/tree/master/src to your project
3) Create the "dll-interface.cpp" to export the function
4) Compile the project to generate "fd-shiqiyu.dll"

<b>第一步：创建用于python接口的DLL</b><br>
1）VS2017中创建新 “C++ DLL”项目，名称为 “fd-shiqiyu”<br>
2）将 https://github.com/ShiqiYu/libfacedetection/tree/master/src 下所有文件复制到项目中<br>
3）新建 "dll-interface.cpp" ，提供DLL访问接口<br>
4）编译项目，生成 "fd-shiqiyu.dll"<br>

<b>Step2 : The sample code of Python call the DLL </b>
1) Copy the "fd-shiqiyu.dll" file to Dlls folder of python code's path
2) Create the "ex.py" sample code file to call the Dll
3）Run "ex.py" 

<b>第2步：Python 调用 Dll 案例代码</b><br>
1）拷贝 "fd-shiqiyu.dll" 文件到 Python 代码的 “Dlls” 子目录下<br>
2）新建 "ex.py" 案例代码<br>
3）运行 "ex.py"<br>


<b>The diffrences between new version and old version of Shiqi.Yu's library.</b>
1) The new version can detect the any angle face, include upside-down face, the old version can't
2) But the new version can't output the angle & 68 landmark points of face now, the old version can do it

<b>于老师新旧版本的比较</b><br>
1）新版本可以检测任何角度的脸，包括倒立的，旧版本不行<br>
2）但新版本现在还不能提供 角度 和 68关键点 参数，旧版本可以<br>
