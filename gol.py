import pygame
import numpy as np

#Initialize pygame
pygame.init()

#Define values
GRID_SIZE = 100
CELL_WIDTH = 10
(WIDTH, HEIGHT) = (GRID_SIZE*CELL_WIDTH, GRID_SIZE*CELL_WIDTH)

# Create cell vector
# 1 = alive
# -1 = dead
CELLS = np.zeros( (GRID_SIZE, GRID_SIZE))

#Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (49, 51, 53)

#Initialize the screen / caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Of Life")

# Draws grid
def draw_grid():
    for x in range(0, GRID_SIZE*CELL_WIDTH, CELL_WIDTH):
        for y in range(0, GRID_SIZE*CELL_WIDTH, CELL_WIDTH):
            #Horizontal
            pygame.draw.line(screen, GRAY, (x, 0), (x, GRID_SIZE*CELL_WIDTH), 1)
            #Vertical
            pygame.draw.line(screen, GRAY, (0, y), (GRID_SIZE*CELL_WIDTH, y), 1)

## Update single cell on press
def update_cell(x, y):
    if CELLS[x][y] == 1:
        CELLS[x][y] = 0
    else:
        CELLS[x][y] = 1
    
    print((x,y))

## Count neighbours
def cell_count(xpos, ypos):
    sum = 0
    
    #Range needs extra +1 to iterate correctly over the cell (see range() command in doc)
    for x in range(xpos - 1, xpos + 1 + 1):
        for y in range(ypos - 1, ypos + 1 + 1):
            #print("Iterating x:" + str(x) + " y:" + str(y) + " value: " + str(CELLS[x][y]))
            sum += CELLS[x][y]

    #Dont count self
    if CELLS[xpos][ypos] == 1:
        sum -= 1

    return sum

## One Life Cycle
def life_cycle():
    global CELLS
    CELLS_FLIP = np.zeros( (GRID_SIZE, GRID_SIZE) ) 
    for x in range(0, GRID_SIZE - 1):
        for y in range(0, GRID_SIZE - 1):
            sum = cell_count(x,y)
            #print("Neighbours at " + str(x) + "," + str(y) +" is " + str(sum))
            if CELLS[x][y] == 1 and sum <2:
                CELLS_FLIP[x][y] = 0            
            if CELLS[x][y] == 1 and (sum == 2 or sum == 3):
                CELLS_FLIP[x][y] = 1  
            if CELLS[x][y] == 1 and sum > 3: 
                CELLS_FLIP[x][y] = 0 
            if CELLS[x][y] == 0 and sum == 3:
                CELLS_FLIP[x][y] = 1 
    CELLS = CELLS_FLIP


# Draws cells that are int 1 in CELLS. Must be some way to find all non zero values in CELLS and get those position out as a subset of positions
# 2DO: Study numpy documentation on finding nonzero positions to reduce the range to only those
def draw_cells():
    for x in range(0,GRID_SIZE - 1):
        for y in range(0, GRID_SIZE - 1):
            if CELLS[x][y] == 1:
                pygame.draw.circle(screen, WHITE, (x * CELL_WIDTH + int(CELL_WIDTH/2),y * CELL_WIDTH + int(CELL_WIDTH/2)), 5, 0)    

# Main function
def main():
    run = True
    draw_mode = False
    auto_cycle = False
    FPS = 60
    clock = pygame.time.Clock()
    
    #Draw basics
    draw_grid()
    
    while run:
        clock.tick(FPS)

        if auto_cycle == True:
            life_cycle()
            pygame.time.wait(40)

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == 115:
                    print("Draw Mode Toggle")
                    draw_mode = not draw_mode
                if event.key == 97:
                    print("Auto Mode Toggle")
                    auto_cycle = not auto_cycle
                if event.key == 116:
                    print("Cycle Once")
                    life_cycle()
         
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and draw_mode:
                #calulate pos i CELLS from mouse position
                xref = event.pos[0] // CELL_WIDTH
                yref = event.pos[1] // CELL_WIDTH
                update_cell(xref, yref)

        screen.fill(BLACK)
        draw_grid()
        draw_cells()
        pygame.display.flip()

# Main program entry point!
main()




