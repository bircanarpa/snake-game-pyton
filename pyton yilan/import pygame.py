import pygame
import random

# Ekran boyutu
WIDTH = 800
HEIGHT = 600

# Renkler
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Yılanın başlangıç boyutu ve hızı
SNAKE_SIZE = 20
SNAKE_SPEED = 10

# Pygame başlatma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Yılanın ve yiyeceğin başlangıç konumu
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_dx = SNAKE_SPEED
snake_dy = 0

food_x = random.randint(0, WIDTH - SNAKE_SIZE)
food_y = random.randint(0, HEIGHT - SNAKE_SIZE)

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Yılanın hareketini kontrol etmek için klavye girişlerini dinle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SPEED
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SPEED
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dy = -SNAKE_SPEED
                snake_dx = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = SNAKE_SPEED
                snake_dx = 0

    # Yılanın yeni konumunu güncelle
    snake_x += snake_dx
    snake_y += snake_dy

    # Yılanın ekran dışına çıkmamasını sağla
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        running = False

    # Yılanın yiyeceği yemesini kontrol et
    if snake_x == food_x and snake_y == food_y:
        # Yeni bir yiyecek yerleştir
        food_x = random.randint(0, WIDTH - SNAKE_SIZE)
        food_y = random.randint(0, HEIGHT - SNAKE_SIZE)

    # Ekranı temizle
    screen.fill(BLACK)

    # Yılanı çiz
    pygame.draw.rect(screen, GREEN, (snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE))

    # Yiyeceği çiz
    pygame.draw.rect(screen, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarla
    clock.tick(30)

# Pygame'i kapat
pygame.quit()