import pygame
import pygame.freetype

# color sets
yellow = (255, 255, 0)
white = (255, 255, 255)

pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)

image = pygame.image.load("shuffle.png")
my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

# front page, menu with game options
def menu():

    while (True):
        
        for event in pygame.event.get():
            
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()
        
        # background
        screen.fill((0,0,20))
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

# gets button message, position, area, and action
def button(text, x, y, width, height, action = None):
    mouse = pygame.mouse.get_pos() 
    click = pygame.mouse.get_pressed() 


    # when hovered
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, white, (x, y, width, height), 2)
        my_font.render_to(screen, (x + (width/2.8), y + (height/5)), text, white)

        # if clicked
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                exit()
            if action == "back":
                menu()
            if action == "4x3":
                level_4x3()
                   
    # not hovered
    else:
        pygame.draw.rect(screen, yellow, (x, y, width, height), 2)
        my_font.render_to(screen, (x + (width/2.8), y + (height/5)), text, yellow)

# first level
def level_4x3():

    while (True):

        for event in pygame.event.get():
            
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()
        
        screen.fill((0,0,20))

        button("Exit", 10, 680, 100, 30, "back")

        pygame.display.flip()

# starts running here    
menu()

        