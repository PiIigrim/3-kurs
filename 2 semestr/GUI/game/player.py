import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load('c:/work/2 semestr/GUI/game/graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.SL_ready = True
        self.shoot_time = 0
        self.shoot_cooldown = 600
        self.SL_shoot_time = 0
        self.SL_shoot_cooldown = 10000

        self.lasers = pygame.sprite.Group()
        self.SL_laser = pygame.sprite.Group()

        self.laser_sound = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/laser.wav')
        self.laser_sound.set_volume(0.4)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot()
            self.ready = False
            self.shoot_time = pygame.time.get_ticks()
            self.laser_sound.play()

        if keys[pygame.K_LCTRL] and self.SL_ready:
            self.SL_shoot()
            self.SL_ready = False
            self.SL_shoot_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.ready = True
    
    def SL_recharge(self):
        if not self.SL_ready:
            SL_current_time = pygame.time.get_ticks()
            if SL_current_time - self.SL_shoot_time >= self.SL_shoot_cooldown:
                self.SL_ready = True


    def constrain(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def shoot(self):
        self.lasers.add(Laser(self.rect.center, 8, self.rect.bottom))

    def SL_shoot(self):
        self.SL_laser.add(Laser(self.rect.center, 15, self.rect.top))

    def is_SL_ready_to_shoot(self):
        return self.SL_ready

    def update(self):
        self.get_input()
        self.constrain()
        self.recharge()
        self.SL_recharge()
        self.lasers.update()
        self.SL_laser.update()