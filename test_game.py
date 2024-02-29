import pytest
from game_entities import Player, Enemy, Obstacle, create_obstacles
from main import Game

#test creating obstacles
def test_create_obstacles():
    obstacles = create_obstacles(800, 600)
    assert len(obstacles) == 5  #check if correct number of obstacles is created
    for obstacle in obstacles:
        assert isinstance(obstacle, Obstacle)  #ensure each obstacle is an instance of Obstacle class

#test collision detection between player & enemy
def test_collision_detection():
    player = Player(50, 50)
    enemy = Enemy(50, 50)
    assert player.check_collision(enemy)  

#test if score increases based on time survived
def test_score_incrementation():
    game = Game()
    start_score = game.score
    #simulate a time period passing 
    game.start_time -= 10000  #subtract 10 seconds from the start time
    game.increase_score()
    assert game.score == start_score + 250  #check if score is increased by 250 after 10 seconds

if __name__ == "__main__":
    pytest.main()
