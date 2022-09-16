import pygame, sys
from settings import *

class Game:
  def _init_(self):
    #general setup
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
    self.clock = pygame.time.clock()

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.quit()
      self.screen.fill("Black")
      pygame.display.update()
      self.clock.tick(FPS)

if __name__ == '__main__':
  game = Game()
  game.run