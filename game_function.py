import pygame
import sys
#tracking keyboard and mouse movements
def check_keydown_events(event,ship):
    if event.key==pygame.K_RIGHT:
    #moving ship right
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
def update_screen(ai_settings,screen,ship,naruto):
    #The screen is redrawn on each iteration of the loop
    screen.fill(ai_settings.bg_colour)
    ship.blitme()
    naruto.blitme()
    pygame.display.flip() 