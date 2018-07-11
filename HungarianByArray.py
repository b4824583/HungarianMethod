import numpy as np


f = open('job data.txt','r')
data=f.read()
# person = numpy.zeros((4,1),int)
person=[]
weight=[[] for i in range (4)]
column_reduse_weight=[[] for i in range(4)]
# weight=weight.append([])
i=-1
print(data)
data_split_already=data.split()
# print(data_split_already)
for person_and_weight in data_split_already:
    if person_and_weight.isalpha():
        person.append(person_and_weight)
        i+=1
    else:
       weight[i].append(int(person_and_weight))
# print(person)
# print(weight)
i=0
#--------------------------------------這邊是在做列簡化
for i in range(0,4):
    if min(weight[i])!=0:
        for j in range(0,4):
            column_reduse_weight[i].append(weight[i][j]-min(weight[i]))
    else:
        column_reduse_weight[i].append(weight[i][j])
print(column_reduse_weight)
#----------------------------------------------------
row_reduse_weight=[[] for i in range(4)]
#-------------------------------------這邊是在做行簡化
# for j in range(0, 4):
#     for i in range(0,4):
#         if min(column_reduse_weight[i][j])!=0:
#             for j in range(0,4):
#                 row_reduse_weight[i].append(column_reduse_weight[i][j]-min(column_reduse_weight[i]))
#         else:
#            row_reduse_weight[i].append(column_reduse_weight[i][j])
# print(row_reduse_weight)
#---------------------------------------------------

x=np.array([[1,2,3],[5,7,4],[4,2,9]])
print(x)