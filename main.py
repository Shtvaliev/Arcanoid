# Pygame шаблон - скелет для нового проекта Pygame
import pygame

WIDTH = 700
HEIGHT = 700
FPS = 60
start_x = 600
start_y = 500

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (10, 186, 181)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0 :
            self.rect.left = WIDTH


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.rect.x = player.rect.x + 49
        # self.rect.y = player.rect.y - 10
        # self.rect.x = 360
        # self.rect.y = 360

    x = 1
    y = 1

    def update(self):
        global speed
        if 'if_active' not in globals():
            global if_active
            if_active = 0
        if 'x' not in globals():
            global x
            global y
            speed = 0
            x = speed
            y = speed
        keystat = pygame.key.get_pressed()
        if keystat[pygame.K_UP] and if_active == 0:
            speed = 2
            x = speed
            y = -speed
            if_active = 1
        if keystat[pygame.K_DOWN]:
            if_active = 0
            self.rect.x = player.rect.x + 49
            self.rect.y = player.rect.y - 10
            # self.rect.x = start_x
            # self.rect.y = start_y
        if self.rect.x > WIDTH - 2:
            x = -speed
        if self.rect.x < 2 :
            x = speed
        if self.rect.y > HEIGHT - 2:
            speed = 0
            if_active = 0
            x = 0
            y = 0
        if if_active == 0:
            self.rect.x = player.rect.x + 49
            self.rect.y = player.rect.y - 10
            # self.rect.x = start_x
            # self.rect.y = start_y
        if self.rect.y < 2:
            y = speed
        if pygame.sprite.spritecollideany(player, ball_sprite):
            y = -speed
        if pygame.sprite.spritecollide(ball, block_sprite, True):
            a = abs(ball.rect.bottom - blocks[self.rect.x // 42][self.rect.y // 40].rect.top) % 40
            b = abs(ball.rect.left - blocks[self.rect.x // 42][self.rect.y // 40].rect.right) % 42
            c = abs(ball.rect.right - blocks[self.rect.x // 42][self.rect.y // 40].rect.left) % 42
            d = abs(ball.rect.top - blocks[self.rect.x // 42][self.rect.y // 40].rect.bottom) % 40
            m = min(a, b, c, d)
            if not(a == 1 and b == 1) and not(a == 1 and c == 1) and not(d == 1 and b == 1) and not(d == 1 and c == 1):
                if m == a or m == d:
                    y = -y
                elif m == b or m == c:
                    x = -x

        self.rect.x += x
        self.rect.y += y


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Acranoid")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ball_sprite = pygame.sprite.Group()
block_sprite = pygame.sprite.Group()
player = Player()
ball = Ball()
all_sprites.add(player)
all_sprites.add(ball)
ball_sprite.add(ball)

blocks = [[Block() for j in range(10)] for i in range(17)]
for i in range(17):
    for j in range(10):
        # blocks[i][j] = Block()
        blocks[i][j].rect.x = 42*i
        blocks[i][j].rect.y = 40*j
        all_sprites.add(blocks[i][j])
        block_sprite.add(blocks[i][j])

# block = Block()
# block.rect.x = 350
# block.rect.y = 350
# all_sprites.add(block)
# block_sprite.add(block)

# Цикл игры
running = True
while running :
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # if pygame.sprite.spritecollideany(player, ball_sprite):
    #     y = -2

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
