import pygame


class Ship:
    """" ship's class"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # put each new ship at the center bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store the fraction in the attribution of the ship
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed_up = False

    def update(self):
        """move the ship according to the moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.speed_up:
                self.x += self.settings.ship_speed
            else:
                self.x += 1
        if self.moving_left and self.rect.left > 0:
            if self.speed_up:
                self.x -= self.settings.ship_speed
            else:
                self.x -= 1
        if self.moving_up and self.rect.top > 0:
            if self.speed_up:
                self.y -= self.settings.ship_speed
            else:
                self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.speed_up:
                self.y += self.settings.ship_speed
            else:
                self.y += 1
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """plot the ship at the specific position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """put the ship at the center of screen bottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)