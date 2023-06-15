import pygame
import random

# 初始化 pygame
pygame.init()

# 游戏区域大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

# 食物大小
FOOD_WIDTH = 20
FOOD_HEIGHT = 20

# 蛇身大小
SNAKE_WIDTH = 20
SNAKE_HEIGHT = 20

# 颜色定义
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# 创建窗口并设置标题
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# 创建时钟并设置初始速度
clock = pygame.time.Clock()
speed = 5

# 初始化蛇
snake_head = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
snake_body = [[snake_head[0], snake_head[1] + i * SNAKE_HEIGHT] for i in range(3)]
snake_direction = 'u'

# 初始化食物
food_pos = [random.randint(0, SCREEN_WIDTH - FOOD_WIDTH), random.randint(0, SCREEN_HEIGHT - FOOD_HEIGHT)]

# 游戏循环标志
running = True

# 游戏结束标志
game_over = False

# 游戏主循环
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'd':
                snake_direction = 'u'
            elif event.key == pygame.K_DOWN and snake_direction != 'u':
                snake_direction = 'd'
            elif event.key == pygame.K_LEFT and snake_direction != 'r':
                snake_direction = 'l'
            elif event.key == pygame.K_RIGHT and snake_direction != 'l':
                snake_direction = 'r'

    # 移动蛇头
    if snake_direction == 'u':
        snake_head[1] -= SNAKE_HEIGHT
    elif snake_direction == 'd':
        snake_head[1] += SNAKE_HEIGHT
    elif snake_direction == 'l':
        snake_head[0] -= SNAKE_WIDTH
    elif snake_direction == 'r':
        snake_head[0] += SNAKE_WIDTH

    # 判断吃到食物
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        food_pos = [random.randint(0, SCREEN_WIDTH - FOOD_WIDTH), random.randint(0, SCREEN_HEIGHT - FOOD_HEIGHT)]
        snake_body.append(snake_body[-1])

    # 移动蛇身
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i] = snake_body[i - 1]
    snake_body[0] = snake_head[:]

    # 判断撞墙或自撞
    if snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT:
        game_over = True
    for i in range(1, len(snake_body)):
        if snake_head[0] == snake_body[i][0] and snake_head[1] == snake_body[i][1]:
            game_over = True

    # 清屏
    screen.fill(GRAY)

    # 绘制食物
    pygame.draw.rect(screen, GREEN, (food_pos[0], food_pos[1], FOOD_WIDTH, FOOD_HEIGHT))

    # 绘制蛇身
    for pos in snake_body:
        pygame.draw.rect(screen, BLUE, (pos[0], pos[1], SNAKE_WIDTH, SNAKE_HEIGHT))

    # 刷新屏幕
    pygame.display.update()

    # 控制帧率和速度
    clock.tick(30)
    if not game_over:
        speed += 0.1
        clock.tick(speed)

# 游戏结束
font = pygame.font.SysFont("arial", 36)
text = font.render("Game Over!", True, RED)
text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
screen.blit(text, text_rect)
pygame.display.update()

# 等待退出
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:exec('exit()')
        pygame.quit()
        quit()