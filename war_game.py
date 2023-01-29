#War game
#Use arrow for movement and spcae

#imports
import math
import random
import pygame

#initialize
pygame.font.init()
pygame.init()


# Display
dis = pygame.display.set_mode((800, 600))

# bg
bg = pygame.image.load('BG.png')

# Display
pygame.display.set_caption("World War")
icon = pygame.image.load('army.png')
pygame.display.set_icon(icon)

# Mili_Hero 
MilImg = pygame.image.load('army.png')
MilX = 370
MilY = 500
MilXChange = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numOfEnymy = 5

for i in range(numOfEnymy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# fireBullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bulletPos = "ready"

#fonts
font = pygame.font.SysFont('comicsans', 32)
dead_font = pygame.font.SysFont('comicsans', 64)

# Point line
point = 0
textX = 10
testY = 10

def showScore(x, y):
    score = font.render("Score : " + str(point), True, (121, 255, 150))
    dis.blit(score, (x, y))


def finished():
    dead_text = dead_font.render("You DIED", True, (3, 225, 225))
    dis.blit(dead_text, (250, 250))


def Mil(x, y):
    dis.blit(MilImg, (x, y))


def enemy(x, y, i):
    dis.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bulletPos
    bulletPos = "fire"
    dis.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY): 
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    dis.fill((0, 0, 0))

    # Bg
    dis.blit(bg, (0, 0))
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            running = False
                
        # This condition is check whether user press right or left key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MilXChange = -4
            if event.key == pygame.K_RIGHT:
                MilXChange = 4
            if event.key == pygame.K_SPACE:
                if bulletPos is "ready":
                    
            
                   
                   
                    # Get the current x cordinate of the Mil plane
                    bulletX = MilX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                MilXChange = 0



    MilX += MilXChange
    if MilX <= 0:
        MilX = 0
    elif MilX >= 736:
        MilX = 736

    # Enemies
    for i in range(numOfEnymy):

        if enemyY[i] > 440:
            for j in range(numOfEnymy):
                enemyY[j] = 2000
            finished()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]      
        remove = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        
        if remove:
                     
            bulletY = 480
            bulletPos = "ready"
            point += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bulletPos = "ready"

    if bulletPos is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    Mil(MilX, MilY)
    showScore(textX, testY)
            
                           

    pygame.display.update()