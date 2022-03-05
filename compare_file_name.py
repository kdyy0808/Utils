
import cv2
import sys
import numpy as np
import os
import shutil

# file_list =  os.listdir("/home/piai202/Downloads/CRACK_soo/output/")
# out_folder = "./annotations/"
# input_path = "/home/piai202/Downloads/CRACK_soo/output/"

compare1_folder = "/media/piai202/53387bcd-1a4a-4370-8c74-abf0c7811ab0/Segmentation_data/output/"
compare2_folder = "/media/piai202/53387bcd-1a4a-4370-8c74-abf0c7811ab0/Segmentation_data/input/"
output_folder = "/media/piai202/53387bcd-1a4a-4370-8c74-abf0c7811ab0/Segmentation_data/New_original_img/"


compare1_file_list = os.listdir(compare1_folder)
compare2_file_list = os.listdir(compare2_folder)



compare1_file_list.sort()
compare2_file_list.sort()

for file_name in compare1_file_list:
    if file_name in compare2_file_list:
        shutil.copy(compare2_folder+file_name,output_folder+file_name)

print("complete")


######
# dddd=cv2.imread("dddd.png", cv2.IMREAD_COLOR)
# b,g,r = cv2.split(dddd)

# kkk=b.tolist()
# Set_num = set(list(map(tuple,kkk)))
# print("output :{}".format(max(list(Set_num))))
# print(Set_num)

#####




'''
total_num=len(file_list)
count=0

for file_name in file_list:
    if ".jpg" not in file_name:
        continue
    ori_img = cv2.imread(input_path+ file_name, cv2.IMREAD_GRAYSCALE)
    height,width=ori_img.shape
    #b,g,r = cv2.split(ori_img)
    b = ori_img//240
    zero = np.zeros((height,width,1), dtype=np.uint8)

    changed_img=cv2.merge((b,zero,zero))
    #cv2.imshow(file_name,changed_img)
    cv2.imwrite(out_folder+file_name[:-4]+".png",changed_img)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    #print(heif_name,end="\t")
    count += 1
    print("----"+str(count)+"/"+str(total_num)+"----",end="")
    print("\r", end="")
print("")
print("Complete!!")



'''