import contans
from soldier import *
matrix = [["SOLDIER BODY" ,"SOLDIER BODY" ,"EMPTY" ,"MINE" ], ["SOLDIER BODY" ,"SOLDIER BODY" ,"MINE" , "EMPTY"], [ "SOLDIER LEG","SOLDIER LEG" , "MINE", "FLAG" ]]


def is_body_on_flag():
    for loc in contans.FLAG_INDEX:
        for body in solder_body_place():
            if loc == body:
                return True
            else:
                continue

def is_leg_on_mine():
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == contans.MINE:
                return True
            else:
                continue

# def is_win():
#     if solder_place() in flag_loc():
#         return True
#     else:
#         return False
#
# print(is_win())