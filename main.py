import pygame
from game_entities import Player, Enemy, Obstacle, create_obstacles, Level1
from graphics import GUI

#initialize Pygame
pygame.init()
pygame.mixer.init()  #initialize Pygame mixer

#set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Run")

#load sound effects and music
collision_sound = pygame.mixer.Sound("assets/collision.mp3")
background_music = pygame.mixer.Sound("assets/background_music.mp3")

#load background img
background_image = pygame.image.load("assets/background.jpg").convert()

WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        self.player = Player(50, 50)
        self.enemy = Enemy(200, 200)
        self.obstacles = create_obstacles(WIDTH, HEIGHT)
        self.score = 0
        self.level = 1
        self.next_level_threshold = 500 * self.level
        self.start_time = pygame.time.get_ticks()
        self.time_to_increase_score = 10000
        self.clock = pygame.time.Clock()
        self.run = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self):
        self.player.update()
        self.enemy.update()
        for obstacle in self.obstacles:
            obstacle.update()

    def check_collisions(self):
        if self.player.check_collision(self.enemy):
            self.player.reset_position()
            self.score -= 10
            collision_sound.play()

        for obstacle in self.obstacles:
            if self.player.check_collision(obstacle):
                self.player.reset_position()
                self.score -= 10
                collision_sound.play()

    def increase_score(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.time_to_increase_score:
            self.score += 250
            self.start_time = current_time

    def increase_level(self):
        if self.score >= self.next_level_threshold:
            self.level += 1
            self.next_level_threshold = 500 * self.level 
            for obstacle in self.obstacles:
                obstacle.velocity += 2

    def draw(self):
        WIN.blit(background_image, (0, 0))
        self.player.draw(WIN)
        self.enemy.draw(WIN)
        for obstacle in self.obstacles:
            obstacle.draw(WIN)
        GUI.draw_text(WIN, f"Score: {self.score}", "Arial", 24, (255, 255, 255), 10, 10)
        GUI.draw_text(WIN, f"Level: {self.level}", "Arial", 24, (255, 255, 255), 10, 40)
        timer_text = pygame.font.Font(None, 36).render(f"Timer: {int((pygame.time.get_ticks() - self.start_time) / 1000)}", True, (255, 255, 255))
        WIN.blit(timer_text, (10, 70))
        pygame.display.update()

    def run_game(self):
        background_music.play(-1)
        while self.run:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.check_collisions()
            self.increase_score()
            self.increase_level()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run_game()
