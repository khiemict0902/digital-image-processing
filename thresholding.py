import matplotlib.pyplot as plt
import matplotlib.image as imgs

img = imgs.imread('./cc.jpg')


#to gray img
grayImg=[]
for r in range(img.shape[0]):
    row = []
    for c in range(img.shape[1]):
        px = int(img[r][c][0]/3)+int(img[r][c][2]/3)+int(img[r][c][1]/3)
        # p1 = [px for _ in range(3)]
        row.append(px)
    grayImg.append(row)

#Thresholding
k = 126
thresImg = []
for r in range(img.shape[0]):
    row = []
    for c in range(img.shape[1]):
        if(grayImg[r][c]<k):
            px=0
        else:
            px=1
        # p1 = [px for _ in range(3)]
        row.append(px)
    thresImg.append(row)


plt.imshow(thresImg, cmap='gray')
plt.show()
