import numpy as np

#----------------------------建立畫線矩陣
def build_draw_line_matrix():
    draw_line_matrix=np.zeros((4,4))
    draw_line_matrix=draw_line_matrix.astype(int)
    return draw_line_matrix
#------------------------------- 如果發現所有的零都已經被劃線了則，則跳出迴圈。
def if_there_is_no_zero_in_matrix_than_break(display_zero_matrix):
    zero_number=0
    for i in range(0,4):
        zero_number+=list(display_zero_matrix[i]).count(0)
    if zero_number==0:
        return False
    else:
        return True

#-----------------------------------------------------開始畫線

#------------------------方法2用list與turple組合來劃線
#------------------------------計算總共有多少個零
def count_zero_in_this_matrix(matrix,whether_reverse):
    how_many_zero_in_matrix = []  # 這個變數是為了計算s有多少個0在同一列或者同一行
    for i in range(0, 4):
        name = "row-" + str(i)
        how_many_zero_in_matrix.append((name, list(matrix[i]).count(0)))
    for i in range(0, 4):
        name = "col-" + str(i)
        how_many_zero_in_matrix.append((name, list(matrix[:, i]).count(0)))

    # print(how_many_zero_in_matrix)
    if whether_reverse==1:
        sort_how_many_zero_in_matrix = sorted(how_many_zero_in_matrix, key=lambda s: s[1], reverse=True)
    else:
        sort_how_many_zero_in_matrix = sorted(how_many_zero_in_matrix, key=lambda s: s[1], reverse=False)
    return sort_how_many_zero_in_matrix

def build_display_zero_matrix(matrix):
    display_zero_matrix=np.zeros((4,4))
    display_zero_matrix=display_zero_matrix.astype(int)
    for i in range(0,4):
        for j in range(0,4):
            if matrix[i][j]==0:
                display_zero_matrix[i][j]=0
            else:
                display_zero_matrix[i][j]=-99
    return display_zero_matrix


#--------------------------------------------------畫完線之後檢查，所有的0是否都被畫到了，沒有畫到則繼續loop下去
def if_element_have_zero_than_draw_a_line(sort_how_many_zero_in_matrix,display_zero_matrix,draw_line_matrix):
    for i in range(0,4):
        which_row_or_column=sort_how_many_zero_in_matrix[i][0].split("-")
        j=int(which_row_or_column[1])
        print (sort_how_many_zero_in_matrix[i][0])
        if which_row_or_column[0]=="row":
            for i in range(0,4):
                if display_zero_matrix[j][i]==0:
                    display_zero_matrix[j][i]=1
                draw_line_matrix[j][i]+=1
        elif which_row_or_column[0]=="col":
            for i in range(0,4):
                if display_zero_matrix[i][j]==0:
                    display_zero_matrix[i][j]=1
                draw_line_matrix[i][j] += 1
        if if_there_is_no_zero_in_matrix_than_break(display_zero_matrix)==False:
            break
    return draw_line_matrix