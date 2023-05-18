import PIL.Image as Image
import numpy as np


image = Image.open('picture1.jpg')  # 不同的图像可以放到这个文件里，然后
# 在这儿改打开的图像名称就可以，比如picture1->picture2
# 显示原始图片
image.show()
width, height = image.size
print(width, height)
# 将图片变为灰度图片，并且显示
image_grey = image.convert("L")
image_grey.show()
data = image_grey.getdata()
data = np.matrix(data, dtype="float")
data = np.reshape(data, (height, width))   # 图片数据被彻底处理为灰度图像，得到矩阵
# 中心化
average = np.sum(data, axis=0)/height
data_S = data.copy() - average
# 开始PCA
C = (data_S.T @ data_S)/width
evalue, evect = np.linalg.eig(C)
# 得到了特征值和特征矩阵
inde = np.argsort(evalue)
inde = list(inde)
lst = []
num = 70  # 主成分个数,在这儿输入即可，现在为70个主成分,由于不同照片的长宽不同，
for k in range(width-1, width-num-1, -1):
    lst.append(inde.index(k))
lst = np.array(lst)
P_k = evect[:, lst]
data_S_new = data_S @ P_k @ P_k.T
data_S_new = data_S_new + average
# 将k个主成分构成的矩阵
mg = Image.fromarray(np.uint8(data_S_new))
mg.show()

