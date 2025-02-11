import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
SPEED = 10

PLAYER_PATH = 'images\player_iluha.png'
OBSTACLE_PATH = 'images\woman.png'

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
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))

    # def update(self):
    #     print('prizhok')

obstacles_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
player_sprite.add(Player(130, HEIGHT - 50))

time_spawn = 0

run = 1

print(111)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        
    time_now = pygame.time.get_ticks()
    random_time = random.randint(1000, 3000)

    if time_now - time_spawn >= random_time:
        obstacles_sprite.add(Obstacle(WIDTH, HEIGHT - 100))
        time_spawn = time_now
    
    obstacles_sprite.update()

    screen.fill((255, 255, 255))
    obstacles_sprite.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()



        

