import pygame
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
""" Recursive fractal function """
def recursive_fractal(x, y, width, height, count, screen):
    pass
 
""" Draw shape based on wanted position (x,y) and size (width, height) """
def draw_shape(x,y,width,height, screen):
    pygame.draw.line(screen,
                    BLACK,
                    [x + width* 0.25, height // 2 + y],
                    [x + width* 0.75, height // 2 + y],
                    3)
    pygame.draw.line(screen,
                    BLACK,
                    [x + width * 0.25, (height * 0.5) // 2 + y],
                    [x + width * 0.25,  (height * 1.5) // 2 + y],
                    3)
    pygame.draw.line(screen,
                    BLACK,
                    [x + width * 0.75, (height * 0.5) // 2 + y],
                    [x + width * 0.75, (height * 1.5) // 2 + y],
                    3)

""" main function that will be executed """
def main(): 
    # Init 
    running = True
    width, height = 700, 700
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(WHITE)

        """ Should draw fractals of certain depth as indicated in GitHub """
        fractal_depth = 3
        recursive_fractal(0, 0, width, height, fractal_depth, screen)
    
        pygame.display.flip()
        clock.tick(20)
    
    pygame.quit()

if __name__ == "__main__":
    main()