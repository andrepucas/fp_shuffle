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

# fixed variables
WINDOW = (1280,720)
CENTER_X = 1280 / 2
CENTER_Y = 720 / 2
GAP = 10     # <- gap inbetween cards
TOP = 60     # <- this margin value is fixed, the side margin's one isn't 
TEXT_WIN = "Congratulations!"

# pygame settings
pygame.init()
res = WINDOW
screen = pygame.display.set_mode(res)
image = pygame.image.load("shuffle.png")
my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
FRAMES = pygame.time.Clock()
FPS = 60

# front page menu
def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        pygame.display.update()
        FRAMES.tick(FPS) 

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

# Levels, Main Gameplay Loop
def game_loop(levelSize):

    # playing board and cards dimensions
    if levelSize == '4x3':
        BOARD_X = 4         # <- board width
        BOARD_Y = 3         # <- board height
        cardWidth = 115     # <- card width
        cardHeight = 190    # <- card height
        SIDE = 390          # <- side margin of the board
    elif levelSize == '4x4':
        BOARD_X = 4 
        BOARD_Y = 4
        cardWidth = 84   
        cardHeight = 140
        SIDE = 450
    elif levelSize == '5x4':
        BOARD_X = 5 
        BOARD_Y = 4
        cardWidth = 84   
        cardHeight = 140
        SIDE = 405
    elif levelSize == '6x5':
        BOARD_X = 6 
        BOARD_Y = 5
        cardWidth = 66  
        cardHeight = 110
        SIDE = 413
    elif levelSize == '6x6':
        BOARD_X = 6 
        BOARD_Y = 6
        cardWidth = 54  
        cardHeight = 90
        SIDE = 448

    # saves the first card selected to be compared later
    firstCard = None
    # generates random board
    board = createBoard(BOARD_X, BOARD_Y)
    # saves data from all found combos
    combosFound = combosFoundResults(False, BOARD_X, BOARD_Y)
    # saves data from picked combos
    combosPicked = combosPickedResults(False, BOARD_X, BOARD_Y)

    while True: 
        click = False
        mouse = pygame.mouse.get_pos() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # clicks are only accepted when the mouse is released as a way to 
            # prevent clicking spam
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                click = True

        screen.fill(SCREEN)
        # draws cards in board
        getBoard(board, combosPicked, combosFound, BOARD_X, BOARD_Y, cardWidth, 
        cardHeight, SIDE)        

        # checks mouse position over cards 
        xCard, yCard = getCard(mouse[0], mouse[1], BOARD_X, BOARD_Y, cardWidth, 
        cardHeight, SIDE)
        # if mouse is over a card
        if xCard != None and yCard != None:
            
            hoverCard(xCard, yCard, cardWidth, cardHeight, SIDE, combosPicked,
            combosFound)
    
            # clicking on a card
            if not combosPicked[xCard][yCard] and click == True:
                showCombo(board, [(xCard, yCard)], cardWidth, cardHeight, SIDE)
                combosPicked[xCard][yCard] = True

                # if this was the first card clicked
                if firstCard == None:
                    firstCard = (xCard, yCard)      
                # second card clicked
                else:
                    # shape and color of first card
                    shape1 = board[firstCard[0]][firstCard[1]][0]
                    color1 = board[firstCard[0]][firstCard[1]][1]
                    # shape and color of second card
                    shape2 = board[xCard][yCard][0]
                    color2 = board[xCard][yCard][1]

                    # combos dont match
                    if shape1 != shape2 or color1 != color2:

                        pygame.time.wait(1000)
                        
                        combosPicked[firstCard[0]][firstCard[1]] = False
                        combosPicked[xCard][yCard] = False

                        combosFound[firstCard[0]][firstCard[1]] = False
                        combosFound[xCard][yCard] = False

                        # re-cover cards
                        hideCombo(board, [(firstCard[0], firstCard[1]), 
                        (xCard, yCard)], cardWidth, cardHeight, SIDE)  

                    # combos match
                    elif shape1 == shape2 and color1 == color2:
                        
                        pygame.time.wait(1000)

                        combosPicked[firstCard[0]][firstCard[1]] = False
                        combosPicked[xCard][yCard] = False

                        combosFound[firstCard[0]][firstCard[1]] = True
                        combosFound[xCard][yCard] = True

                        # checks if player has found all combos - won
                        # returns True if confirmed
                        if gotEmAll(combosFound):
                            # updates the board 
                            getBoard(board, combosPicked, combosFound, 
                            BOARD_X, BOARD_Y, cardWidth, cardHeight, SIDE)

                            victoryScreen()
                
                    firstCard = None

        button("Exit", 10, 680, 100, 30, "back")

        pygame.display.update()
        FRAMES.tick(FPS)
       
# creates all the playable card combos in the game
def createBoard(width, height):
    
    # all possible combos with the colors and shapes assigned
    combos = []
    for color in I_COLORS:
        for shape in I_SHAPES:
            combos.append((shape, color)) 
    
    # shuffles all combinations and selects only the needed pairs according
    # to the size of the level (board dimensions) 
    random.shuffle(combos)
    combosNeeded = int(width * height / 2)
    combos = combos[:combosNeeded] * 2
    random.shuffle(combos)

    board = []
    for x in range(width):
        column = []
        for y in range(height):
            # cycle that always adds the first combo in combos[],
            # which is deleted right after, causing it to be
            # a different combo in every cycle  
            column.append(combos[0])
            del combos[0]
        board.append(column)
    return board

