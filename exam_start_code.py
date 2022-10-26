
import re


def exercise1(array2D):
    result=0
    for i in array2D:
        for j in i:
            result+=j
    return result

def exercise2():
    result=[]
    for i in range(1,21):
        result.append(i**2)
    return result


def exercise3(x, y, z):
    if x==y or y==z or x==z:
        result=0
    else:
        result=x+y+z
    return result

def exercise4(array1, array2):
    result=[]
    for i in range(len(array1)):
        result.append(array1[i]+array2[i])
    return result


def exercise5(array):
    result=[]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]%3==0:
                result.append((i,j))
    return result


    
array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]

print(exercise1([[1,2,3],[4,5]]))

print(exercise2())

print(exercise3(5,15,23))
print(exercise3(True,False,True))

print(exercise4([1,2,3,4],[5,6,7,8]))

print(exercise5(array))