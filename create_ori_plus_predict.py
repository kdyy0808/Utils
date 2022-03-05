import os
#from posixpath import commonpath
import cv2
from cv2 import IMREAD_COLOR


#os.environ['DISPLAY'] = ':0'
#os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

common_path = "/media/piai202/53387bcd-1a4a-4370-8c74-abf0c7811ab0/Segmentation_data/ALL_train_data/test/"

ori_folder = common_path+"ori_img/"
gt_folder = common_path+"mask_img/"
predict_folder = common_path+"prediction/"

compare_result_folder = common_path+"compare_result/"


file_list = os.listdir(ori_folder)
gt_file_list = os.listdir(gt_folder)
predict_file_list = os.listdir(predict_folder)


file_list.sort()
count=0
file_num = len(file_list)

for file_name in file_list:
    if file_name in gt_file_list:
        if file_name in predict_file_list:
            img=cv2.imread(ori_folder+file_name,IMREAD_COLOR)
            gt_img = cv2.imread(gt_folder+file_name,IMREAD_COLOR)## 1 0 
            predict_img = cv2.imread(predict_folder+file_name,IMREAD_COLOR)###132 197

            b,g,r=cv2.split(gt_img)
            b_p,_,_ = cv2.split(predict_img)

            test = b+b_p

            TP = len(img[test==133])
            FP = len(img[test==132])
            FN = len(img[test==198])
            TN = len(img[test==197])

            if TP==0:
                Precision = 0
                Recall =0
                Accuracy =0
                IOU = 0

            else:

                Precision = float(TP/(TP+FP))
                Recall = float(TP/(TP+FN))
                Accuracy = float((TP+TN)/(TP+FP+FN+TN))
                IOU = float(TP/(TP+FN+FP))


            blue = (255, 0, 0)
            green= (0, 255, 0)
            red= (0, 0, 255)
            white= (255, 255, 255) 
            # 폰트 지정
            font =  cv2.FONT_HERSHEY_COMPLEX_SMALL
            
            # 이미지에 글자 합성하기
            img[:100,:220] = (255,255,255)
            img = cv2.putText(img, "Precision : {:.3f}".format(Precision), (5, 25), font, 1, blue, 1)
            img = cv2.putText(img, "Recall    : {:.3f}".format(Recall), (5, 55), font, 1, blue, 1)
            img = cv2.putText(img, "IOU       : {:.3f}".format(IOU), (5, 85), font, 1, blue, 1)


            print(len(img[test==133]))
            img[test==133] = (0,255,0)#맞춘거 초록  
            img[test==198] = (0,0,255)#못맞춘거 (정답인데 체크못함) 붉은색
            img[test==132] = (255,0,0)# 정답으로 오해한거 하늘색 


            #cv2.imshow("dd", img)

            cv2.imwrite(compare_result_folder+file_name,img)
            #cv2.waitKey()
            #cv2.destroyAllWindows()
            count+=1
            print("-----train_file working-----"+str(count)+"/"+str(file_num)+"----",end="")
            print("\r", end="")
print("")
print("Complete!!")

