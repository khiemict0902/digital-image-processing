import matplotlib.pyplot as plt
import matplotlib.image as imgs

def equaling(arr):
    newarr = []
    s = sum(arr)
    temp = 0
    for i in arr:
        temp += int((i/s)*255) 
        newarr.append(temp)

    return newarr


img = imgs.imread('img.JPG')
r = [0 for _ in range(256)]
g = [0 for _ in range(256)]
b = [0 for _ in range(256)]

print(img.shape)

for c1 in range(img.shape[0]):
    for c2 in range(img.shape[1]):
        # print(f"x[{c1}][{c2}][x]")
        r[img[c1][c2][0]]+=1
        g[img[c1][c2][1]]+=1
        # print("F ", b[img[c1][c2][2]])
        b[img[c1][c2][2]]+=1
        # print("A ", b[img[c1][c2][2]])


print("done 1")

er = equaling(r)
eg = equaling(g)
eb = equaling(b)

print("done 2")


newimg = img[:,:,:].tolist()

heg = [0 for _ in range (256)]
her = [0 for _ in range (256)]
dXX = [f"{i}" for i in range (256)]
heb = [0 for _ in range (256)]

for c1 in range(img.shape[0]):
    for c2 in range(img.shape[1]):
        nr = img[c1][c2][0]
        ng = img[c1][c2][1]
        nb = img[c1][c2][2]

        x1 = er[nr]
        x2 = eg[ng]
        x3 = eb[nb]
        
        her[x1] +=1
        heg[x2] +=1
        heb[x3] +=1

        newimg[c1][c2][0] = x1
        newimg[c1][c2][1] = x2
        newimg[c1][c2][2] = x3

    print(f"{int((c1/img.shape[0])*100)}%")

print(her)

print("done 3")
print("Showing...")


plt.subplot(2, 2, 1)
plt.bar(dXX, r, color='r', label='red') 
plt.bar(dXX, g, color='g', label='green')
plt.bar(dXX, b, color='b', label='blue')
plt.title("Before Histogram Equalisation")

plt.subplot(2, 2, 3)
plt.bar(dXX, her, color='r', label='red') 
plt.bar(dXX, heg, color='g', label='green')
plt.bar(dXX, heb, color='b', label='blue')
plt.title("After Histogram Equalisation")

plt.subplot(2,2,4)
plt.imshow(newimg)
plt.title("Output Image")

plt.subplot(2,2,2)
plt.imshow(img)
plt.title("Input Image")

plt.show()
