import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class of  managing by bullet"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object in current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Creating bullet in pos (0, 0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Save pos in float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves bullet up by screen"""
        # Update of pos of bullet in float
        self.y -= self.speed_factor
        # Update of rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)