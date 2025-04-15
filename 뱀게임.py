import pygame
import random
import time

# pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("뱀 게임")

# 시계 객체 생성
clock = pygame.time.Clock()

# 폰트 설정
font = pygame.font.SysFont("comicsansms", 35)

# 점수 표시 함수
def show_score(score):
    value = font.render(f"점수: {score}", True, WHITE)
    screen.blit(value, [10, 10])

# 게임 종료 메시지
def game_over_message():
    message = font.render("게임 오버!", True, RED)
    screen.blit(message, [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20])
    pygame.display.flip()
    time.sleep(2)

# 메인 게임 루프
def main():
    # 뱀 초기 설정
    snake_pos = [100, 50]  # 뱀의 머리 위치
    snake_body = [[100, 50], [90, 50], [80, 50]]  # 뱀의 몸
    direction = "RIGHT"  # 초기 이동 방향
    change_to = direction
    score = 0

    # 음식 초기 위치
    food_pos = [random.randrange(1, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                random.randrange(1, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
    food_spawn = True

    running = True
    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        # 방향 변경
        direction = change_to

        # 뱀의 머리 이동
        if direction == "UP":
            snake_pos[1] -= BLOCK_SIZE
        elif direction == "DOWN":
            snake_pos[1] += BLOCK_SIZE
        elif direction == "LEFT":
            snake_pos[0] -= BLOCK_SIZE
        elif direction == "RIGHT":
            snake_pos[0] += BLOCK_SIZE

        # 뱀의 몸 업데이트
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:  # 좌표 비교를 명확히 수정
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # 음식 생성
        if not food_spawn:
            food_pos = [random.randrange(1, SCREEN_WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                        random.randrange(1, SCREEN_HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
        food_spawn = True

        # 화면 그리기
        screen.fill(BLACK)
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # 점수 표시
        show_score(score)

        # 게임 종료 조건
        if (snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH or
                snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT):
            game_over_message()
            running = False

        for block in snake_body[1:]:
            if snake_pos == block:
                game_over_message()
                running = False

        # 화면 업데이트
        pygame.display.flip()

        # 게임 속도 조절
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()