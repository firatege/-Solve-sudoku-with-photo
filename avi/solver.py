import numpy as np
'''board=[[0,6,0,4,2,0,0,0,1],
         [1,9,0,0,8,3,0,2,0],
         [0,0,2,0,1,0,7,0,0],
         [0,0,0,8,7,0,5,0,0],
         [0,5,1,3,4,9,0,0,2],
         [4,0,3,0,5,0,0,8,0],
         [6,0,5,1,3,2,0,0,0],
         [7,0,4,0,0,8,0,1,0],
         [0,1,0,0,6,0,8,5,0]]'''



'''board = [[0,7,0,0,1,4,0,0,0],
         [6,1,2,0,9,5,3,8,9],
         [3,0,4,0,6,8,9,7,1],
         [0,0,0,1,0,0,0,5,0],
         [2,8,0,0,0,0,7,0,3],
         [5,0,3,0,8,0,0,0,0],
         [0,2,0,0,3,0,0,0,0],
         [0,0,6,8,0,0,1,0,5],
         [0,0,0,6,7,0,4,3,0]]'''


'''board= [[0,7,0,0,1,4,0,0,0],
        [6,1,2,0,9,5,3,8,0],
        [3,0,4,0,6,8,9,7,1],
        [0,0,0,1,0,0,0,5,0],
        [2,8,0,0,0,0,7,0,3],
        [5,0,3,0,8,0,0,0,0],
        [0,2,0,0,3,0,0,0,0],
        [0,0,6,8,0,0,1,0,5],
        [0,0,0,6,7,0,4,3,0]]'''
        
def sudokuSolver(board):


    print(np.matrix(board))
    print("\n\n")
    #x,y,kare kontol verilerin listeleri
    check_x = list()
    check_y = list()
    check_s = list()
    check_t = list()
    check_c = list()



    def controlx(index_y):
        number = [1,2,3,4,5,6,7,8,9]
        for x in board[index_y]:

            for n in number:
                if x == n : number.remove(n)
        check_x.append(number)
        
    def controly(index_x):
        number = [1,2,3,4,5,6,7,8,9]
        index_y = 0
        while True:
            
            
            for m in number:
                if  board[index_y][index_x] == m : number.remove(m)
                #print(f"board[{index_y}][{index_x}] , borard: {board[index_y][index_x]} m : {m}  number: {number}")
            index_y += 1
        
            
            if index_y == 9 : break
        check_y.append(number)

    def controls(y,x):
        number = [1,2,3,4,5,6,7,8,9]
        
        if (x == 0 or x == 1 or x == 2):
                if (y == 0 or y == 1 or y == 2):
                    index_x = 0
                    index_y = 0
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 3 == 0 : index_y += 1
                        if index_x == 3 : index_x = 0
                        if index_y == 3 : break
                if (y == 3 or y == 4 or y == 5):
                    index_x = 0
                    index_y = 3
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 3 == 0 : index_y += 1
                        if index_x == 3 : index_x = 0
                        if index_y == 6 : break
                if (y == 6 or y == 7 or y == 8):
                    index_x = 0
                    index_y = 6
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                        
                        index_x += 1
                        if index_x % 3 == 0 : index_y += 1
                        if index_x == 3 : index_x = 0
                        if index_y == 9 : break
        if (x == 3 or x == 4 or x == 5):
                if (y == 0 or y == 1 or y == 2):
                    index_x = 3
                    index_y = 0
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 5 == 0 : index_y += 1
                        if index_x == 5 : index_x = 3
                        if index_y == 3 : break
                if (y == 3 or y == 4 or y == 5):
                    index_x = 3
                    index_y = 3
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 5 == 0 : index_y += 1
                        if index_x == 5 : index_x = 3
                        if index_y == 6 : break
                if (y == 6 or y == 7 or y == 8):
                    index_x = 3
                    index_y = 6
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 5 == 0 : index_y += 1
                        if index_x == 5 : index_x = 3
                        if index_y == 9 : break
        if (x == 6 or x == 7 or x == 8):
                if (y == 0 or y == 1 or y == 2):
                    index_x = 6
                    index_y = 0
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 9 == 0 : index_y += 1
                        if index_x == 9 : index_x = 6
                        if index_y == 3 : break
                if (y == 3 or y == 4 or y == 5):
                    index_x = 6
                    index_y = 3
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 9 == 0 : index_y += 1
                        if index_x == 9 : index_x = 6
                        if index_y == 6 : break
                if (y == 6 or y == 7 or y == 8):
                    index_x = 6
                    index_y = 6
                    while True:
                        for n in number:
                            if board[index_y][index_x] == n : number.remove(n)   
                            
                        index_x += 1
                        if index_x % 9 == 0 : index_y += 1
                        if index_x == 9 : index_x = 6
                        if index_y == 9 : break
            
        check_s.append(number)              
            
    def tcontrol():
        inTheT = list()
        for x in range(0,81):
            inTheT = list()
            check_c.append(check_x[x]+check_y[x]+check_s[x])
            #print(check_c)
            if(check_c[x] == 0):
                    inTheT.append(0)
            else:
                for n in range(0,10): 
                        
                        if check_c[x].count(n) == 3 : inTheT.append(n)
                    
            check_t.append(inTheT)
        #print(check_t)

    def load():
        x=0
        y=0
        for i in range(0,81):
            if check_t[i] != [0] :
                #print(f"i : {i} board[{y}][{x}]: {board[y][x]} check_t[{i}] : {check_t[i]}")
                if len(check_t[i]) == 1 : board[y][x] = check_t[i]
                
            x += 1
            if x == 9 : y += 1
            if x == 9 :  x = 0
            if y == 9 : y = 0
        
    def rebuild():
        x = 0
        y = 0

        while True:
            for n in range(0,10):
                if board[y][x] == [n]: board[y][x] = n
            x += 1
            if x == 9 : y += 1
            if x == 9 : x = 0
            if y == 9 : break
        
    def controlTheZero(board):
            index_y = 0
            while True:
                for x in range(0,9):
                    deger = board[index_y][x]
                    #print(f"x: {x} deger: {deger}")
                    if deger != 0: 
                        
                        check_x.append(0)
                        check_y.append(0)
                        check_s.append(0)
                    else:
                        controly(x)
                        controlx(index_y)
                        controls(index_y,x)
                index_y += 1
                if  index_y == 9: break
            tcontrol()
            load()
            rebuild()
            NewBoard = board
            print(np.matrix(board))
            check_x.clear()
            check_y.clear()
            check_s.clear()
            check_t.clear()
            check_c.clear()
            print("\n\n")
            for i in range(0,9):
                for j in range(0,9):
                    if board[i][j] == 0 : controlTheZero(NewBoard)
                    else: break
            return board

    controlTheZero(board)

#sudokuSolver(board)
        

    




