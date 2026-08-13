import contans

def solder_body_place(matrix):
    body_place = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == contans.SOLDIER_BODY:
                body_place.append((row,col))
    return body_place

def solder_legs_place(matrix):
    legs_place = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == contans.SOLDIER_LEGS:
                legs_place.append((row,col))
    return legs_place