import os, random, shutil

def renew(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        os.makedirs(path)
    
    return


def makesample(fileDir,rate):
    folderDir = os.listdir(fileDir[0])    #取每一类的文件夹的原始路径
    sample1 = []
    sample2 = []
    for folder in folderDir:
        pathDir1 = os.listdir(fileDir[0]+folder)
        pathDir2 = os.listdir(fileDir[1]+folder)
        picknumber=800 #从每个文件夹中取一定数量图片
        sample1.append(random.sample(pathDir1, picknumber))  #随机选取picknumber数量的样本图片
        sample2.append(random.sample(pathDir2, int((picknumber-300)*rate+300))) #随机选取picknumber数量的样本图片
    return(sample1,sample2)


def makecontrast(fileDir,conDir,sample1,sample2):
    os.makedirs(conDir)
    folderlist = os.listdir(fileDir[0])
    for i in range(9):
        a = sample1[i]
        b = sample2[i]
        for name in a[0:500]:
            shutil.copy(fileDir[0]+folderlist[i]+'/'+name, conDir+name)
        for name in b[0:len(b)-300]:
            shutil.copy(fileDir[1]+folderlist[i]+'/'+name, conDir+name)
    return

def makelinear(fileDir,liDir,sample1,sample2):
    folderlist = os.listdir(fileDir[0])
    for i in range(9):
        os.makedirs(liDir+'train/'+folderlist[i])
        a = sample1[i]
        b = sample2[i]
        for name in a[500:800]:
            shutil.copy(fileDir[0]+folderlist[i]+'/'+name, liDir+'train/'+folderlist[i]+'/'+name)
        for name in b[len(b)-300:len(b)]:
            shutil.copy(fileDir[1]+folderlist[i]+'/'+name, liDir+'train/'+folderlist[i]+'/'+name)
           
    return
    #！！！还缺少验证集

 
if __name__ == '__main__':
    #STL is the dominant data
    fileDir = ["/home/jinjin/STL10/img_t/" , "/home/jinjin/CIFAR-10-dataset/train/"]  #源图片文件夹路径
    ratelist = [0.1,0.05,0.02]
    for i in range(3):
        tarDir = './'+str(i+1)+'/'
        renew(tarDir)
        conDir = tarDir+'contrast/'    #移动到新的文件夹路径
        liDir = tarDir+'linear/'    #移动到新的文件夹路径
        sam1,sam2 = makesample(fileDir,ratelist[i])
        print(len(sam1[0]))
        print(len(sam2[0]))
        makecontrast(fileDir,conDir,sam1,sam2)
        makelinear(fileDir,liDir,sam1,sam2)

    #CIFAR is dominant data
    fileDir = ["/home/jinjin/CIFAR-10-dataset/train/" , "/home/jinjin/STL10/img_t/"]
    for i in range(3):
        tarDir = './'+str(i+4)+'/'
        renew(tarDir)
        conDir = tarDir+'contrast/'    #移动到新的文件夹路径
        liDir = tarDir+'linear/'    #移动到新的文件夹路径
        sam1,sam2 = makesample(fileDir,ratelist[i])
        print(len(sam1[0]))
        print(len(sam2[0]))
        makecontrast(fileDir,conDir,sam1,sam2)
        makelinear(fileDir,liDir,sam1,sam2)


  