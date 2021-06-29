import os
import pygame
import random
from pygame import mixer

pygame.init()

width = 700
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Punk hazard')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# score
score_value = 0
miss = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
textY = 10

intro_font = pygame.font.Font('introfont.ttf', 50)
intro_textfont = pygame.font.Font('introfont.ttf', 20)

winlose_font = pygame.font.Font('winlose.ttf', 50)

dev_font = pygame.font.Font('introfont.ttf', 20)


def press_key(x, y):
    key = font.render("Click to play", 1, (255, 255, 255))
    screen.blit(key, (x, y))


def developed_by(x, y):
    dev = dev_font.render("-Developed by Faizan Hanief-", 1, (255, 0, 0))
    screen.blit(dev, (x, y))


def you_lose(x, y):
    lose_label = winlose_font.render("YOU LOSE :( ", True, (255, 255, 255))
    screen.blit(lose_label, (x, y))


def you_win(x, y):
    win_label = winlose_font.render("YOU WIN ", True, (255, 255, 255))
    screen.blit(win_label, (x, y))


def show_score(x, y):
    score = font.render('Score :' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def intro_text(x, y):
    intro_text = intro_textfont.render("A Space shooter Game.", 1, (255, 255, 255))
    screen.blit(intro_text, (x, y))


def intro_title(x, y):
    title = intro_font.render("Punk Hazard", 1, (255, 0, 0))
    screen.blit(title, (x, y))


running = True

background = pygame.image.load('bg.jpg')
# background music
mixer.music.load('bgmusic.mp3')
mixer.music.play(-1)


# creating the player
class PLayer:
    def __init__(self, x, y, ):  # used for constructor to construct an object
        self.x = x
        self.y = y

    def draw(self):
        playerImg = pygame.image.load('spaceship.png')
        screen.blit(playerImg, (self.x, self.y))

    def detectcollision(self):
        for laser in lasers2:
            if (laser.x > self.x and laser.x < self.x + 64 and laser.y > self.y and laser.y < self.y + 64):
                lasers.remove(laser)
                player.remove(self)
                explosion_sound = mixer.Sound('boom.wav')
                explosion_sound.play()



# enemy
class Enemy:
    def __init__(self, x, y):  # used for constructor to construct an object
        self.x = x
        self.y = y

    def draw(self):
        enemyImg = pygame.image.load('enemy.png')
        screen.blit(enemyImg, (self.x, self.y))
        self.y += 0.5

    def detectcollision(self):
        for laser in lasers:
            if (laser.x > self.x and laser.x < self.x + 64 and laser.y > self.y and laser.y < self.y + 64):
                lasers.remove(laser)
                enemies.remove(self)
                explosion_sound = mixer.Sound('boom.wav')
                explosion_sound.play()
                global score_value
                score_value += 1


# enemy2
class Enemy2:
    def __init__(self, x, y):  # used for constructor to construct an object
        self.x = x
        self.y = y

    def draw(self):

        enemy2Img = pygame.image.load('enemy2.png')
        screen.blit(enemy2Img, (self.x, self.y))
        self.y += 0.9

    def detectcollision(self):
        for laser in lasers:
            if (laser.x > self.x and laser.x < self.x + 150 and laser.y > self.y and laser.y < self.y + 150):
                lasers.remove(laser)
                enemies.remove(self)
                explosion_sound = mixer.Sound('boom.wav')
                explosion_sound.play()

                global score_value
                score_value += 1


# laser
class Laser:
    def __init__(self, x, y):  # used for constructor to construct an object
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (254, 71, 110), pygame.Rect(self.x, self.y, 4, 6))
        self.y -= 6


class Laser2:
    def __init__(self, x, y):  # used for constructor to construct an object
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (254, 71, 110), pygame.Rect(self.x, self.y, 4, 6))
        self.y += 0.5


def displayText(text):
    font = pygame.font.SysFont('calibri', 50)
    message = font.render(text, False, (255, 255, 255))
    screen.blit(message, (220, 160))


player = PLayer(width / 2, height - 70)
enemies = []
lasers = []
lasers2 = []

for x in range(2, 6):
    for y in range(3, 9):
        enemy = Enemy(random.randrange(50, width - 100), random.randrange(-3000, -200))
        enemies.append(enemy)
    for i in range(2, 7):
        for j in range(2, 9):
            enemy = Enemy2(random.randrange(50, width - 100), random.randrange(-1500, -100))
        enemies.append(enemy)

fps = 60
clock = pygame.time.Clock()
lost = False


def main():
    fps = 60
    clock = pygame.time.Clock()
    lost = False
    running = True

    while running:

        screen.blit(background, (0, 0))
        player.draw()

        for enemy in enemies:
            enemy.draw()

            enemy.detectcollision()
            if enemy.y > height:
                enemy.y = 2000
                for enemy in enemies:
                    enemy.y = 2000
                player.y = 2000
                player.x = 2000
                you_lose(110, 100)

        for laser in lasers:
            laser.draw()
        for laser in lasers2:
            laser.draw()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            if player.x > 0:
                player.x -= 2

        if pressed[pygame.K_RIGHT]:
            if player.x < width - 62:
                player.x += 2
        if pressed[pygame.K_UP]:
            if player.y > 0:
                player.y -= 2
        if pressed[pygame.K_DOWN]:
            if player.y <= height - 63:
                player.y += 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                lasers.append(Laser(player.x + 30, player.y))
                laser_sound = mixer.Sound('fire.mp3')
                laser_sound.play()

        if len(enemies) <= 0:
            player.y = 2000
            player.x = 2000
            you_win(180, 100)

        show_score(textX, textY)
        pygame.display.update()


def menu():
    run = True
    while run:

        screen.blit(background, (0, 0))
        screen.blit(icon, (100, 30))
        press_key(10, 10)
        intro_title(150, 110)
        intro_text(327, 300)
        developed_by(280, 550)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                main()


menu()
