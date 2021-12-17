import pygame


def make_blocks(Block, sprites):
    blocks = [[Block() for j in range(10)] for i in range(17)]
    for i in range(17):
        for j in range(10):
            blocks[i][j].rect.x = 42 * i
            blocks[i][j].rect.y = 40 * j
            sprites['all_sprites'].add(blocks[i][j])
            sprites['block_sprite'].add(blocks[i][j])
    return blocks


def update_player(self, param):
    self.speedx = 0
    keye = pygame.key.get_pressed()
    if keye[pygame.K_LEFT]:
        self.speedx = -8
    if keye[pygame.K_RIGHT]:
        self.speedx = 8
    self.rect.x += self.speedx
    if self.rect.left > param['width']:
        self.rect.right = 0
    if self.rect.right < 0:
        self.rect.left = param['width']
    return self


is_active = 0
speed = 3
x = 0
y = 0


def rebound_frames(i, j, x, y, speed, is_active, param):
    if i > param['width'] - 2:
        x = -speed
    if i < 2:
        x = speed
    if j < 2:
        y = speed
    if j > param['height'] - 2:
        is_active = 0
        x = 0
        y = 0
    return x, y, is_active, speed


def activate_check(is_active, i_player, j_player, i_ball, j_ball):
    if is_active == 0:
        i_ball = i_player + 49
        j_ball = j_player - 10
    return i_ball, j_ball


def activating(i_ball, j_ball, par1, par2, is_active, speed, x, y):
    if par1 and is_active == 0:
        x = speed
        y = -speed
        is_active = 1
    if par2:
        is_active = 0
        # i_ball = i_player + 49
        # j_ball = j_player - 10
    return x, y, is_active, i_ball, j_ball


def rebound_player(speed, local_param, y):
    if local_param:
        y = -speed
    return y


def rebound_block(ball_bottom, ball_left, ball_right, ball_top, block_top, block_right, block_left, block_bottom,
                  local_param, x, y):
    if local_param:
        a = abs(ball_bottom - block_top) % 40
        b = abs(ball_left - block_right) % 42
        c = abs(ball_right - block_left) % 42
        d = abs(ball_top - block_bottom) % 40
        m = min(a, b, c, d)
        if not (a == 1 and b == 1) and not (a == 1 and c == 1) and not (d == 1 and b == 1) and not (
                d == 1 and c == 1):
            if m == a or m == d:
                y = -y
            elif m == b or m == c:
                x = -x
    return x, y


def update_ball(self, player, param, sprites, blocks):
    global is_active
    global speed
    global x
    global y
    key = pygame.key.get_pressed()

    x, y, is_active, self.rect.x, self.rect.y = activating(self.rect.x, self.rect.y,
                                                           key[pygame.K_UP], key[pygame.K_DOWN], is_active, speed, x, y)
    x, y, is_active, speed = rebound_frames(self.rect.x, self.rect.y, x, y, speed, is_active, param)
    self.rect.x, self.rect.y = activate_check(is_active, player.rect.x, player.rect.y, self.rect.x, self.rect.y)
    y = rebound_player(speed, pygame.sprite.spritecollideany(player, sprites['ball_sprite']), y)
    if self.rect.x // 42 < 17 and self.rect.y // 40 < 10:
        x, y = rebound_block(self.rect.bottom, self.rect.left, self.rect.right, self.rect.top,
                             blocks[self.rect.x // 42][self.rect.y // 40].rect.top,
                             blocks[self.rect.x // 42][self.rect.y // 40].rect.right,
                             blocks[self.rect.x // 42][self.rect.y // 40].rect.left,
                             blocks[self.rect.x // 42][self.rect.y // 40].rect.bottom,
                             pygame.sprite.spritecollide(self, sprites['block_sprite'], True), x, y)

    self.rect.x += x
    self.rect.y += y


def classes(param, sprites):
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((100, 10))
            self.image.fill(param['green'])
            self.rect = self.image.get_rect()
            self.rect.center = (param['width'] / 2, param['height'] - 50)

        def update(self):
            update_player(self, param)
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

        def update(self):
            update_ball(self, player, param, sprites, blocks)
    ball = Ball()
    sprites['all_sprites'].add(ball)
    sprites['ball_sprite'].add(ball)

    return sprites


def main_parameters():
    global param
    param = {
        'width': 700,
        'height': 700,
        'FPS': 60,
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (10, 186, 181),
        'blue': (0, 0, 255),
        'speed': 3,
        'is_active': 0,
        'x': 0,
        'y': 0
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