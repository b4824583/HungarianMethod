import numpy as np
import Function as func
diction={"row":"row train","column":"stone column"}





f = open('hungarian test data.txt','r')
data=f.read()
data=data.split()
i=-1
person=[]
weight_array=[[] for i in range (4)]
for person_and_weight in data:
    if person_and_weight.isalpha():
        person.append(person_and_weight)
        i+=1
    else:
        weight_array[i].append(int(person_and_weight))
# print(person)
# print(weight[0])



# a=np.arange(16).reshape(4,4)
weight_matrix=np.eye(4)
weight_matrix=weight_matrix.astype(int)
for i in range(0,4):
    for j in range(0,4):
        weight_matrix[i][j]=weight_array[i][j]

print(weight_matrix)
#------------------------------列簡化
row_reduse_matrix=np.zeros((4,4))
row_reduse_matrix=row_reduse_matrix.astype(int)
for i in range(0,4):
    if min(weight_matrix[i])!=0:
        row_reduse_matrix[i]=weight_matrix[i]-min(weight_matrix[i])
    else:
        row_reduse_matrix[i]=weight_matrix[i]
print("row reduse matrix \n",row_reduse_matrix,"\n")
#------------------------------行簡化
column_reduse_matrix=np.zeros((4,4))
column_reduse_matrix=column_reduse_matrix.astype(int)
for i in range(0,4):
    # print(min(row_reduse_matrix[:,i]))
    if min(row_reduse_matrix[:,i])!=0:
        column_reduse_matrix[:,i]=row_reduse_matrix[:,i]-min(row_reduse_matrix[:,i])
    else:
        column_reduse_matrix[:,i]=row_reduse_matrix[:,i]
print("column reduse mastrix \n",column_reduse_matrix,"\n")
#------------------------------------
#---------------------------------劃線
#------------------------目前劃線遇到困難，思考說要怎麼畫零






sort_how_many_zero_in_matrix=func.count_zero_in_this_matrix(column_reduse_matrix,1)
print("sort zero number \n",sort_how_many_zero_in_matrix,"\n")
#------ -------------------------------------------



display_zero_matrix=func.build_display_zero_matrix(column_reduse_matrix)
print("display zero in matrix \n",display_zero_matrix,"\n")


draw_line_matrix=func.build_draw_line_matrix()
print("draw line matrix \n",draw_line_matrix,"\n")






func.if_element_have_zero_than_draw_a_line(sort_how_many_zero_in_matrix,display_zero_matrix,draw_line_matrix)

print("display zero 的其中\n",display_zero_matrix)

print("draw line matrix\n",draw_line_matrix)

#--------------------------------------------------這邊要對所有的element做排序

buble_sort_list=[]
for i in range(0,4):
    for j in range(0,4):
        if column_reduse_matrix[i][j]>0:
            coordinate=str(i)+"-"+str(j)
            buble_sort_list.append((coordinate,column_reduse_matrix[i][j]))
print(min(buble_sort_list, key=lambda s: s[1]))
min_weight=min(buble_sort_list, key=lambda s: s[1])
#--------------------------------------------減去最小值的element
min_number_coordinate=min_weight[0].split("-")

for i in range(0,4):
    for j in range(0,4):
        if i==min_number_coordinate[0] and j==min_number_coordinate[j]:
            column_reduse_matrix[i][j]=0
        elif draw_line_matrix[i][j]==0:
            column_reduse_matrix[i][j]-=min_weight[1]
        elif draw_line_matrix[i][j]==2:
            column_reduse_matrix[i][j]+=min_weight[1]
print("new column reduse matrix\n",column_reduse_matrix)



#-----------------------------------------------------------檢查是否所
sort_how_many_zero_in_matrix=func.count_zero_in_this_matrix(column_reduse_matrix,0)

print("sort zero number \n",sort_how_many_zero_in_matrix,"\n")

draw_line_matrix=func.build_draw_line_matrix()
display_zero_matrix=func.build_display_zero_matrix(column_reduse_matrix)




#這邊有問題需要修改，需要思考怎麼找出MATCHING的東西

#display_zero_matrix=func.build_display_zero_matrix(column_reduse_matrix)
#print("zero matrix \n",display_zero_matrix)

#draw_line_matrix=func.if_element_have_zero_than_draw_a_line(func.count_zero_in_this_matrix(column_reduse_matrix),display_zero_matrix,draw_line_matrix)







