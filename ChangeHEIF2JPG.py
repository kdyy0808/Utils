from PIL import Image
import pyheif
import os

file_list =  os.listdir("./input")
out_folder = "./output"

total_num = len(file_list)
count = 1
for heif_name in file_list:
    if ".HEIC" not in heif_name:
        continue
    heif_file = pyheif.read("./input/"+heif_name)

    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    heif_name= heif_name[:-5]
    print(heif_name,end="\t")
    print("----"+str(count)+"/"+str(total_num)+"----",end="")
    image.save(out_folder +"/" +heif_name+".jpg", "JPEG")
    count += 1
    print("\r", end="")
print("Complete!!")
