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
CELLS = np.full( (GRID_SIZE, GRID_SIZE), -1)

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
    CELLS[x][y] *= -1
    print(CELLS[x][y])

## Count neighbours
def cell_cycle(xpos, ypos):
    ## Some special cases
    sum = 0
    for x in range(xpos - 1, xpos + 1):
        for y in range(ypos - 1, ypos + 1):
            sum += CELLS[x][y]
    if sum == -7:
        print("FEW")

## One Life Cycle
def life_cycle():
    for x in range(0, GRID_SIZE - 1):
        for y in range(0, GRID_SIZE - 1):
            cell_cycle(x,y)

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
    FPS = 50
    clock = pygame.time.Clock()
    
    #Draw basics
    draw_grid()
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 115:
                    print("Draw Mode Toggle")
                    draw_mode = not draw_mode
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




