"""
Visualisation of towers of Hanoi. 
All code in this file is completed.
"""

import pygame, time

pygame.init()
pygame.display.set_caption("Towers of Hanoi")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# game vars:
framerate = 60
steps = 0
disks = []
towers_midx = {"A": 120, "B":320, "C":520}

# colors:
white = (255, 255, 255)
black = (0, 0, 0)
blue = (78,162,196) 
green = (77, 206, 145)

def blit_text(screen, text, midtop, aa=True, font_name = None, size = None, color=white):
    font = pygame.font.SysFont(font_name, size)     
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)

def draw_towers():
    global screen
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(screen, green, pygame.Rect(xpos, 400, 160 , 20))
        pygame.draw.rect(screen, black, pygame.Rect(xpos+75, 200, 10, 200))
    blit_text(screen, 'Start', (towers_midx["A"], 403), font_name='mono', size=14, color=black)
    blit_text(screen, 'Finish', (towers_midx["C"], 403), font_name='mono', size=14, color=black)
    
def draw_disks():
    global screen, disks
    for disk in disks:
        pygame.draw.rect(screen, blue, disk['rect'])
    return

def update_visuals():
    screen.fill(white)
    draw_towers()
    draw_disks()
    blit_text(screen, 'Steps: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
    pygame.display.flip()
    clock.tick(framerate)

def make_disks(n_disks):
    global disks
    height_disk = 20
    ypos = 397 - height_disk
    width = n_disks * 23
    for i in range(n_disks):
        disk = {}
        disk['rect'] = pygame.Rect(120-width/2, ypos, width, height_disk)
        disk['val'] = n_disks-i
        disk['tower'] = "A"
        disks.append(disk)
        ypos -= height_disk+3
        width -= 23
        print(disk)

def game_loop(n, source, destination):
    # Setup
    global steps
    active_disk = None
    height_factor = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for disk in disks:
        if disk["val"] == n:
            active_disk = disk
    for disk in disks:
        if disk["tower"] == destination:
            height_factor+=1
            
    # Move active disk to correct position (in multiple steps)
    steps+=1
    active_disk["rect"].midtop = (towers_midx[source], 100)
    update_visuals()
    time.sleep(0.5)
    active_disk["rect"].midtop = (towers_midx[destination], 100)
    active_disk["tower"] = destination
    update_visuals()
    time.sleep(0.5)
    active_disk["rect"].midtop = (towers_midx[destination], 400-height_factor*23) 
    update_visuals()
    time.sleep(0.5)

    