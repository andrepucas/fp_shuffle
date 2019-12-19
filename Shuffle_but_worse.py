import pygame
import pygame.freetype

def main():

    pygame.init()

    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    image = pygame.image.load("shuffle.png")
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    while (True):
        
        for event in pygame.event.get():
            
            if (event.type == pygame.QUIT):
                exit()
        
        # background
        screen.fill((0,0,20))
        # header
        screen.blit(image, (240,20))
        # 4x3
        pygame.draw.rect(screen, (225, 255, 0), (570, 300, 140, 30), 2)
        my_font.render_to(screen, (620, 305), "4x3", (255, 255, 0))
        # 4x4
        pygame.draw.rect(screen, (225, 255, 0), (570, 340, 140, 30), 2)
        my_font.render_to(screen, (620, 345), "4x4", (255, 255, 0))
        # 5x4
        pygame.draw.rect(screen, (225, 255, 0), (570, 380, 140, 30), 2)
        my_font.render_to(screen, (620, 385), "5x4", (255, 255, 0))
        # 6x5
        pygame.draw.rect(screen, (225, 255, 0), (570, 420, 140, 30), 2)
        my_font.render_to(screen, (620, 425), "6x5", (255, 255, 0))
        # 6x6
        pygame.draw.rect(screen, (225, 255, 0), (570, 460, 140, 30), 2)
        my_font.render_to(screen, (620, 465), "6x6", (255, 255, 0))
        # exit
        pygame.draw.rect(screen, (225, 255, 0), (570, 520, 140, 30), 2)
        my_font.render_to(screen, (620, 525), "Exit", (255, 255, 0))
       

        pygame.display.flip()

main()

        