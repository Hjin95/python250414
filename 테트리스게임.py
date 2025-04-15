import pygame
import random

# 초기화
pygame.init()

# 화면 크기
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (255, 0, 0),    # 빨강
    (0, 255, 0),    # 초록
    (0, 0, 255),    # 파랑
    (255, 255, 0),  # 노랑
    (0, 255, 255),  # 청록
    (255, 0, 255),  # 자홍
]

# 테트로미노 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

# 게임 보드 크기
BOARD_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# 게임 보드 초기화
board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]


class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(COLORS)
        self.x = BOARD_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]


def draw_board():
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x]:
                pygame.draw.rect(screen, board[y][x],
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def draw_tetromino(tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, tetromino.color,
                                 ((tetromino.x + x) * BLOCK_SIZE, (tetromino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def check_collision(tetromino, dx=0, dy=0):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = tetromino.x + x + dx
                new_y = tetromino.y + y + dy
                if new_x < 0 or new_x >= BOARD_WIDTH or new_y >= BOARD_HEIGHT:
                    return True
                if new_y >= 0 and board[new_y][new_x]:
                    return True
    return False


def merge_tetromino(tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                board[tetromino.y + y][tetromino.x + x] = tetromino.color


def clear_lines():
    global board
    board = [row for row in board if any(cell == 0 for cell in row)]
    while len(board) < BOARD_HEIGHT:
        board.insert(0, [0] * BOARD_WIDTH)


def main():
    clock = pygame.time.Clock()
    running = True
    current_tetromino = Tetromino(random.choice(SHAPES))
    fall_time = 0

    while running:
        screen.fill(BLACK)
        draw_board()
        draw_tetromino(current_tetromino)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(current_tetromino, dx=-1):
                    current_tetromino.x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(current_tetromino, dx=1):
                    current_tetromino.x += 1
                elif event.key == pygame.K_DOWN and not check_collision(current_tetromino, dy=1):
                    current_tetromino.y += 1
                elif event.key == pygame.K_UP:
                    current_tetromino.rotate()
                    if check_collision(current_tetromino):
                        current_tetromino.rotate()
                        current_tetromino.rotate()
                        current_tetromino.rotate()

        fall_time += clock.get_rawtime()
        clock.tick(30)

        if fall_time > 500:
            if not check_collision(current_tetromino, dy=1):
                current_tetromino.y += 1
            else:
                merge_tetromino(current_tetromino)
                clear_lines()
                current_tetromino = Tetromino(random.choice(SHAPES))
                if check_collision(current_tetromino):
                    running = False  # 게임 오버
            fall_time = 0

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()