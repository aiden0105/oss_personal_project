import pygame

# 게임 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

class Minesweeper:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]

if __name__ == "__main__":
    game = Minesweeper()
