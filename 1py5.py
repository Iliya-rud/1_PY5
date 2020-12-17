#Два множества точек задают два многоугольника. Определить расстояние между
#этими многоугольниками

import math
eps = 0.00000001


def enter():
    try:
        count_1 = int(input("Enter the number of vertices of the first polygon: "))
    except ValueError:
        print("You entered incorrect information")
        exit(-2)
    if count_1 < 3:
        print("You entered incorrect value")
        exit(-1)
    coor_1 = []
    for i in range(count_1):
        print("Entering the coordinates of the", i + 1, "vertex")
        try:
            a = float(input("enter the abscissa: "))
            b = float(input("enter the ordinate: "))
        except ValueError:
            print("You entered incorrect information")
            exit(-3)
        coor_1.append([a, b])
    try:
        count_2 = int(input("Enter the number of vertices of the second polygon: "))
    except ValueError:
        print("You entered incorrect information")
        exit(-2)
    if count_2 == 0 or count_2 < 3:
        print("You entered incorrect value")
        exit(-1)
    coor_2 = []#создали пустой список
    for i in range(count_2):
        print("Entering the coordinates of the", i + 1, "vertex")
        try:
            a = float(input("enter the abscissa: "))
            b = float(input("enter the ordinate: "))
        except ValueError:
            print("You entered incorrect information")
            exit(-3)
        coor_2.append([a, b])#заполнили конец списка
    return [coor_1, coor_2, count_1, count_2]


def distance(coor1, coor2): #Функция для поиска расстояние между точками
    a = coor1[0] - coor2[0]#расстояние по абсциссе
    b = coor1[1] - coor2[1]#расстояние по оординате
    return math.sqrt(a * a + b * b)# вернет расстояние


