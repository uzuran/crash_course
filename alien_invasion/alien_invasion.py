import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # Initialize game and create screen object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    ship = Ship(screen, ai_settings)
    # Make a group to store bullets in
    bullets = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Start the main loop for game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, alien)


run_game()
