def view(mat):
    for line in mat:
        for i in line:
            print(i, end = ' ')
        print()
                
def snail(n):
    mat = [[1] * n for i in range(n)]
    flag = 0
    x = 0
    y = 0
    maxx = n
    maxy = n 
    
    for i in range(n * n):
        #################
        view(mat)
        print("x", x, "y", y)
        print("--------")
        #################
        if flag % 4 == 0:
            x += 1
            mat[y][x] += i
            if x == maxx:
                flag += 1
                maxx -= 1
                y += 1
        if flag % 4 == 1:
            mat[y][x] += i
            y += 1
            if y == maxy:
                flag += 1
                maxy -= 1
                x -= 1
        if flag % 4 == 2:
            mat[y][x] += i
            x -= 1
            if x == n - maxx:
                flag += 1
                maxx -= 1
                y -= 1 
        if flag % 4 == 3:
            mat[y][x] += i
            y -= 1
            if y == n - maxy:
                flag += 1
                maxy -= 1
                x += 1
    return(mat)


#n = int(input())
n = 5
view(snail(n))
