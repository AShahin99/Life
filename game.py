import sys, pygame, life

pygame.init()
ALIVE, DEAD = 1,0
alive_count = 0
colors = white, black, grey, dark_grey, blue, red = (255,255,255),(0,0,0),(150,150,150),(110,110,110),(0,180,180), (200,0,0)
sizes = width, height, block_size = 700, 600, 10 # To make adjustable later
screen = pygame.display.set_mode((width,height)) # Create screen display

def create_board(): #  Create the underlying array to be returned
    return life.dead_state(int(height/block_size),int(height/block_size))

def home_view():
    screen.fill(grey)
    draw_grid()
    play_button(False)
    clear_button()
    pygame.display.flip() # Update the display

def play_button(playing):
    if not playing:
        start_button = pygame.Rect(width-95,100,90,45) # Create the start button and draw it
        pygame.draw.rect(screen,dark_grey,start_button)
        
        reg_font = pygame.font.Font(None, 30)
        start_txt = reg_font.render("START", True, white)
        screen.blit(start_txt,(618,115))

        pygame.display.flip()
    else:
        start_button = pygame.Rect(width-95,100,90,45) # Create the start button and draw it
        pygame.draw.rect(screen,dark_grey,start_button)

        reg_font = pygame.font.Font(None, 30)
        start_txt = reg_font.render("STOP", True, white)
        screen.blit(start_txt,(623,115))
        
        pygame.display.flip()

def clear_button():
        clear_button = pygame.Rect(width-95,155,90,45)
        pygame.draw.rect(screen,dark_grey,clear_button)
        reg_font = pygame.font.Font(None, 30)
        start_txt = reg_font.render("CLEAR", True, white)
        screen.blit(start_txt,(615,168))
        pygame.display.flip()


def kill_board(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] = 0
    return board
def draw_grid():
    for y in range(0,height,block_size):
        pygame.draw.line(screen,dark_grey,[0,y],[width-100,y])
    for x in range(0,height,block_size):
        pygame.draw.line(screen,dark_grey,[x+10,0],[x+10,height])

def grid_click(life_board, pos):
    if(life_board[int(pos[1]/block_size)][int(pos[0]/block_size)] == DEAD):
        rect = pygame.Rect(pos[0] - (pos[0]%block_size),pos[1] - (pos[1]%block_size),block_size,block_size)
        pygame.draw.rect(screen,blue,rect)
        draw_grid()
        pygame.display.flip()
        life_board[int(pos[1]/block_size)][int(pos[0]/block_size)] = ALIVE
    elif(life_board[int(pos[1]/block_size)][int(pos[0]/block_size)] == ALIVE): # If ALIVE, make DEAD
        rect = pygame.Rect(pos[0] - (pos[0]%block_size),pos[1] - (pos[1]%block_size),block_size,block_size)
        pygame.draw.rect(screen,grey,rect)
        draw_grid()
        pygame.display.flip()
        life_board[int(pos[1]/block_size)][int(pos[0]/block_size)] = DEAD

def gen_life_board(life_board):
    alive_count=0 
    for c in range(0,width-100,block_size):
        for r in range(0,height,block_size):
            rect = pygame.Rect(c,r,block_size,block_size)
            if(life_board[int(r/block_size)][int(c/block_size)]==0):
                colour = grey
            else:
                colour = blue
                alive_count = alive_count + 1
            pygame.draw.rect(screen,colour,rect,0)
    draw_grid()
    
    counter = pygame.Rect(width-95,300,90,45)
    pygame.draw.rect(screen,dark_grey,counter)
    reg_font = pygame.font.Font(None, 25)
    start_txt = reg_font.render("Count: {0}".format(alive_count), True, white)
    screen.blit(start_txt,(610,315))
    pygame.display.flip()


    
    pygame.display.flip()
    return(life.next_board_state(life_board))

def play_life():
    home_view()
    board = create_board()
    playing = False
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT): sys.exit()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if((0,0) <= event.pos <= (width-100,height) and not playing): # If the grid is clicked before we click start
                    grid_click(board,event.pos)
                elif(100 <= event.pos[1] <= 145): # If start button is clicked
                    playing = not playing
                    play_button(playing)
                elif(155 <= event.pos[1] <= 200 and not playing): 
                    gen_life_board(kill_board(board))
                    clear_button()
            if(event.type == pygame.KEYDOWN and event.__dict__['key'] ==13 and not playing):
               board = gen_life_board(board)

        if playing:
            board = gen_life_board(board)
            
if __name__ == "__main__":
    play_life()