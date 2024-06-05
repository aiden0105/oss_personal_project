import pygame

# 게임 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
MINE_COUNT = 40 # 지뢰 총 개수

class Minesweeper:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]

    # 지뢰를 게임 보드에 무작위로 배치
    def place_mines(self):
        placed = 0
        while placed < MINE_COUNT:
            x = random.randint(0, GRID_SIZE-1)
            y = random.randint(0, GRID_SIZE-1)
            if not self.mines[x][y]:
                self.mines[x][y] = True
                placed += 1

    

if __name__ == "__main__":
    game = Minesweeper()
