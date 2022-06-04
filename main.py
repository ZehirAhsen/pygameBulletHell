# Import the pygame module
import pygame
# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    RLEACCEL,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_z,
    K_x,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

playerHP = 4
bossHP = 15
clock = pygame.time.Clock()


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT,
            ))
        self.health = playerHP

    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite

# The surface you draw on the screen is now an attribute of 'enemy'
class EnemyBomber(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyBomber, self).__init__()
        self.surf = pygame.image.load("pinkBomber.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(40, SCREEN_WIDTH - 20),
                random.randint(40, 140),
            )
        )
        self.speed = 5

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed *= -1

    def attack(self):
        newBullet = Bullet(self.rect.right, self.rect.bottom, self.rect.right, SCREEN_HEIGHT)
        bullets.add(newBullet)
        all_sprites.add(newBullet)


class EnemyBoss(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyBoss, self).__init__()
        self.surf = pygame.image.load("boss.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.health = bossHP
        self.speed = 1
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 200
            )
        )

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen

    def attack(self):
        rand = random.randint(0, 3)
        pygame.time.set_timer(BOSSBULLETSTORM, 0)
        if rand == 0:
            offset = random.randint(-25, 25)
            bullet = BulletRect(-10, 100 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-50, 200 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-90, 300 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-130, 400 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-170, 500 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-170, 600 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-170, 700 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
        elif (rand == 1):
            offset = random.randint(-25, 25)
            bullet = BulletRect(SCREEN_WIDTH + 10, 100 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 50, 200 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 90, 300 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 130, 400 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 210, 500 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 250, 600 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 290, 700 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
        else:
            pygame.time.set_timer(BOSSBULLETSTORM, 300)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed *= -1


class EnemyGun(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyGun, self).__init__()
        self.surf = pygame.image.load("redStar.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(20, SCREEN_WIDTH - 20),
                random.randint(40, 400),
            )
        )
        self.speed = 5

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen

    def attack(self):
        newBullet = Bullet(self.rect.right, self.rect.bottom, player.rect.right, player.rect.bottom)
        bullets.add(newBullet)
        all_sprites.add(newBullet)


class HealthOrb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(HealthOrb, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((113, 255, 31))
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
            )
        )


class ShieldNotif(pygame.sprite.Sprite):
    def __init__(self):
        super(ShieldNotif, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                0,
            )
        )


class BossHealthOrb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(BossHealthOrb, self).__init__()
        self.surf = pygame.Surface((3, 20))
        self.surf.fill((63, 14, 175))
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
            )
        )


class EnemyStar(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyStar, self).__init__()
        self.surf = pygame.image.load("greenStar.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(30, SCREEN_WIDTH - 30),
                random.randint(40, SCREEN_HEIGHT - 100),
            )
        )
        self.speed = 5

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def attack(self):
        newBullet = Bullet(self.rect.right, self.rect.bottom, self.rect.right + 800, self.rect.bottom)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.bottom, self.rect.right + 600, self.rect.bottom + 600)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.bottom, self.rect.right, self.rect.bottom + 800)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.left, self.rect.bottom, self.rect.left - 600, self.rect.bottom + 600)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.left, self.rect.bottom, self.rect.left - 800, self.rect.bottom)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.left, self.rect.top, self.rect.left - 600, self.rect.top - 600)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.top, self.rect.right, self.rect.top - 800)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.top, self.rect.right + 600, self.rect.top - 600)
        bullets.add(newBullet)
        all_sprites.add(newBullet)


class PlayerShield(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerShield, self).__init__()
        self.surf = pygame.image.load("shieldsprite.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                player.rect.right - 10,
                player.rect.top + 10
            )
        )


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerBullet, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(
            center=(
                player.rect.right - 10,
                player.rect.top
            )
        )

        # Move the sprite based on speed

    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        # self.rect.move_ip(0, self.speed)
        self.rect.move_ip(0, -20)
        if self.rect.bottom < 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, targetx, targety):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                x,
                y
            )
        )
        self.speedX = (targetx - self.rect.right) / 100
        self.speedY = (targety - self.rect.bottom) / 100

        # Move the sprite based on speed

    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        # self.rect.move_ip(0, self.speed)
        self.rect.move_ip(self.speedX, self.speedY)
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


class BulletRect(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(BulletRect, self).__init__()
        self.x = x
        self.y = y
        self.surf = pygame.Surface((400, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                x,
                y
            )
        )
        if self.x < 0:
            self.speedX = 5
        elif self.x > SCREEN_WIDTH:
            self.speedX = -5
        # Move the sprite based on speed

    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        # self.rect.move_ip(0, self.speed)
        self.rect.move_ip(self.speedX, 0)
        if self.x < 0:
            if self.rect.left > SCREEN_WIDTH:
                self.kill()
        elif self.x > SCREEN_WIDTH:
            if self.rect.right < 0:
                self.kill()



# Setup for sounds. Defaults are good.
pygame.mixer.init()
# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

shootSound = pygame.mixer.Sound("ATTACK5.wav")
shieldSound = pygame.mixer.Sound("TWINKLE.wav")
hitSound = pygame.mixer.Sound("DEAD.wav")

shootSound.set_volume(0.05)
shieldSound.set_volume(0.1)
hitSound.set_volume(0.1)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 2000)

