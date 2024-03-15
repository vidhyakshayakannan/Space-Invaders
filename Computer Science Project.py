import pygame
import random
import math
from pygame import mixer

pygame.init()

# Creating the game window:

screen = pygame.display.set_mode((800, 600))

# Background

background = pygame.image.load("background.png")

# Background Music

mixer.music.load("background.wav")
mixer.music.play(-1)  # Plays continuously

# Title and Icon:

pygame.display.set_caption("Space Invaders: Computer Science Project by Vidhyakshaya, Keerthana and Rishab")
icon = pygame.image.load("BVM.jpeg")
pygame.display.set_icon(icon)

# Player:

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
X_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy:

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6  # We want six enemies
for i in range(num_enemies):
    enemyImg.append(pygame.imgage.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet:

# Ready state: You can't see the bullet on the screen
# Fire: The bullet is currently moving

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score:

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Displaying Game Over
gameoverfont = pygame.font.Font("freesansbold.ttf", 64)


def display_gameover(x, y):
    gameovertext = gameoverfont.render("GAME OVER ", True, (255, 255, 255))
    screen.blit(gameovertext, (200, 250))


def display_score(x, y):
    scorevalue = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(scorevalue, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # This is for the bullet to appear at the centre of the screen.


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(((enemyX - bulletX) ** 2) + ((enemyY - bulletY) ** 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop:

running = True
while running:

    # Backgorund Colour

    screen.fill((0, 0, 0))

    # Background Image

    background = pygame.image.load("background.png")
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check whether it is right or left

        if event.type == pygame.KEYDOWN:
            # A keystroke is pressed

            if event.key == pygame.K_LEFT:
                # Left key has been pressed
                X_change = - 5

            if event.key == pygame.K_RIGHT:
                # Right key has been pressed
                X_change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":  # Can't fire bullet when it's already in the fire state, if it's fired the bullet will move along with the spaceship
                    bulletsound = mixer.Sound("laser.wav")
                    bulletsound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                X_change = 0

    # Player Movement

    playerX = playerX + X_change

    # Adding Boundaries (Ensures that the spaceship stays within the game window's boundary)

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    enemyX = enemyX + enemyX_change

    # Enemy Movement:

    for i in range(num_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_enemies):
                enemyY[j] = 2000
            gameover()
            break
    if enemyX[i] <= 0:
        enemyX_change[i] = 4
        enemyY[i] = enemyY[i] + enemyY_change[i]
    elif enemyX[i] >= 736:
        enemyX_change[i] = -4
        enemyY[i] = enemyY[i] + enemyY_change[i]

# Bullet Movement:

if bulletY <= 0:  # We want the bullet to be reset to its original position
    bulletY = 480
    bullet_state = "ready"  # We want the bullet to be fired again

if bullet_state == "fire":
    fire_bullet(bulletX, bulletY)
    bulletY = bulletY - bulletY_change

# Collision:

collision = isCollision(enemyX, enemyY, bulletX, bulletY)
if collision:
    explosionsound = mixer.Sound("explosion.wav")
    explosionsound.play()
    bulletY = 480
    bullet_state = "ready"
    score = score + 1
    enemyX = random.randint(0, 736)
    enemyY = random.randint(50, 150)  # New position for enemy after collision

player(playerX, playerY)
enemy(enemyX, enemyY)
display_score(textX, textY)
pygame.display.update()


