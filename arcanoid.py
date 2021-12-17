# -*- coding: utf-8 -*-
import pygame


def make_blocks(block):
    """Making blocks

    Makes matrix of blocks and adds it to all and block sprites groups
    :param block: block sprite
    :return: objects of block sprite
    """
    blocks = [[block() for j in range(10)] for i in range(17)]
    for i in range(17):
        for j in range(10):
            blocks[i][j].rect.x = 42 * i
            blocks[i][j].rect.y = 40 * j
    print(type(blocks))
    print(blocks)
    return blocks


def update_player(self, default_parameters):
    """Updating player's platform location

    :param self: player sprite
    :param default_parameters: parameters of game configuration
    """
    self.speedx = 0
    keye = pygame.key.get_pressed()
    if keye[pygame.K_LEFT]:
        self.speedx = -8
    if keye[pygame.K_RIGHT]:
        self.speedx = 8
    self.rect.x += self.speedx
    if self.rect.left > default_parameters['width']:
        self.rect.right = 0
    if self.rect.right < 0:
        self.rect.left = default_parameters['width']


def rebound_frames(i, j, x, y, speed, is_active, default_parameters):
    """Rebound from frames rules

    Changes direction of movement of the ball if it touches one of the frames and stop the game
    if ball touched bottom frame
    :param i: Ox ball coordinate
    :param j: Oy ball coordinate
    :param x: Ox axis speed of the ball
    :param y: Oy axis speed of the ball
    :param speed: default speed of ball
    :param is_active: says if the game has to be continued
    :param default_parameters: parameters of game configuration
    :return: new Ox and Oy axis speed and answer if the game has to be continued
    """
    if i > default_parameters['width'] - 2:
        x = -speed
    if i < 2:
        x = speed
    if j < 2:
        y = speed
    if j > default_parameters['height'] - 2:
        is_active = 0
        x = 0
        y = 0
    return x, y, is_active


def activate_check(is_active, i_player, j_player, i_ball, j_ball):
    """Activated check

    Checks if the game has to be continued and return ball to the player's platform if not
    :param is_active: says if the game has to be continued
    :param i_player: Ox player's platform coordinate
    :param j_player: Oy player's platform coordinate
    :param i_ball: Ox ball coordinate
    :param j_ball: Oy ball coordinate
    :return: new Ox and Oy coordinates for the ball
    """
    if is_active == 0:
        i_ball = i_player + 49
        j_ball = j_player - 10
    return i_ball, j_ball


def activating(par1, par2, is_active, speed, x, y):
    """Game activating

    Activate game or stop it after pressing buttons of start and stop
    :param par1: is start button was pressed
    :param par2: is stop button was pressed
    :param is_active: says if the game has to be continued
    :param speed: default speed of ball
    :param x: Ox axis speed of the ball
    :param y: Oy axis speed of the ball
    :return: Ox and Oy axis speed of the ball and answer if the game has to be continued
    """
    if par1 and is_active == 0:
        x = speed
        y = -speed
        is_active = 1
    if par2:
        is_active = 0
    return x, y, is_active


def rebound_player(speed, local_parameter, y):
    """Rebound from player's platform rules

    Changes direction of movement of the ball if it touches the player's platform
    :param speed: default speed of ball
    :param local_parameter: is ball touched the platform
    :param y: Oy axis speed of the ball
    :return: new Oy axis speed of the ball
    """
    if local_parameter:
        y = -speed
    return y


def rebound_block(ball_bottom, ball_left, ball_right, ball_top, block_top, block_right, block_left, block_bottom,
                  local_parameter, x, y):
    """Rebound from blocks rules

    Changes direction of movement of the ball if it touches a block and delete the block
    :param ball_bottom: coordinates of the bottom of the ball
    :param ball_left: coordinates of the left edge of the ball
    :param ball_right: coordinates of thr right edge of the ball
    :param ball_top: coordinates of the top of the ball
    :param block_top: coordinates of the top of the block
    :param block_right: coordinates of the right edge of the block
    :param block_left: coordinates of the left edge of the block
    :param block_bottom: coordinates of the bottom of the bloock
    :param local_parameter: is ball touched a block
    :param x: Ox axis speed of the ball
    :param y: Oy axis speed of the ball
    :return: new Ox and Oy axis speed for the ball
    """
    if local_parameter:
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


def update_ball(self, player, default_parameters, sprites, blocks):
    """Updating ball location

    Contains rules of ball movement
    :param self: ball sprite
    :param player: player sprite
    :param default_parameters: parameters of game configuration
    :param sprites: groups of sprites
    :param blocks: list of blocks sprites
    """
    global is_active
    global speed
    global x
    global y
    key = pygame.key.get_pressed()

    x, y, is_active= activating(key[pygame.K_UP], key[pygame.K_DOWN], is_active, speed, x, y)
    x, y, is_active = rebound_frames(self.rect.x, self.rect.y, x, y, speed, is_active, default_parameters)
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


def classes(default_parameters, sprites):
    """Makes game objects

    Makes sprites attending the game
    :param default_parameters: parameters of game configuration
    :param sprites: groups of sprites
    :return: groups of sprites with added object in it
    """
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((100, 10))
            self.image.fill(default_parameters['green'])
            self.rect = self.image.get_rect()
            self.rect.center = (default_parameters['width'] / 2, default_parameters['height'] - 50)

        def update(self):
            update_player(self, default_parameters)
    player = Player()
    sprites['all_sprites'].add(player)

    class Block(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((30, 30))
            self.image.fill(default_parameters['green'])
            self.rect = self.image.get_rect()
            self.rect.center = (default_parameters['width'] / 2, default_parameters['height'] / 2)
    blocks = make_blocks(Block)
    sprites['all_sprites'].add(blocks)
    sprites['block_sprite'].add(blocks)

    class Ball(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((5, 5))
            self.image.fill(default_parameters['green'])
            self.rect = self.image.get_rect()
            self.rect.center = (default_parameters['width'] / 2, default_parameters['height'] / 2)

        def update(self):
            update_ball(self, player, default_parameters, sprites, blocks)
    ball = Ball()
    sprites['all_sprites'].add(ball)
    sprites['ball_sprite'].add(ball)

    return sprites


def main_parameters():
    """Set parameters

    Contains parameters of game configuration
    :return: parameters of game configuration
    """
    global default_parameters
    global speed
    global is_active
    global x
    global y
    default_parameters = {
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
    speed = default_parameters['speed']
    is_active = default_parameters['is_active']
    x = default_parameters['x']
    y = default_parameters['y']
    return default_parameters


def make_sprites():
    """Sprites making

    Makes all used groups of sprites
    :return: groups of sprites
    """
    sprites = {
        'all_sprites': pygame.sprite.Group(),
        'ball_sprite': pygame.sprite.Group(),
        'block_sprite': pygame.sprite.Group()
    }
    return sprites


def main():
    """Run function"""
    default_parameters = main_parameters()
    sprites = classes(default_parameters, make_sprites())
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((default_parameters['width'], default_parameters['height']))
    pygame.display.set_caption("Acranoid")
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(default_parameters['FPS'])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sprites['all_sprites'].update()

        screen.fill(default_parameters['black'])
        sprites['all_sprites'].draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
