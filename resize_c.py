import cv2
import os.path
import os
import numpy as np

##长边设置为64像素，等比修改图片大小
##
def img_resize(img):
    height, width = img.shape[0], img.shape[1]
    # 设置新的图片分辨率框架,这里设置为长边像素大小为64
    width_new = 64
    height_new = 64
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(img, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(img, (int(width * height_new / height), height_new))
    return img_new


def read_path(file_path,save_path):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_path):
        print(filename)
        img = cv2.imread(file_path+'/'+ filename)
        if img is None :
            print("None")
            break
        ####change to size
        image = img_resize(img)
        cv2.imwrite(save_path + filename, image)


#读取的目录
if __name__ == '__main__':
    folder_path = '/home/jinjin/CIFAR-10-dataset/test/'
    folder = []
    for foldername in os.listdir(folder_path):
        folder.append(foldername)
    for i in range(len(folder)):
        file_path = folder_path+folder[i]
        save_path = folder_path+folder[i]+'/'
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        read_path(file_path,save_path)


    folder_path = '/home/jinjin/CIFAR-10-dataset/train/'
    folder = []
    for foldername in os.listdir(folder_path):
        folder.append(foldername)
    for i in range(len(folder)):
        file_path = folder_path+folder[i]
        save_path = folder_path+folder[i]+'/'
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        read_path(file_path,save_path)


