import matplotlib.pyplot as plt
import matplotlib.image as imgs

img = imgs.imread('./catimg.jpg')

noF = [[0,0,0],[0,0,0],[0,0,0]]

filterBlur =   [[4,8,4],
             [8,16,8],
             [4,8,4]]

filterLaplancian = [[0,1,0],
                    [1,-4,1],
                    [0,1,0]]

def filtering(img, filters, smooth=True):
    if smooth:
        s = sum(sum(row) for row in filters)
    else:
        s = 1
    print(s)
    newImg = []
    for r in range(1,len(img)-1):
        row = []
        for c in range(1,len(img[0])-1):
            if smooth:
                px = sum([int(img[r+u][c+v]*filters[u+1][v+1]/s) for u in range(-1,2) for v in range(-1,2)]) 
            else:
                px = img[r][c] - sum([int(img[r+u][c+v]*filters[u+1][v+1]/s) for u in range(-1,2) for v in range(-1,2)])
                if px <=0:
                    px = 0
                if px >=255:
                    px=255
            
            row.append(px)
        newImg.append(row)

        



    return newImg

def sharpening(oriImg, filterImg):
    newImg = [[oriImg[r][c]-filterImg[r][c] for r in range(len(oriImg))] for c in range(len(oriImg[0])) ]
    return newImg   


#to gray img
# grayImg = [[int((img[r][c][0]+img[r][c][1]+img[r][c][2])/3) for r in range(img.shape[0])] for c in range(img.shape[1])]
grayImg = []
for r in range(img.shape[0]):
    row = []
    for c in range(img.shape[1]):
        px = int((img[r][c][0]/3+img[r][c][2]/3+img[r][c][1]/3))
        # px = [pi for _ in range(3)]
        row.append(px)
    grayImg.append(row)

newImg = filtering(grayImg,filterLaplancian,smooth=False)

# print(grayImg)
plt.subplot(1,2,1)
plt.imshow(grayImg,cmap='gray')

plt.subplot(1,2,2)
plt.imshow(newImg, cmap='gray')
plt.show()
