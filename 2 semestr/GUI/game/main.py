import pygame, sys, random
from player import Player
import obstacles
from alien import Alien, Extra
from laser import Laser

def read_stats():
    stats = {}
    with open('c:/work/2 semestr/GUI/game/stats.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            stats[key] = int(value)
    return stats

def write_stats():
    with open('c:/work/2 semestr/GUI/game/stats.txt', 'w') as f:
        for key, value in stats.items():
            f.write(f'{key}: {int(value)}\n')


class Game:
    def __init__(self):
        self.i = 0
        self.speed_multiplier = 1
        self.pause = False
        self.game_over = False
        self.level_clear = False
        self.message_shown = False
        self.stat_changed = False
        self.played = False
        self.level = 0
        self.alien_rows = 4
        self.alien_cols = 5
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.lives = 3
        self.lives_surface = pygame.image.load('c:/work/2 semestr/GUI/game/graphics/player.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.lives_surface.get_size()[0] * 2 + 20)

        self.score = 0
        self.font = pygame.font.Font('c:/work/2 semestr/GUI/game/font/Pixeled.ttf', 16)
        self.big_font = pygame.font.Font('c:/work/2 semestr/GUI/game/font/Pixeled.ttf', 64)

        self.shape = obstacles.shape
        self.block_size = 8
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 5
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_mul_obstacle(*self.obstacle_x_positions, x_start = screen_width / 15, y_start = 580)

        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.aliens_setup(rows = self.alien_rows, cols = self.alien_cols)
        self.alien_direction = 1
        self.down = 2

        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = random.randint(40, 80)

        self.music = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/music.wav')
        self.music.set_volume(0.4)
        self.music.play(loops = -1)
        self.laser_sound = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/laser.wav')
        self.laser_sound.set_volume(0.4)
        self.explosion_sound = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/explosion.wav')
        self.explosion_sound.set_volume(0.3)
        self.hit_sound = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/hit-sound.wav')
        self.hit_sound.set_volume(0.5)
        self.extra_hit_sound = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/extra-hit.wav')
        self.extra_hit_sound.set_volume(1.5)
        self.death_sound = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/death-sound.wav')
        self.death_sound.set_volume(0.5)
        self.level_clear_sound = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/level-clear.wav')
        self.level_clear_sound.set_volume(0.5)

    def restart_game(self):
        stats['alien_shot_speed'] = 800
        write_stats()
        self.stats = read_stats()
        self.i = 0
        self.level = 1
        self.death_sound.stop()
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.lives = 3
        self.lives_surface = pygame.image.load('c:/work/2 semestr/GUI/game/graphics/player.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.lives_surface.get_size()[0] * 2 + 20)

        self.score = 0
        self.font = pygame.font.Font('c:/work/2 semestr/GUI/game/font/Pixeled.ttf', 16)

        self.shape = obstacles.shape
        self.block_size = 8
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 5
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_mul_obstacle(*self.obstacle_x_positions, x_start = screen_width / 15, y_start = 580)

        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.aliens_setup(rows = self.alien_rows, cols = self.alien_cols)
        self.alien_direction = 1
        self.down = 2

        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = random.randint(40, 80)

        self.music = pygame.mixer.Sound('c:/work/2 semestr/GUI/game/audio/music.wav')
        self.music.set_volume(0.2)
        self.music.play(loops = -1)

    def new_level(self):
        self.level += 1
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.aliens_setup(rows = self.alien_rows, cols = self.alien_cols)
        self.speed_multiplier += 0.2
        self.down += 1
        if self.level % 5 == 0:
            choise = random.choice([1, 2])
            if choise == 1 : self.alien_rows += 1
            elif choise == 2 : self.alien_cols += 1
        
        if self.level % 3 == 0:
            stats['alien_shot_speed'] = stats['alien_shot_speed'] // 1.2

        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = random.randint(40, 80)
        self.stat_changed = False
        
    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacles.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_mul_obstacle(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def aliens_setup(self, rows, cols, x_distance = 100, y_distance = 60, offset_x = 70, offset_y = 60):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + offset_x
                y = row_index * y_distance + offset_y

                if row_index == 0: alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2: alien_sprite = Alien('green', x, y)
                else: alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)
    
    def alien_position_check(self):
        all_aliens = self.aliens.sprites()
        if not self.pause:
            for alien in all_aliens:
                if alien.rect.right >= screen_width:
                    self.alien_direction = -1 * self.speed_multiplier
                    self.alien_move_down(self.down)
                elif alien.rect.left <= 0:
                    self.alien_direction = 1 * self.speed_multiplier
                    self.alien_move_down(self.down)

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites() and not self.pause:
            random_alien = random.choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, screen_height)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        if not self.pause:
            self.extra_spawn_time -= 1
            if self.extra_spawn_time <= 0:
                self.extra.add(Extra(random.choice(['right', 'left']), screen_width))
                self.extra_spawn_time = random.randint(400, 800)

    def collision_checks(self):
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sound.play()

                if pygame.sprite.spritecollide(laser, self.extra, True):
                    self.extra_hit_sound.play()
                    self.score += 500
                    if self.lives < 3:
                        self.lives += 1
                    laser.kill()

        if self.player.sprite.SL_laser:
            for sl_laser in self.player.sprite.SL_laser:
                if pygame.sprite.spritecollide(sl_laser, self.blocks, True):
                    pass

                aliens_hit = pygame.sprite.spritecollide(sl_laser, self.aliens, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    self.explosion_sound.play()

                if pygame.sprite.spritecollide(sl_laser, self.extra, True):
                    self.extra_hit_sound.play()
                    self.score += 500
                    if self.lives < 3:
                        self.lives += 1

        if self.alien_lasers:
            for laser in self.alien_lasers:
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives > 0:
                        self.hit_sound.play()
                    if self.lives <= 0:
                        self.game_over = True

        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    self.game_over = True

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * (self.lives_surface.get_size()[0] + 10))
            screen.blit(self.lives_surface, (x, 8))

    def all_clear(self):
        if not self.aliens.sprites() and not self.game_over and not self.message_shown:
            self.level_clear = True
            self.message_shown = True
            self.clear_time = pygame.time.get_ticks()

    def game_over_screen(self):
        if self.lives <= 0:
            if self.i == 0:
                self.extra.empty()
                self.extra_spawn_time = 10000000
                self.music.stop()
                self.death_sound.play()
                self.aliens.empty()
                player_sprite = Player((10000, 10000), 10000, 5)
                self.player = pygame.sprite.GroupSingle(player_sprite)
                self.i += 1
            if self.level > stats['best_level']:
                best_level_surface = self.font.render(f'New best level: {self.level}', False, 'white')
                best_level_rect = best_level_surface.get_rect(center = (screen_width / 2, (screen_height / 2) + 100))
                screen.blit(best_level_surface, best_level_rect)
            if self.score > stats['best_score']:
                best_score_surface = self.font.render(f'New best score: {self.score}', False, 'white')
                best_score_rect = best_score_surface.get_rect(center = (screen_width / 2, (screen_height / 2) + 160))
                screen.blit(best_score_surface, best_score_rect)
            game_over_surface = self.big_font.render('GAME OVER', False, 'white')
            game_over_rect = game_over_surface.get_rect(center = (screen_width / 2, (screen_height / 2) - 100))
            screen.blit(game_over_surface, game_over_rect)
            game_over_surface2 = self.font.render('Press ENTER to restart', False, 'white')
            game_over_rect2 = game_over_surface.get_rect(center = (screen_width / 2, (screen_height / 2) + 40))
            screen.blit(game_over_surface2, game_over_rect2)

    def display_score(self):
        score_surface = self.font.render(f'Score: {self.score}', False, 'white')
        score_rect = score_surface.get_rect(topleft = (10, -10))
        screen.blit(score_surface, score_rect)

    def ready_to_shoot_SL(self):
        if self.player.sprite.is_SL_ready_to_shoot() and not self.pause:
            SL_surface = self.font.render(f'SL READY', False, 'white')
            SL_rect = SL_surface.get_rect(bottomleft = (10, screen_height - 10))
            screen.blit(SL_surface, SL_rect)

    def display_level(self):
        level_surface = self.font.render(f'Level: {self.level + 1}', False, 'white')
        level_rect = level_surface.get_rect(bottomright = (screen_width - 10, screen_height - 10))
        screen.blit(level_surface, level_rect)
    
    def display_clear(self):
        if not self.played:
            self.level_clear_sound.play()
            self.played = True
        if self.level > stats['best_level']:
            if not self.stat_changed:
                stats['player_SL_shot_cooldown']  = stats['player_SL_shot_cooldown'] // 1.05
            SL_shot_cd_decr_surface = self.font.render(f'SL cooldown decreased to {stats["player_SL_shot_cooldown"]} in next ship', False, 'white')
            SL_shot_cd_decr_rect = SL_shot_cd_decr_surface.get_rect(center = (screen_width / 2, (screen_height / 2) + 50))
            screen.blit(SL_shot_cd_decr_surface, SL_shot_cd_decr_rect)
        
        if self.score > stats['best_score']:
            if not self.stat_changed:
                stats['player_shot_cooldown'] = stats['player_shot_cooldown'] // 1.05
            shot_cd_decr_surface = self.font.render(f'Shot cooldown decreased to {stats["player_shot_cooldown"]} in next ship', False, 'white')
            shot_cd_decr_rect = shot_cd_decr_surface.get_rect(center = (screen_width / 2, (screen_height / 2) + 100))
            screen.blit(shot_cd_decr_surface, shot_cd_decr_rect)

        self.stat_changed = True
        level_surface = self.big_font.render(f'Level {self.level} clear!', False, 'white')
        level_rect = level_surface.get_rect(center = (screen_width / 2, (screen_height / 2) - 50))
        screen.blit(level_surface, level_rect)
                
    def run(self):
        if not self.game_over:
            self.player.update()
        if self.game_over:
            self.game_over_screen()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                stats['best_level'] = self.level
                stats['best_score'] = self.score
                stats['alien_shot_speed'] = 800
                write_stats()
                self.game_over = False
                self.restart_game()
        if self.level_clear:
            self.display_clear()
            if pygame.time.get_ticks() - self.clear_time >= 4000:
                self.level_clear = False
                self.message_shown = False
                self.played = False
                self.new_level()
        self.aliens.update(self.alien_direction)
        self.alien_position_check()
        self.alien_lasers.update()
        self.extra_alien_timer()
        self.extra.update()
        self.collision_checks()
        self.player.sprite.lasers.draw(screen)
        self.player.sprite.SL_laser.draw(screen)
        self.ready_to_shoot_SL()
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra.draw(screen)
        self.display_lives()
        self.display_score()
        self.all_clear()
        self.display_level()

if __name__ == "__main__":
    stats = read_stats()
    pygame.init()
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Космическая братва 1: Пришествие(Beta)')
    pygame.display.set_icon(pygame.image.load('c:/work/2 semestr/GUI/game/graphics/red.png').convert_alpha())
    clock = pygame.time.Clock()
    game = Game()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, stats['alien_shot_speed'])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stats['alien_shot_speed'] = 800
                write_stats()
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.update()
        clock.tick(60)