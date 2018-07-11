import numpy as np
# exit()

#------------------------------這是一個utf16的檔案
#導致我一開始一直無法decode
# with open("yolo_out.txt", 'rb') as f:
with open("yolo data/yolo_out.txt",'r',encoding="utf-16") as f:
    contents = f.read()
# f = open('yolo_out.txt','rb')
#
# data=f.read()
data_array=contents.split("\n")
print(data_array[50])
