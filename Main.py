import random
def pretty_print(mas):
    print('-'*10)
    for row in mas:
        print(*row)
    print('-'*10)
def get_number(i,j):
    return i*4+j+1
def get_index(num):
    num-=1
    x,y = num//4, num % 4
    return x,y
def two_or_four(mas,x,y):
    if random.random()<=0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas
def get_empty_list(mas):
    empty=[]
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number(i,j)
                empty.append(num)
    return empty

mas=[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

mas[1][2]=2
mas[3][0]=4
pretty_print(mas)
print(get_empty_list(mas))