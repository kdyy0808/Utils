from cProfile import label
import cv2
import sys
import numpy as np
from PIL import Image
import os


class Labeling_image:


    def __init__(self):
        self.filename = ''#'sample1.jpg'
        self.cnt = 0
        #self.initialize()

    def initialize(self):
        self.img_ori = cv2.imread("input/"+self.filename, cv2.IMREAD_COLOR)
        
        self.img_binary = 0
        self.img_labeled = 0

        if self.img_ori is None:
            print('Image load failed!')
            sys.exit()
        self.img_ori = cv2.resize(self.img_ori,dsize=(640,480))
        self.img_painting = self.img_ori.copy()

        hsv = cv2.cvtColor(self.img_ori, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        self.img_gray = v
        
        cv2.imshow('Original', self.img_ori)
        if self.cnt ==0:
            cv2.createTrackbar('Threshold', 'Original', 0, 255, self.on_change)
        cv2.setTrackbarPos('Threshold', 'Original', 100)
        self.cnt +=1
        

    def labeling_image(self,Binary_img,Painting_img):
        cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(Binary_img, connectivity=8)

        important_label_idx = list()

        for i in range(0, cnt): # 각각의 객체 정보에 들어가기 위해 반복문. 범위를 1부터 시작한 이유는 배경을 제외
            (x, y, w, h, area) = stats[i]

            # 노이즈 제거
            if area < 1000 or area >10000:#200
                continue

            cv2.rectangle(Painting_img, (x, y, w, h), (0, 0, 255),thickness=3)
            important_label_idx.append(i)

        for y in range(480):
            for x in range(640):
                if labels[y][x] not in important_label_idx:
                    labels[y][x] = 0

        labels=np.where(labels>0,255,0)

        Output_img = np.array(labels.copy(), dtype = np.uint8)
        return Output_img

    def change_file(self,file_list,idx):
        self.filename = file_list[idx]
    
    def on_change(self,pos):
        pass   

def main():
    
    file_list =  os.listdir("./input")
    out_folder = "./output"
    Not_processing_folder = './not_processing'
    
    file_list.sort()

    labeling_img = Labeling_image()
    labeling_img.change_file(file_list=file_list,idx=0)
    labeling_img.initialize()
    print("\rWorking"+"\tfile name :\t{}\t{}/{}".format(file_list[0],1,len(file_list)),end="")
    cnt =0
    while True:
        key = cv2.waitKeyEx(1)#50
        if key == ord('q'):
            break
        #print(key)
        if key == 65361:
            print("LLLLL")
        elif key == 65363:
            print("RRRRR")
        elif key == 115:# s누를 때 
            

            cv2.imwrite(out_folder+'/'+labeling_img.filename[:-4]+'_BI.jpg', arr)
            if cnt >= len(file_list)-1:
                break

            print("\rWorking"+"\tfile name :\t{}\t{}/{}".format(file_list[cnt+1],cnt+2,len(file_list)),end="")

            cnt += 1
            labeling_img.change_file(file_list, cnt)           
            labeling_img.initialize()
        elif key == 110: # n 누를 때
            
            img_ori=labeling_img.img_painting.copy()
            cv2.imwrite(Not_processing_folder+'/'+labeling_img.filename[:-4]+'_Not.jpg', img_ori)
            if cnt >= len(file_list)-1:
                break
            print("Not processing")
            print("\rWorking"+"\tfile name :\t{}\t{}/{}".format(file_list[cnt+1],cnt+2,len(file_list)),end="")
        
            cnt += 1
            labeling_img.change_file(file_list, cnt)
            labeling_img.initialize()

        threshold_value = cv2.getTrackbarPos('Threshold', 'Original')
        _, binary_img = cv2.threshold(labeling_img.img_gray, threshold_value, 255, cv2.THRESH_BINARY_INV)

        img_ori=labeling_img.img_painting.copy()

        arr=labeling_img.labeling_image(binary_img,img_ori)

        cv2.imshow('Original', img_ori)
        cv2.imshow('Binary',arr)
        if cnt == 0:
            cv2.moveWindow('Original', 0,0)
            cv2.moveWindow('Binary', 715,0)

    cv2.destroyAllWindows()
    print("\r총 작업 파일 수 : {}".format(cnt))
#main()

if __name__ == "__main__":
    main()

