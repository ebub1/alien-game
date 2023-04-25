import pygame
import sys
from bullet import Bullet
#tracking keyboard and mouse movements
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key==pygame.K_RIGHT:
    #moving ship right
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:
        #Creating a new bullet and adding into bullets group
        new_bullet = Bullet(ai_settings, screen, ship )
        bullets.add(new_bullet)
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        
def update_screen(ai_settings, screen, ship, bullets):
    #The screen is redrawn on each iteration of the loop
    screen.fill(ai_settings.bg_colour)
    #All the bullets draw behinde the ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip() 