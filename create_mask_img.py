import cv2
import numpy as np
from PIL import Image


img_ori = cv2.imread('5545.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('5545.jpg', cv2.IMREAD_GRAYSCALE)

img_ori = cv2.resize(img_ori,dsize=(640,480))
img_gray = cv2.resize(img_gray,dsize=(640,480))


ret, img_binary = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(img_binary, connectivity=8)

import_label_idx = list()

for i in range(0, cnt): # 각각의 객체 정보에 들어가기 위해 반복문. 범위를 1부터 시작한 이유는 배경을 제외
    (x, y, w, h, area) = stats[i]

    # 노이즈 제거
    if area < 200 or area >10000:
        continue

    cv2.rectangle(img_ori, (x, y, w, h), (0, 0, 255),thickness=3)
    import_label_idx.append(i)

for y in range(480):
    for x in range(640):
        if labels[y][x] not in import_label_idx:
            labels[y][x] = 0

for y in range(480):
    for x in range(640):
        if labels[y][x] != 0:
            labels[y][x] = 255
    
arr = np.array(labels)
np.expand_dims(arr, axis=1)
#label2=Image.fromarray()

#cv2.imwrite('color_img.jpg', img)


# 구조화 요소 커널, 사각형 (5x5) 생성 ---①
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# # 열림 연산 적용 ---②
#opening = cv2.morphologyEx(img_binary, cv2.MORPH_OPEN, k)
# # 닫힘 연산 적용 ---③
closing = cv2.morphologyEx(img_binary, cv2.MORPH_CLOSE, k)

# 결과 출력

img_ori = cv2.resize(img_ori,dsize=(640,480))

cv2.imshow('ori', img_ori)
merged1 = np.hstack((img_gray, img_gray))
merged2 = np.hstack((img_binary, closing))

merged3 = np.vstack((merged1, merged2))
cv2.imshow('test', merged3)


#label2.show()

cv2.imshow('mask', arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
