import pygame
import sys
from constants import *
from player import *
from asteroid import *
from AsteroidField  import *
from shot import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)
def main():
	pygame.init()
	Clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,20,PLAYER_RADIUS)
	AstoroidField = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		Clock.tick(60)
		dt = Clock.tick(60)/1000
		player.shoot()
		updatable.update(dt)
		for obj in asteroids:
			if obj.collision(player)==True:
				print("Game over!")
				sys.exit()
		

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
	main()



