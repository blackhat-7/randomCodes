import pygame
import os

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
SPACESHIP_DIMS = (55, 40)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SPACESHIP_DIMS), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, SPACESHIP_DIMS), -90)
MID_BORDER = pygame.Rect(WIDTH/2 - 10, 0, 10, HEIGHT)


class Bullet:
    def __init__(self, x, y, width, height, player):
        self.bullet = pygame.Rect(x, y, width, height)
        self.player = player
        if player.side == 'left':
            self.SPEED = 7
        else:
            self.SPEED = -7

    def update_pos(self):
        self.x += self.SPEED


class Player:
    SPEED = 5
    MAX_BULLETS = 3

    def __init__(self, name, side, x, y, dims, image):
        self.name = name
        self.side = side
        self.image = image
        self.player = pygame.Rect(x, y, *dims)
        self.bullets = []
        self.draw()

    def draw(self):
        WIN.blit(self.image, (self.player.x, self.player.y))

    def move(self, keys_pressed):
        if self.side == 'left':
            if keys_pressed[pygame.K_a] and self.player.x - Player.SPEED > 0:
                self.player.x -= Player.SPEED
            if keys_pressed[pygame.K_d] and self.player.x + self.player.width + Player.SPEED < MID_BORDER.x:
                self.player.x += Player.SPEED
            if keys_pressed[pygame.K_w] and self.player.y - Player.SPEED > 0:
                self.player.y -= Player.SPEED
            if keys_pressed[pygame.K_s] and self.player.y + self.player.height + Player.SPEED < HEIGHT:
                self.player.y += Player.SPEED

        else:
            if keys_pressed[pygame.K_LEFT] and self.player.x - Player.SPEED > MID_BORDER.x + MID_BORDER.width:
                self.player.x -= Player.SPEED
            if keys_pressed[pygame.K_RIGHT] and self.player.x + self.player.width + Player.SPEED < WIDTH:
                self.player.x += Player.SPEED
            if keys_pressed[pygame.K_UP] and self.player.y - Player.SPEED > 0:
                self.player.y -= Player.SPEED
            if keys_pressed[pygame.K_DOWN] and self.player.y + self.player.height + Player.SPEED < HEIGHT:
                self.player.y += Player.SPEED

    def shoot(self):
        if len(self.bullets) < Player.MAX_BULLETS:
            if self.side == 'left':
                bullet = Bullet(self.player.x + self.player.width, self.player.y + self.player.height/2 - 2, 10, 5, self)
            else:
                bullet = Bullet(self.player.x - 10, self.player.y + self.player.height/2 - 2, 10, 5, self)
            self.bullets.append(bullet)
        print(len(self.bullets))


def draw_window(yellow, red):
    WIN.fill(WHITE)
    yellow.draw()
    red.draw()
    pygame.draw.rect(WIN, BLACK, MID_BORDER)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    yellow = Player('yellow', 'left', WIDTH/4, HEIGHT/2, SPACESHIP_DIMS[::-1], YELLOW_SPACESHIP)
    red = Player('red', 'right', WIDTH/2 + WIDTH/4, HEIGHT/2, SPACESHIP_DIMS[::-1], RED_SPACESHIP)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    yellow.shoot()
                if event.key == pygame.K_RALT:
                    red.shoot()

        keys_pressed = pygame.key.get_pressed()
        yellow.move(keys_pressed)
        red.move(keys_pressed)
        draw_window(yellow, red)

    pygame.quit()


if __name__ == '__main__':
    main()
