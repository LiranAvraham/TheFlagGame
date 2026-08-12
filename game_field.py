import contans

matrix = [["SOLDIER BODY" ,"SOLDIER BODY" ,"EMPTY" ,"MINE" ], ["SOLDIER BODY" ,"SOLDIER BODY" ,"MINE" , "EMPTY"], [ "SOLDIER LEG","SOLDIER LEG" , "MINE", "FLAG" ]]


def solder_body_place():
    body_place = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == contans.SOLDIER_BODY:
                body_place.append((row,col))
    return body_place

def solder_legs_place():
    legs_place = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == contans.SOLDIER_LEGS:
                legs_place.append((row,col))
    return legs_place


def is_body_on_flag():
    for loc in contans.FLAG_INDEX:
        for leg in solder_legs_place():
            if loc == leg:
                return True
            else:
                return False

print(is_body_on_flag())


# def is_win():
#     if solder_place() in flag_loc():
#         return True
#     else:
#         return False
#
# print(is_win())