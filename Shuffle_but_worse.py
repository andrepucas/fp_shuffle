import pygame

def main():

    pygame.init()

    res = (1280, 720)
    screen = pygame.display.set_mode(res)

    image = pygame.image.load("shuffle.png")

    while (True):
        
        for event in pygame.event.get():
            
            if (event.type == pygame.QUIT):
                exit()
        
        screen.fill((0,0,20))

        screen.blit(image, (240,20))

        pygame.draw.rect(screen, (225, 255, 0), (570, 300, 140, 30), 2)
        pygame.draw.rect(screen, (225, 255, 0), (570, 340, 140, 30), 2)
        pygame.draw.rect(screen, (225, 255, 0), (570, 380, 140, 30), 2)
        pygame.draw.rect(screen, (225, 255, 0), (570, 420, 140, 30), 2)
        pygame.draw.rect(screen, (225, 255, 0), (570, 460, 140, 30), 2)
        pygame.draw.rect(screen, (225, 255, 0), (570, 520, 140, 30), 2)
       

        pygame.display.flip()

main()

        