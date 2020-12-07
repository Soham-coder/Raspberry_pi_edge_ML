import os
category_list = []
image_list_new = []
input_image_dir = input("Enter path of image directory where images are present:")
print("Entered image directory is : ", input_image_dir)
pic_list=os.listdir(path = input_image_dir)
for image in pic_list:
    image_list = image.split('_')
    category = image_list[3].strip('.png')
    image_list_new.append(str(image))
    category_list.append(str(category))
    #print(image_list_new)
dictionary = dict(zip(image_list_new, category_list))
print(dictionary)
