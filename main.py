import pygame
import random

# 게임 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
MINE_COUNT = 40    # 지뢰 총 개수

class Minesweeper:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
        
    # 주어진 위치 주변의 지뢰 수를 증가시키는 함수
    def increment_adjacent(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    self.adjacent[nx][ny] += 1
                    
    # 지뢰를 게임 보드에 무작위로 배치하는 함수
    def place_mines(self):
        placed = 0
        while placed < MINE_COUNT:
            x = random.randint(0, GRID_SIZE-1)
            y = random.randint(0, GRID_SIZE-1)
            if not self.mines[x][y]:
                self.mines[x][y] = True
                self.increment_adjacent(x, y)    # 인접 지뢰 수 업데이트 호출
                placed += 1

    # 마우스 입력 처리 함수
    def handle_mouse_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos[0] // (SCREEN_WIDTH // GRID_SIZE), event.pos[1] // (SCREEN_HEIGHT // GRID_SIZE)
            if event.button == 1:  # 왼쪽 클릭
                self.open_cell(x, y)
            elif event.button == 3:  # 오른쪽 클릭
                self.toggle_flag(x, y)

    # 지정된 위치의 칸을 여는 함수
    def open_cell(self, x, y):
        if not self.flags[x][y]:  # 깃발이 없는 칸만 열기
            self.grid[x][y] = 1  # 칸 상태를 열림으로 변경
            if self.adjacent[x][y] == 0:
                self.open_adjacent_cells(x, y)  # 인접 칸 자동 열기

    # 깃발 상태를 토글하는 함수
    def toggle_flag(self, x, y):
        if not self.grid[x][y]:  # 칸이 닫혀 있는 경우만 깃발 상태 변경 가능
            self.flags[x][y] = not self.flags[x][y]

    # 지정된 위치의 인접 칸을 자동으로 여는 함수
    def open_adjacent_cells(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and not self.grid[nx][ny]:
                    self.open_cell(nx, ny)

if __name__ == "__main__":
    game = Minesweeper()
