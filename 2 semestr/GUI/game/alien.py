import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x ,y):
        super().__init__()
        scale_factor = 1.3
        alien_path = 'c:/work/2 semestr/GUI/game/graphics/' + color + '.png'
        self.image = pygame.image.load(alien_path).convert_alpha()

        original_image = pygame.image.load(alien_path).convert_alpha()

        # Масштабируем изображение
        new_width = int(original_image.get_width() * scale_factor)
        new_height = int(original_image.get_height() * scale_factor)
        self.image = pygame.transform.scale(original_image, (new_width, new_height))

        self.rect = self.image.get_rect(topleft = (x, y))

        if color == "red": self.value = 100
        elif color == "green": self.value = 200
        else: self.value = 300

    def update(self, direction):
        self.rect.x += direction

class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        self.image = pygame.image.load('c:/work/2 semestr/GUI/game/graphics/extra.png').convert_alpha()

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else: 
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft = (x, 50))

    def update(self):
        self.rect.x += self.speed