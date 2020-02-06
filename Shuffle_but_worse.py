import pygame
import pygame.freetype
import random

# color sets
SCREEN = (0, 0, 20)
CARD = (0, 128, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
I_COLORS = (YELLOW, GREEN, RED, CYAN, BLUE, MAGENTA)

# shapes
SQUARE = 'square'
TRIANGLE = 'triangle'
CIRCLE = 'circle'
I_SHAPES = (SQUARE, TRIANGLE, CIRCLE)

# general dimensions
WINDOW = (1280,720)
GAP = 10            # <- gap inbetween cards
TOP_MARGIN = 60     # <- this value is fixed
SIDE_MARGIN = 390   # <- this one varies sligthly, adjusted individually later

# pygame settings
pygame.init()
res = WINDOW
screen = pygame.display.set_mode(res)
image = pygame.image.load("shuffle.png")
my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

# front page menu
def menu():
    while (True): 
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()

        # background
        screen.fill(SCREEN)

        # header
        screen.blit(image, (240,20))

        # buttons
        button("4x3", 570, 300, 140, 30, "4x3")
        button("4x4", 570, 340, 140, 30, "4x4")
        button("5x4", 570, 380, 140, 30, "5x4")
        button("6x5", 570, 420, 140, 30, "6x5")
        button("6x6", 570, 460, 140, 30, "6x6")
        button("Exit", 570, 520, 140, 30, "quit")
       
        pygame.display.flip()

# button function, gets message, position, area, and action
def button(text, x, y, width, height, action = None):
    mouse = pygame.mouse.get_pos() 
    click = pygame.mouse.get_pressed() 

    # when hovered
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, WHITE, (x, y, width, height), 2)
        my_font.render_to(screen, (x + (width/2.8), y + (height/5)), text, WHITE)

        # if clicked
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                exit()
            elif action == "back":
                menu()
            elif action == "4x3":
                levelSize = "4x3"
                game_loop(levelSize)
            elif action == "4x4":
                levelSize = "4x4"
                game_loop(levelSize)
            elif action == "5x4":
                levelSize = "5x4"
                game_loop(levelSize)
            elif action == "6x5":
                levelSize = "6x5"
                game_loop(levelSize)
            elif action == "6x6":
                levelSize = "6x6"
                game_loop(levelSize)
                   
    # not hovered
    else:
        pygame.draw.rect(screen, YELLOW, (x, y, width, height), 2)
        my_font.render_to(screen, (x + (width/2.8), y + (height/5)), text, YELLOW)

# Levels, Gameplay Loop
def game_loop(levelSize):
    
    # playing board and cards dimensions
    if (levelSize == '4x3'):
        BOARD_X = 4 # board width
        BOARD_Y = 3 # board height
        cardWidth = 115     
        cardHeight = 190
    elif (levelSize == '4x4'):
        BOARD_X = 4 
        BOARD_Y = 4 
    elif (levelSize == '5x4'):
        BOARD_X = 5 
        BOARD_Y = 4
    elif (levelSize == '6x5'):
        BOARD_X = 6 
        BOARD_Y = 5
    elif (levelSize == '6x6'):
        BOARD_X = 6 
        BOARD_Y = 6
    
    mouse = pygame.mouse.get_pos() 
    click = pygame.mouse.get_pressed() 
    
    # saves the first card selected to be compared later
    firstCard = None
    # generates random board
    board = createBoard(BOARD_X, BOARD_Y)
    # list of combos found, starts empty
    combosFound = combosFoundResults(False, BOARD_X, BOARD_Y)

    while (True):
        
        screen.fill(SCREEN)
        # draws cards in board
        getBoard(board, combosFound, BOARD_X, BOARD_Y, cardWidth, cardHeight)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()
        
        button("Exit", 10, 680, 100, 30, "back")

        pygame.display.flip()

# creates all the playable card combos in the game
def createBoard(width, height):
    
    # all possible combos with the colors and shapes assigned
    combos = []
    for color in I_COLORS:
        for shape in I_SHAPES:
            combos.append( (shape, color) ) 
    
    # shuffles all combinations and selects only the needed pairs according
    # to the size of the level (board dimensions) 
    random.shuffle(combos)
    combosNeeded = int(width * height / 2)
    combos = combos[:combosNeeded] * 2
    random.shuffle(combos)

    board = []
    column = []
    for x in range(width):
        for y in range(height):

            # cycle of always adding the first combo in combos[],
            # which is deleted right after. Causing it to be
            # a different combo in every cycle  
            column.append(combos[0])
            del combos[0]
        board.append(column)
    return board

# draws board with cards
def getBoard(board, combosFound, width, height, cardWidth, cardHeight):
    for xCard in range(width):
        for yCard in range(height):
            x, y = cardPos(xCard, yCard, cardWidth, cardHeight)
            # only draws the cards pairs that havent yet been revealed
            if not combosFound[xCard][yCard]:
                pygame.draw.rect(screen, CARD, (x, y, cardWidth, cardHeight))

# card position in pixels
def cardPos(xCard, yCard, cardWidth, cardHeight):
    x = xCard * (cardWidth + GAP) + SIDE_MARGIN
    y = yCard * (cardHeight + GAP) + TOP_MARGIN
    return (x, y)

# list of Bools that stores if a combo has been found
def combosFoundResults(res, width, height):
    combosFound = []
    for i in range(width):
        combosFound.append([res] * height)
    return combosFound

##### starts running here #####   
menu()

        