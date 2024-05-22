import matplotlib.pyplot as plt
import matplotlib.image as imgs

img = imgs.imread('./catimg.jpg')


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

k = [[1,0,1],
     [0,0,0],
     [1,0,1]]


def hit(pimg, kernel):
    check = False
    for u in range(len(kernel)):
        for v in range(len(kernel)):
            if pimg[u][v] == kernel[u][v] and kernel[u][v]==0:
                return True
    return check


def fit(pimg, kernel):
    check = True
    for u in range(len(kernel)):
        for v in range(len(kernel)):
            if pimg[u][v] != kernel[u][v] and kernel[u][v]==0:
                return False
    return check


def dilation(img, kernel):
    newImg = []
    for r in range(1, len(img)-1):
        row=[]
        for c in range(1, len(img[0])-1):
            #this so fkin crazy D:
            pimg = [[int(img[r+u][c+v]) for u in range(-1,2) ]for v in range(-1,2)]
            check = hit(pimg,kernel)        

            if check:
                print(pimg)
                px = 0
            else:
                px = img[r][c]
            row.append(px)
        newImg.append(row)

    return newImg

def erosion(img, kernel):
    newImg = []
    for r in range(1, len(img)-1):
        row=[]
        for c in range(1, len(img[0])-1):
            #this so fkin crazy D:
            pimg = [[int(img[r+u][c+v]) for u in range(-1,2) ]for v in range(-1,2)]
            check = fit(pimg,kernel)        

            if check:
                # print(pimg)
                px = img[r][c]
            else:
                px = 1
            row.append(px)
        newImg.append(row)

    return newImg

def opening(img, kernel):
    newImg = erosion(img,kernel)
    newImg = dilation(newImg, kernel)
    return newImg


def closing(img, kernel):
    newImg = dilation(img,kernel)
    newImg = erosion(newImg, kernel)
    return newImg

eroImg = erosion(thresImg,k)
dilationImg = dilation(thresImg,k)
openImg = opening(thresImg,k)
closeImg = closing(thresImg, k)

plt.subplot(3,2,1)
plt.imshow(eroImg, cmap='gray')
plt.title('Erosion')
plt.subplot(3,2,2)
plt.imshow(dilationImg, cmap='gray')
plt.title('Dilation')
plt.subplot(3,2,3)
plt.imshow(thresImg, cmap='gray')
plt.title('Thresholding')
plt.subplot(3,2,4)
plt.imshow(grayImg, cmap='gray')
plt.title('Gray Image')
plt.subplot(3,2,5)
plt.imshow(openImg, cmap='gray')
plt.title('Opening Image')
plt.subplot(3,2,6)
plt.imshow(closeImg, cmap='gray')
plt.title('Closing Image')
plt.show()
