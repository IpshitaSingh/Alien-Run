import pygame
from graphics import Graphics
from utils import Utils

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.velocity = 5
        self.image = Graphics.load_image("assets/player.png")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity

        #ensure player stays within screen bounds
        self.x = Utils.clamp(self.x, 0, 800 - self.width)
        self.y = Utils.clamp(self.y, 0, 600 - self.height)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def check_collision(self, other):
        return self._check_rect_collision(self.x, self.y, self.width, self.height, other.x, other.y, other.width, other.height)

    def _check_rect_collision(self, x1, y1, w1, h1, x2, y2, w2, h2):
        return pygame.Rect(x1, y1, w1, h1).colliderect(pygame.Rect(x2, y2, w2, h2))

    def reset_position(self):
        self.x = 50
        self.y = 50


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100  
        self.height = 100 
        self.velocity_x = 3  
        self.velocity_y = 2 
        original_image = Graphics.load_image("assets/enemy.png")
        #scale enemy img to desired dimensions
        self.image = pygame.transform.scale(original_image, (self.width, self.height))
        self.window_width = 800 
        self.window_height = 600  

    def update(self):
        #update the enemy's position based on velocity
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        #reverse direction if the enemy reaches the window boundaries
        if self.x <= 0 or self.x + self.width >= self.window_width:
            self.velocity_x = -self.velocity_x
        if self.y <= 0 or self.y + self.height >= self.window_height:
            self.velocity_y = -self.velocity_y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def check_collision(self, other):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(pygame.Rect(other.x, other.y, other.width, other.height))


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50  
        self.height = 150  
        self.velocity = 3  
        original_image = Graphics.load_image("assets/obstacle.png")
        #scale obstacle img to desired dimensions
        self.image = pygame.transform.scale(original_image, (self.width, self.height))
        self.window_width = 800  # Window width

    def update(self):
        #update the obstacle's position based on velocity
        self.x -= self.velocity

        #respawn the obstacle if it moves beyond the window
        if self.x + self.width <= 0:
            self.x = self.window_width  

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

def create_obstacles(window_width, window_height):
    NUM_OBSTACLES = 5
    start_x = window_width + 50
    start_y = 100
    gap = 200
    obstacle_height = 150
    obstacles = []
    for i in range(NUM_OBSTACLES):
        obstacle = Obstacle(start_x, start_y + i * (obstacle_height + gap))
        obstacles.append(obstacle)
    return obstacles


class Level1:
    def __init__(self):
        self.enemies = [Enemy(200, 200)]  

    def update(self):
        #update logic for the level
        for enemy in self.enemies:
            enemy.update()

    def draw(self, win):
        #draw level elements
        for enemy in self.enemies:
            enemy.draw(win)

