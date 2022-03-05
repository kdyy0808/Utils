import os
import random
import shutil

common_path = "/media/piai202/53387bcd-1a4a-4370-8c74-abf0c7811ab0/Segmentation_data/ALL_train_data/"

All_img_path = common_path + "ori_img/"
All_mask_path = common_path + "mask_img/"

train_img_path = common_path + "train/"+"ori_img/"
train_mask_path = common_path + "train/"+"mask_img/"

test_img_path = common_path + "test/"+"ori_img/"
test_mask_path = common_path + "test/"+"mask_img/"

All_img_file_list = os.listdir(All_img_path)

random.shuffle(All_img_file_list)
total_file_num = len(All_img_file_list)

test_ratio = 0.1
test_idx = int(total_file_num*test_ratio)

test_file_name_list = All_img_file_list[:test_idx]
train_file_name_list = All_img_file_list[test_idx:]

count = 0
file_num = len(test_file_name_list)

for test_file_name in test_file_name_list:
    count+=1
    shutil.copy(All_img_path+test_file_name, test_img_path+test_file_name)
    shutil.copy(All_mask_path+test_file_name, test_mask_path+test_file_name)
    print("-----test_file working-----"+str(count)+"/"+str(file_num)+"----",end="")
    print("\r", end="")
print("")
count = 0
file_num = len(train_file_name_list)
for train_file_name in train_file_name_list:
    count+=1
    shutil.copy(All_img_path+train_file_name, train_img_path+train_file_name)
    shutil.copy(All_mask_path+train_file_name, train_mask_path+train_file_name)
    print("-----train_file working-----"+str(count)+"/"+str(file_num)+"----",end="")
    print("\r", end="")
print("")
print("Complete!!")

#r_seed = random.randrange(0,10)
