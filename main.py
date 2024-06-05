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
        self.flags = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]  # 깃발 상태 저장 배열


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

    # 게임 보드 그리기 함수
    def draw_board(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(x * (SCREEN_WIDTH // GRID_SIZE), y * (SCREEN_HEIGHT // GRID_SIZE), 
                                   SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE)
                if self.grid[x][y] == 1:  # 칸이 열렸다면
                    pygame.draw.rect(self.screen, (255, 255, 255), rect)  # 백색으로 칸 채우기
                    if self.adjacent[x][y] > 0:  # 인접 지뢰 수가 있다면 숫자 표시
                        label = self.font.render(str(self.adjacent[x][y]), True, (0, 0, 0))
                        self.screen.blit(label, (rect.x + 10, rect.y + 10))
                else:  # 칸이 닫혀 있으면
                    pygame.draw.rect(self.screen, (160, 160, 160), rect)  # 회색으로 칸 채우기
                    if self.flags[x][y]:  # 깃발이 있다면 깃발 표시
                        pygame.draw.circle(self.screen, (255, 0, 0), (rect.x + rect.width // 2, rect.y + rect.height // 2), 10)
                        
    # 게임 실행 함수 업데이트
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.handle_mouse_input(event)  # 마우스 이벤트 처리
            
            self.screen.fill((0, 0, 0))  # 화면을 검은색으로 초기화
            self.draw_board()  # 게임 보드 그리기
            pygame.display.flip()  # 변경된 내용 화면에 업데이트

if __name__ == "__main__":
    game = Minesweeper()
