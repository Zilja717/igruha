import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 400
SPEED = 10
hp = 1
PLAYER_PATH = 'images\player.png'
OBSTACLE_PATH = 'images\obstacle_woman.png'
GG_PATH = 'images\gg.png'
START_PATH = 'images\start.png'


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

points = 0

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(OBSTACLE_PATH)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def update(self):
        global points
        self.rect.x -= SPEED
        if self.rect.x < -50:
            self.kill()
            points += 1


    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(PLAYER_PATH)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 0
        self.live = 1
        self.respawn_flag = 0

    def update(self):
        if not self.live:
            self.image = pygame.transform.rotate(self.image, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
        
        if self.rect.y > 300:
            self.rect.y = 300
            self.speed = 0
        elif self.rect.y == 300:
            self.rect.y += self.speed
        else:
            self.rect.y += self.speed
            self.speed += 1
        
            
    def jump(self):
        if self.rect.y >= 295:
            self.speed = -20
            self.update()
        
    def drop(self):
        self.rect.y = 300
        self.speed = 0

    def death(self):
        self.live = 0
    
    def respawn(self):
        self.respawn_flag = 1
        self.live = 1
        self.image = pygame.image.load(PLAYER_PATH)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

obstacles_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
j = Player(130, HEIGHT - 200)
player_sprite.add(j)


time_spawn = 0

run = 1
game = 0

random_time = random.randint(10, 20) * 100

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game:
                j.jump()
                print('jump')
            if event.key == pygame.K_SPACE and not game:
                game = 1
                hp = 1
                pygame.display.update()
                print('game')
            if event.key == pygame.K_LSHIFT:
                j.drop()
                
    if game:    

        time_now = pygame.time.get_ticks()
        if time_now - time_spawn >= random_time:
            obstacles_sprite.add(Obstacle(WIDTH, HEIGHT - 100))
            time_spawn = time_now
            random_time = random.randint(5, random_time // 100 + 5) * 100
        
        j.update()
        obstacles_sprite.update()
        if pygame.sprite.spritecollide(j, obstacles_sprite, True):
            print('ОЙ ЙОЙ ЙОЙ')
            hp -= 1
        
        if hp > 0:
            game = 1
        
        if hp == 0:
            j.death()
            print(points)
        
        if hp < 0:
            gg = pygame.image.load(GG_PATH)
            gg = pygame.transform.scale(gg, (WIDTH, HEIGHT))
            screen.blit(gg, (0, 0))
            pygame.display.update()
            time.sleep(2)
            game = 0
            hp = 1
            obstacles_sprite.empty()
            points = 0
            j.respawn()


        
            
    screen.fill((255, 255, 255))
    if game:
        obstacles_sprite.draw(screen)
        player_sprite.draw(screen)
    else:
        start = pygame.image.load(START_PATH)
        start = pygame.transform.scale(start, (WIDTH, HEIGHT))
        screen.blit(start, (0, 0))
    
    pygame.display.update()

    clock.tick(60)

pygame.quit()