ADDBULLET = pygame.USEREVENT + 2
pygame.time.set_timer(ADDBULLET, 1000)

BOSSBULLETSTORM = pygame.USEREVENT + 3
BOSSATTACK = pygame.USEREVENT + 4

# Instantiate player. Right now, this is just a rectangle.
# Create the 'player'
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
playerBullets = pygame.sprite.Group()
shieldGroup = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
bossgroup = pygame.sprite.Group()
notifGroup = pygame.sprite.Group()
all_sprites.add(player)
players.add(player)

healthOrbs = []
bossHealthOrbs = []

for i in range(0, playerHP):
    healthOrbs.append(HealthOrb(10 + i * 20, 10))
    all_sprites.add(healthOrbs[i])

for i in range(0, bossHP):
    bossHealthOrbs.append(BossHealthOrb(SCREEN_WIDTH - i * 3, 10))
    all_sprites.add(bossHealthOrbs[i])

shieldNotif = ShieldNotif()
all_sprites.add(shieldNotif)
notifGroup.add(shieldNotif)

pygame.mixer.music.load("muzyczka.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

# Variable to keep the main loop running
running = True

time = 0
shieldDeathTime = 0
shieldTime = -15000
kill = 0
IframeTime = 0

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_z:
                if pygame.time.get_ticks() > time + 300:
                    new_bullet = PlayerBullet()
                    shootSound.play()
                    playerBullets.add(new_bullet)
                    all_sprites.add(new_bullet)
                    time = pygame.time.get_ticks()
            if event.key == K_x:
                if pygame.time.get_ticks() > shieldTime + 15000:
                    playerShield = PlayerShield()
                    shieldSound.play()
                    shieldGroup.add(playerShield)
                    all_sprites.add(playerShield)
                    shieldTime = pygame.time.get_ticks()
                    shieldDeathTime = pygame.time.get_ticks()
                    for notif in notifGroup.sprites():
                        notif.kill()




        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            rand = random.randint(0, 2)
            if rand == 0:
                new_enemy = EnemyGun()
            elif rand == 1:
                new_enemy = EnemyStar()
            else:
                new_enemy = EnemyBomber()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDBULLET:
            for enemy in enemies.sprites():
                enemy.attack()

        elif event.type == BOSSATTACK:
            for boss in bossgroup.sprites():
                boss.attack()

        elif event.type == BOSSBULLETSTORM:
            for boss in bossgroup.sprites():
                newBullet = Bullet(boss.rect.right + 10, boss.rect.bottom - 20, player.rect.left, player.rect.bottom)
                bullets.add(newBullet)
                all_sprites.add(newBullet)
                newBullet = Bullet(boss.rect.left - 10, boss.rect.bottom - 20, player.rect.right, player.rect.bottom)
                bullets.add(newBullet)
                all_sprites.add(newBullet)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()
    bullets.update()
    bossgroup.update()
    playerBullets.update()
    # Fill the screen with black
    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.groupcollide(players, bullets, False, True):
        # If so, then remove the player and stop the loop
        healthOrbs[player.health - 1].kill()
        if pygame.time.get_ticks() > IframeTime + 1000:
            player.health -= 1
            hitSound.play()
            IframeTime = pygame.time.get_ticks()
        if player.health <= 0:
            player.kill()
            running = False
    pygame.sprite.groupcollide(enemies, shieldGroup, True, False)
    pygame.sprite.groupcollide(bullets, shieldGroup, True, False)
    if pygame.sprite.groupcollide(enemies, playerBullets, True, True):
        kill += 1
        if kill == 5:
            boss = EnemyBoss()
            bossgroup.add(boss)
            all_sprites.add(boss)
            pygame.time.set_timer(ADDENEMY, 5000)
            pygame.time.set_timer(BOSSATTACK, 3000)
    if pygame.sprite.groupcollide(bossgroup, playerBullets, False, True):
        for boss in bossgroup.sprites():
            bossHealthOrbs[boss.health - 1].kill()
            boss.health -= 1

            if boss.health <= 0:
                pygame.mixer.music.load("win.mp3")
                pygame.mixer.music.play(loops=1)
                pygame.mixer.music.set_volume(0.1)
                boss.kill()
                for enemy in enemies.sprites():
                    enemy.kill()
                for bullet in bullets.sprites():
                    bullet.kill()
                pygame.time.set_timer(ADDENEMY, 0)
                pygame.time.set_timer(ADDBULLET, 5000)
                pygame.time.set_timer(BOSSATTACK, 0)

    if (pygame.time.get_ticks() > shieldDeathTime + 1000):
        for shield in shieldGroup.sprites():
            shield.kill()
    if pygame.time.get_ticks() > shieldDeathTime + 15000:
        shieldNotif = ShieldNotif()
        all_sprites.add(shieldNotif)
        notifGroup.add(shieldNotif)

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)
