import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 400
SPEED = 10
hp = 1
PLAYER_PATH = 'images\player.png'
OBSTACLE_PATH = 'images\obstacle_woman.png'
GG_PATH = 'images\gg.jpeg'

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(OBSTACLE_PATH)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def update(self):
        self.rect.x -= SPEED
        if self.rect.x < -50:
            self.kill()

    
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(PLAYER_PATH)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 0
        self.live = 1

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

obstacles_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
j = Player(130, HEIGHT - 200)
player_sprite.add(j)


time_spawn = 0

run = 1

# print(111)
random_time = random.randint(10, 20) * 100

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                j.jump()
            if event.key == pygame.K_LSHIFT:
                j.drop()
        
    time_now = pygame.time.get_ticks()
    # print(random_time)

    if time_now - time_spawn >= random_time:
        obstacles_sprite.add(Obstacle(WIDTH, HEIGHT - 100))
        time_spawn = time_now
        random_time = random.randint(5, random_time // 100 + 5) * 100
    
    j.update()
    if pygame.sprite.spritecollide(j, obstacles_sprite, True):
        print('ОЙ ЙОЙ ЙОЙ')
        hp -= 1
        print('HP', hp)
    
    if hp > 0:
        obstacles_sprite.update()
    
    if hp == 0:
        j.death()
    
    if hp < 0:
        gg = pygame.image.load(GG_PATH)
        gg = pygame.transform.scale(gg, (WIDTH, HEIGHT))
        screen.blit(gg, (0, 0))
        pygame.display.update()
        time.sleep(5)
        run = 0

        
            
    screen.fill((255, 255, 255))
    obstacles_sprite.draw(screen)
    player_sprite.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()



        

