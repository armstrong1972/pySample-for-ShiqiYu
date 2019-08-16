#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "facedetectcnn.h"

#define DETECT_BUFFER_SIZE 0x20000


extern "C" __declspec(dllexport) 
int * shiqi_fd(unsigned char * rgb_image_data, int width, int height, int step) //input image, it must be RGB (three-channel) image!
{
	unsigned char * pBuffer = (unsigned char *)malloc(DETECT_BUFFER_SIZE);
	return facedetect_cnn(pBuffer, rgb_image_data, width, height, step);
}