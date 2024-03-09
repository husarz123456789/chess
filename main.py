import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((177, 135, 107))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # horizontal lines
    pygame.draw.line(window, 'black', (20, 20), (420, 20), 2)
    pygame.draw.line(window, 'black', (20, 70), (420, 70), 2)
    pygame.draw.line(window, 'black', (20, 120), (420, 120), 2)
    pygame.draw.line(window, 'black', (20, 170), (420, 170), 2)
    pygame.draw.line(window, 'black', (20, 220), (420, 220), 2)
    pygame.draw.line(window, 'black', (20, 270), (420, 270), 2)
    pygame.draw.line(window, 'black', (20, 320), (420, 320), 2)
    pygame.draw.line(window, 'black', (20, 370), (420, 370), 2)
    pygame.draw.line(window, 'black', (20, 420), (420, 420), 2)
    # vertical lines
    pygame.draw.line(window, 'black', (20, 20), (20, 420), 2)
    pygame.draw.line(window, 'black', (70, 20), (70, 420), 2)
    pygame.draw.line(window, 'black', (120, 20), (120, 420), 2)
    pygame.draw.line(window, 'black', (170, 20), (170, 420), 2)
    pygame.draw.line(window, 'black', (220, 20), (220, 420), 2)
    pygame.draw.line(window, 'black', (270, 20), (270, 420), 2)
    pygame.draw.line(window, 'black', (320, 20), (320, 420), 2)
    pygame.draw.line(window, 'black', (370, 20), (370, 420), 2)
    pygame.draw.line(window, 'black', (420, 20), (420, 420), 2)
    # fields
    # row 1
    pygame.draw.rect(window, 'black', (70, 20, 50, 50))
    pygame.draw.rect(window, 'black', (170, 20, 50, 50))
    pygame.draw.rect(window, 'black', (270, 20, 50, 50))
    pygame.draw.rect(window, 'black', (370, 20, 50, 50))
    # row 2
    pygame.draw.rect(window, 'black', (20, 70, 50, 50))
    pygame.draw.rect(window, 'black', (120, 70, 50, 50))
    pygame.draw.rect(window, 'black', (220, 70, 50, 50))
    pygame.draw.rect(window, 'black', (320, 70, 50, 50))
    # row 3
    pygame.draw.rect(window, 'black', (70, 120, 50, 50))
    pygame.draw.rect(window, 'black', (170, 120, 50, 50))
    pygame.draw.rect(window, 'black', (270, 120, 50, 50))
    pygame.draw.rect(window, 'black', (370, 120, 50, 50))
    # row 4
    pygame.draw.rect(window, 'black', (20, 170, 50, 50))
    pygame.draw.rect(window, 'black', (120, 170, 50, 50))
    pygame.draw.rect(window, 'black', (220, 170, 50, 50))
    pygame.draw.rect(window, 'black', (320, 170, 50, 50))
    # row 5
    pygame.draw.rect(window, 'black', (70, 220, 50, 50))
    pygame.draw.rect(window, 'black', (170, 220, 50, 50))
    pygame.draw.rect(window, 'black', (270, 220, 50, 50))
    pygame.draw.rect(window, 'black', (370, 220, 50, 50))
    # row 6
    pygame.draw.rect(window, 'black', (20, 270, 50, 50))
    pygame.draw.rect(window, 'black', (120, 270, 50, 50))
    pygame.draw.rect(window, 'black', (220, 270, 50, 50))
    pygame.draw.rect(window, 'black', (320, 270, 50, 50))
    # row 7
    pygame.draw.rect(window, 'black', (70, 320, 50, 50))
    pygame.draw.rect(window, 'black', (170, 320, 50, 50))
    pygame.draw.rect(window, 'black', (270, 320, 50, 50))
    pygame.draw.rect(window, 'black', (370, 320, 50, 50))
    # row 8
    pygame.draw.rect(window, 'black', (20, 370, 50, 50))
    pygame.draw.rect(window, 'black', (120, 370, 50, 50))
    pygame.draw.rect(window, 'black', (220, 370, 50, 50))
    pygame.draw.rect(window, 'black', (320, 370, 50, 50))
    pygame.display.update()
