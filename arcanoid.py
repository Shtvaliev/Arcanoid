import pygame


def make_blocks(Block, sprites):
    blocks = [[Block() for j in range(10)] for i in range(17)]
    for i in range(17):
        for j in range(10):
            # blocks[i][j] = Block()
            blocks[i][j].rect.x = 42 * i
            blocks[i][j].rect.y = 40 * j
            sprites['all_sprites'].add(blocks[i][j])
            sprites['block_sprite'].add(blocks[i][j])
    return blocks


def classes(param, sprites):
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((100, 10))
            self.image.fill(param['green'])
            self.rect = self.image.get_rect()
            self.rect.center = (param['width'] / 2, param['height'] - 50)

        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            self.rect.x += self.speedx
            if self.rect.left > param['width']:
                self.rect.right = 0
            if self.rect.right < 0:
                self.rect.left = param['width']
    player = Player()
    sprites['all_sprites'].add(player)

    class Block(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((30, 30))
            self.image.fill(param['green'])
            self.rect = self.image.get_rect()
            self.rect.center = (param['width'] / 2, param['height'] / 2)
    blocks = make_blocks(Block, sprites)
    sprites['all_sprites'].add(blocks)
    sprites['block_sprite'].add(blocks)

    class Ball(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((5, 5))
            self.image.fill(param['green'])
            self.rect = self.image.get_rect()
            self.rect.center = (param['width'] / 2, param['height'] / 2)
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
            if self.rect.x > param['width'] - 2:
                x = -speed
            if self.rect.x < 2:
                x = speed
            if self.rect.y > param['height'] - 2:
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
            if pygame.sprite.spritecollideany(player, sprites['ball_sprite']):
                y = -speed
            if pygame.sprite.spritecollide(ball, sprites['block_sprite'], True):
                a = abs(ball.rect.bottom - blocks[self.rect.x // 42][self.rect.y // 40].rect.top) % 40
                b = abs(ball.rect.left - blocks[self.rect.x // 42][self.rect.y // 40].rect.right) % 42
                c = abs(ball.rect.right - blocks[self.rect.x // 42][self.rect.y // 40].rect.left) % 42
                d = abs(ball.rect.top - blocks[self.rect.x // 42][self.rect.y // 40].rect.bottom) % 40
                m = min(a, b, c, d)
                if not (a == 1 and b == 1) and not (a == 1 and c == 1) and not (d == 1 and b == 1) and not (
                        d == 1 and c == 1):
                    if m == a or m == d:
                        y = -y
                    elif m == b or m == c:
                        x = -x

            self.rect.x += x
            self.rect.y += y
            
    ball = Ball()
    sprites['all_sprites'].add(ball)
    sprites['ball_sprite'].add(ball)

    return sprites


def main_parameters():
    param = {
        'width': 700,
        'height': 700,
        'FPS': 60,
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (10, 186, 181),
        'blue': (0, 0, 255)
    }
    return param


def make_sprites():
    sprites = {
        'all_sprites': pygame.sprite.Group(),
        'ball_sprite': pygame.sprite.Group(),
        'block_sprite': pygame.sprite.Group()
    }
    return sprites


def main():
    param = main_parameters()
    # all_sprites = make_sprites()
    sprites = classes(param, make_sprites())
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((param['width'], param['height']))
    pygame.display.set_caption("Acranoid")
    clock = pygame.time.Clock()

    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(param['FPS'])
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # if pygame.sprite.spritecollideany(player, ball_sprite):
        #     y = -2

        # Обновление
        sprites['all_sprites'].update()

        # Рендеринг
        screen.fill(param['black'])
        sprites['all_sprites'].draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()

    return 


if __name__ == "__main__":
    main()