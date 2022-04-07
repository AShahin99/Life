import random
def dead_state(height = 10, width= 10):
    return [[0 for j in range(width)] for i in range(height)]

def kill_board(state):
    for r in range(len(state)):
        for c in range(len(state[0])):
            state[r][c] = 0
    return state

def random_state(state):
    height = len(state)
    width = len(state[0])
    state = kill_board(state)
    for h in range(height):
        for w in range(width):
            if(random.random() >= 0.9):
                state[h][w] = 1
            else:
                state[h][w] = 0
    return state

def render(state):
    width = len(state[0])
    height = len(state)
    print('--------'*len(state[0]))
    for h in range(len(state)):
        row = '|'
        for w in range(len(state[0])):
            if(state[h][w] == 1):
                row+='   *   |'
            else:
                row+='       |'
        print(row)
        print('--------'*len(state[0]))
        row = ''
    return state

def next_board_state(state):
    height = len(state)
    width = len(state[0])
    new_board = dead_state(height, width)
    for r in range(height):
        for c in range(width):
            n = 0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if(height>r+x>=0 and width>c+y>=0 and state[r+x][c+y]==1 and not (x==0 and y==0)):
                        n=n+1
            # If ALIVE and HOSPITABLE    
            if((n==2 or n==3) and (state[r][c]==1) and 0<r<height-1 and 0<c<width-1):
                new_board[r][c] = 1
            if((n==2 or n==3) and (state[r][c]==1) and (r == height-1 or c==width-1 or r == 0 or c == 0)):
                new_board[r][c] = 0
            # If DEAD and HOSPITABLE
            if(n==3 and (state[r][c]==0)):
                new_board[r][c] = 1

    return new_board

def bruteforce(state):
    new_board = dead_state(len(state),len(state[0])) # Create a new board full of zeros with the same dimensions.
    for r in range(len(state)):
        for c in range(len(state[0])):
            # Top row actions
            if(r == 0):
                n=0
                # Top left corner
                if(c == 0):
                    if(state[r+1][c] == 1):
                        n=n+1
                    if(state[r][c+1] == 1):
                        n=n+1
                    if(state[r+1][c+1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
                # Top right corner
                elif(c == len(state[0])-1):
                    if(state[r+1][c] == 1):
                        n=n+1
                    if(state[r][c-1] == 1):
                        n=n+1
                    if(state[r+1][c-1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
                # Top row middle section
                else: 
                    if(state[r][c-1] == 1):
                        n=n+1
                    if(state[r][c+1] == 1):
                        n=n+1
                    if(state[r+1][c-1] == 1):
                        n=n+1
                    if(state[r+1][c] == 1):
                        n=n+1
                    if(state[r+1][c+1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
            # Bottom row actions
            elif(r == len(state)-1):
                n=0
                # Bottom left corner
                if(c == 0):
                    if(state[r-1][c] == 1):
                        n=n+1
                    if(state[r][c+1] == 1):
                        n=n+1
                    if(state[r-1][c+1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
                # Bottom right corner
                elif (c == len(state[0])-1):
                    if(state[r-1][c] == 1):
                        n=n+1
                    if(state[r][c-1] == 1):
                        n=n+1
                    if(state[r-1][c-1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
                # Bottom row middle section
                else:
                    if(state[r][c-1] == 1):
                        n=n+1
                    if(state[r][c+1] == 1):
                        n=n+1
                    if(state[r-1][c-1] == 1):
                        n=n+1
                    if(state[r-1][c] == 1):
                        n=n+1
                    if(state[r-1][c+1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
            # Middle rows actions
            else:
                n=0
                # Middle left edge
                if(c == 0):
                    if(state[r-1][c] == 1):
                        n=n+1
                    if(state[r+1][c] == 1):
                        n=n+1
                    if(state[r-1][c+1] == 1):
                        n=n+1
                    if(state[r][c+1] == 1):
                        n=n+1
                    if(state[r+1][c+1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
                # Middle right edge
                elif (c == len(state[0])-1):
                    if(state[r-1][c] == 1):
                        n=n+1
                    if(state[r+1][c] == 1):
                        n=n+1
                    if(state[r-1][c-1] == 1):
                        n=n+1
                    if(state[r][c-1] == 1):
                        n=n+1
                    if(state[r+1][c-1] == 1):
                        n=n+1
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
                # Middle row middle section
                else:
                    if(state[r][c-1] == 1):
                        n=n+1
                    if(state[r][c+1] == 1):
                        n=n+1
                    if(state[r-1][c-1] == 1):
                        n=n+1
                    if(state[r-1][c] == 1):
                        n=n+1
                    if(state[r-1][c+1] == 1):
                        n=n+1
                    if(state[r+1][c-1] == 1):
                        n=n+1
                    if(state[r+1][c] == 1):
                        n=n+1
                    if(state[r+1][c+1] == 1):
                        n=n+1    
                    # If ALIVE and HOSPITABLE    
                    if((n==2 or n==3) and (state[r][c]==1)):
                        new_board[r][c] = 1
                    # If DEAD and HOSPITABLE
                    if((n==3) and (state[r][c]==0)):
                        new_board[r][c] = 1
    state = new_board
    return state