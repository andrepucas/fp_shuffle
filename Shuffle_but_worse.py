import pygame
import pygame.freetype

# color sets
normal = (255, 255, 0)
hover = (255, 255, 255)

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
        button("4x3", 570, 300, 140, 30)
        button("4x4", 570, 340, 140, 30)
        button("5x4", 570, 380, 140, 30)
        button("6x5", 570, 420, 140, 30)
        button("6x6", 570, 460, 140, 30)
        button("Exit", 570, 520, 140, 30, "quit")
       
        pygame.display.flip()

# gets button message, position, area, and action
def button(text, x, y, width, height, action = None):
    mouse = pygame.mouse.get_pos() 
    click = pygame.mouse.get_pressed() 


    # if hovered
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover, (x, y, width, height), 2)
        my_font.render_to(screen, (x + 50, y + 5), text, hover)

        # if clicked
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                exit()
                
    # normal state
    else:
        pygame.draw.rect(screen, normal, (x, y, width, height), 2)
        my_font.render_to(screen, (x + 50, y + 5), text, normal)

# starts running here    
menu()

        