def normal(coor, coor1, coor2): #возвращает расстояние от точки coor до прямой, проходящей, через coor1 и coor2
    a = distance(coor, coor1)#подсчёт расстояний
    b = distance(coor, coor2)#подсчёт расстояний
    c = distance(coor1, coor2)#подсчёт расстояний
    p = 0.5*(a+b+c)
    try:
        n = (2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/(c)
    except ZeroDivisionError:
        n = 0
    if abs(n - round(n)) < eps:
        return float(round(n))
    else:
        return n


def Sgn(coor, coor1, coor2): #Если треугольник из вершин в аргуменете функции Sgn остроугольный или прямоуг, либо тупой угол находится при вершине coor, то вернёт 1 
    a = distance(coor, coor1)
    b = distance(coor, coor2)
    c = distance(coor1, coor2)
    lst = []#пустой список
    try:
        lst.append((b**2 + c**2 - a**2)/(2*c*b))# в конец пустого списка косинус между b и c
        lst.append((a**2 + c**2 - b**2)/(2*a*c))# в конец пустого списка косинус между a и c
        lst.append((a**2 + b**2 - c**2)/(2*a*b))# в конец пустого списка косинус между a и b
    except ZeroDivisionError:
        return 1
    for i in range(3):
        if abs(lst[i]) < eps:
            lst[i] = 0
    if lst[0] < 0:
        return -1
    if lst[1] < 0:
        return -1
    if lst[2] < 0:
        return 1
    lst.clear()
    return 1


def Intersec(coor1, coor2, coor3, coor4): #Если отрезки пересекаются или совпадают, то вернёт 1 иначе -1
    x1=coor1[0]
    y1=coor1[1]
    x2=coor2[0]
    y2=coor2[1]
    x3=coor3[0]
    y3=coor3[1]
    x4=coor4[0]
    y4=coor4[1]
    A1 = y1 - y2
    A2 = y3 - y4
    B1 = x2 - x1
    B2 = x4 - x3
    C1 = x1*y2 - y1*x2
    C2 = x3*y4 - y3*x4
    if A1*B2 - A2*B1 == 0 and B1*C2-B2*C1 == 0:
        if (abs(x2 - x1) + abs(x3 - x4) < abs(max(x1, x2) - max(x3, x4))) and (abs(y2 - y1) + abs(y3 - y4) < abs(max(y1, y2) - max(y3, y4))):
            return 1
        else:
            return -1
    if A1*B2 - A2*B1 == 0 and B1*C2-B2*C1 != 0:
        return -1
    x = -(-B2*C1 + B1*C2)/(A2*B1 - A1*B2)
    y = -(A2*C1 - A1*C2)/(A2*B1 - A1*B2)
    if (abs(abs(x1 - x) + abs(x2 - x) - abs(x1 - x2)) < eps) and (abs(abs(x3 - x) + abs(x4 - x) - abs(x3 - x4)) < eps) and (abs(abs(y1 - y) + abs(y2 - y) - abs(y1 - y2)) < eps) and (abs(abs(y3 - y) + abs(y4 - y) - abs(y3 - y4)) < eps):
        return 1
    else:
        return -1


def inclusion(coor_1, coor_2, count_1, count_2): #вернет 1, если вершина одного многоугольника лежит внутри другого, иначе -1
    in_polygon = False
    for i in range(count_1):
        x = coor_1[i][0]
        y = coor_1[i][1]
        for j in range(count_2):
            xp = coor_2[j][0]
            yp = coor_2[j][1]
            xp_prev = coor_2[j - 1][0]
            yp_prev = coor_2[j - 1][1]
            if (((yp <= y and y < yp_prev) or (yp_prev <= y and y < yp)) and (
                    x > (xp_prev - xp) * (y - yp) / (yp_prev - yp) + xp)):
                in_polygon = not in_polygon
        if in_polygon == True:
            return in_polygon
    for i in range(count_2):
        x = coor_2[i][0]
        y = coor_2[i][1]
        for j in range(count_1):
            xp = coor_1[j][0]
            yp = coor_1[j][1]
            xp_prev = coor_1[j - 1][0]
            yp_prev = coor_1[j - 1][1]
            if (((yp <= y and y < yp_prev) or (yp_prev <= y and y < yp)) and (
                    x > (xp_prev - xp) * (y - yp) / (yp_prev - yp) + xp)):
                in_polygon = not in_polygon
        if in_polygon == True:
            return in_polygon
    return in_polygon   


def min_distance_vert(coor_1, coor_2, count_1, count_2):
    min_distance = distance(coor_1[0], coor_2[0])
    for i in range(count_1):
        for k in range(count_2):
            tmp_distance = distance(coor_1[i], coor_2[k])
            if tmp_distance < min_distance:
                min_distance = tmp_distance
    return min_distance


def min_distance_vert_edge(coor_1, coor_2, count_1, count_2):#расстояние между точками одного многоугольника и сторонами другого
    min_distance = distance(coor_1[0], coor_2[0])
    for i in range(count_1):
        for k in range(count_2):
            if k < count_2-1:
                if Sgn(coor_1[i], coor_2[k], coor_2[k+1]) == 1:
                    tmp_distance = normal(coor_1[i], coor_2[k], coor_2[k+1])
                    if tmp_distance < min_distance:
                        min_distance = tmp_distance
            else:
                if Sgn(coor_1[i], coor_2[k], coor_2[0]) == 1:
                    tmp_distance = normal(coor_1[i], coor_2[k], coor_2[0])
                    if tmp_distance < min_distance:
                        min_distance = tmp_distance
    return min_distance


def distance_polygons(coor_1, coor_2, count_1, count_2):#собственно основная функция
    if inclusion(coor_1, coor_2, count_1, count_2) == True:
        return 0
    for i in range(count_1):
        for j in range(count_2):
            if Intersec(coor_1[i-1], coor_1[i], coor_2[j-1], coor_2[j]) == 1:
                return 0
    return min(min_distance_vert(coor_1, coor_2, count_1, count_2), min_distance_vert_edge(coor_1, coor_2, count_1, count_2))


def AutoTest():
     a = distance_polygons([[-3, 3], [3, 3], [3, -3], [-3, -3]], [[-1, 0], [1, 0], [0, 1]], 4, 3)
     b = distance_polygons([[0, 0], [0, 1], [1, 1], [1, 0]], [[2, 0], [2, 1], [3, 1], [3, 0]], 4, 4)
     c = distance_polygons([[-1, 0], [1, 0], [0, 1]], [[-2, 3], [2, 3], [0, 7]], 3, 3)
     d = distance_polygons([[-1, 0], [1, 0], [0, 1]], [[0, 2], [-1, 10], [1, 7]], 3, 3)
     if a != 0 or b != 1 or c != 2 or d != 1:
         print("AutoTest failed!!!")
     else:
         print("AutoTest passed...")

AutoTest()
lst = enter()
coor_1 = lst[0]
coor_2 = lst[1]
count_1 = lst[2]
count_2 = lst[3]
lst.clear()

print("Distance between polygons: ")
print(distance_polygons(coor_1, coor_2, count_1, count_2))