# draws board with cards
def getBoard(board, combosPicked, combosFound, width, height, cardWidth, 
cardHeight, SIDE):
    for xCard in range(width):
        for yCard in range(height):
            x, y = cardPixel(xCard, yCard, cardWidth, cardHeight, SIDE)
            # only draws the cards pairs that havent yet been revealed
            if not combosPicked[xCard][yCard] and not combosFound[xCard][yCard]:
                pygame.draw.rect(screen, CARD, (x, y, cardWidth, cardHeight))
            # draws the picked combos
            if combosPicked[xCard][yCard]:
                shape = board[xCard][yCard][0]
                color = board[xCard][yCard][1]

                pygame.draw.rect(screen, color, (x, y, cardWidth, cardHeight), 2)
                drawCombo(shape, color, xCard, yCard, cardWidth, cardHeight, SIDE)
            # "removes" found combos from the board
            if combosFound[xCard][yCard] and not combosPicked[xCard][yCard]:
                pygame.draw.rect(screen, SCREEN, (x, y, cardWidth, cardHeight))

# checks if mouse is over a card
def getCard(xMouse, yMouse, width, height, cardWidth, cardHeight, SIDE):
    for xCard in range(width):
        for yCard in range(height):
            x, y = cardPixel(xCard, yCard, cardWidth, cardHeight, SIDE)
            # sets a card hitbox for the hovered card and checks if the mouse
            # collides with it 
            card = pygame.Rect(x, y, cardWidth, cardHeight)
            if card.collidepoint(xMouse, yMouse):
                return (xCard, yCard)
    # returns None if the mouser isnt over any card            
    return (None, None)

# card position in pixels
def cardPixel(xCard, yCard, cardWidth, cardHeight, SIDE):
    x = xCard * (cardWidth + GAP) + SIDE
    y = yCard * (cardHeight + GAP) + TOP
    return (x, y)

# list of Bools that stores if a combo has been found
def combosFoundResults(res, width, height):
    combosFound = []
    for i in range(width):
        combosFound.append([res] * height)
    return combosFound

# list of Bools that stores if a combo has been picked
def combosPickedResults(res, width, height):
    combosPicked = []
    for i in range(width):
        combosPicked.append([res] * height)
    return combosPicked

# draws a highlighted card, doesnt hover "hidden" cards
def hoverCard(xCard, yCard, cardWidth, cardHeight, SIDE, combosPicked, combosFound):
    x, y = cardPixel(xCard, yCard, cardWidth, cardHeight, SIDE)
    if combosPicked[xCard][yCard]:
        pygame.draw.rect(screen, WHITE, (x, y, cardWidth, cardHeight), 2)
    if not combosPicked[xCard][yCard] and not combosFound[xCard][yCard]:
        pygame.draw.rect(screen, WHITE, (x, y, cardWidth, cardHeight))


# when a card is pressed, a combo is revealed 
def showCombo(board, cards, cardWidth, cardHeight, SIDE):
    
    for card in cards:
        x, y = cardPixel(card[0], card[1], cardWidth, cardHeight, SIDE)

        shape = board[card[0]][card[1]][0]
        color = board[card[0]][card[1]][1]

        # outline + shape
        pygame.draw.rect(screen, color, (x, y, cardWidth, cardHeight), 2)
        drawCombo(shape, color, card[0], card[1], cardWidth, cardHeight, SIDE)

    pygame.display.update()
    FRAMES.tick(FPS)

# hides 2 combos if they dont match
def hideCombo(board, cards, cardWidth, cardHeight, SIDE):

    for card in cards:
        x, y = cardPixel(card[0], card[1], cardWidth, cardHeight, SIDE)
        # re-cover the card
        pygame.draw.rect(screen, CARD, (x, y, cardWidth, cardHeight))

    pygame.display.update()
    FRAMES.tick(FPS)

# Winning function, returns False if there are still combos left to be found
def gotEmAll(combosFound):
    for combo in combosFound:
        if False in combo:
            return False     
    return True

# player is redirected here when he wins the game
def victoryScreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(SCREEN)
        # congratulations message
        my_font.render_to(screen, (CENTER_X - 94, CENTER_Y - 10), 
        TEXT_WIN, CYAN)
        
        button("Exit", 10, 680, 100, 30, "back")
        
        pygame.display.update()
        FRAMES.tick(FPS) 

                

# drawings of the shapes
def drawCombo(shape, color, xCard, yCard, cardWidth, cardHeight, SIDE):
    x, y = cardPixel(xCard, yCard, cardWidth, cardHeight, SIDE)

    # usefull proportions
    xHalf = int(cardWidth * 0.5)
    yHalf = int(cardHeight * 0.5)
    xQuarter = int(cardWidth * 0.25)
    yQuarter = int(cardHeight * 0.25)
    x03 = int(cardWidth * 0.31)
    x04 = int(cardWidth * 0.4)
    y04 = int(cardHeight * 0.38)

    if shape == SQUARE:
        pygame.draw.rect(screen, color, (x + x03, y + y04, 
        x04, x04))

    if shape == TRIANGLE:
        pygame.draw.polygon(screen, color, [(x + xQuarter, y + yQuarter + y04), 
        (x + xQuarter + xHalf, y + yQuarter + y04), (x + xHalf, y + y04)])
    
    if shape == CIRCLE:
        pygame.draw.circle(screen, color, (x + xHalf, y + yHalf), xQuarter)

##### starts running here #####   
menu()

        