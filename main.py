import pygame

import random

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

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

playerHP = 6
bossHP = 20
boss2HP = 40
clock = pygame.time.Clock()


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
        if lose:
            return
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


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
        self.speed = 4

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

    def attack(self):
        rand = random.randint(0, 3)
        pygame.time.set_timer(BOSSBULLETSTORM, 0)
        if rand == 0:
            offset = random.randint(-25, 25)
            bullet = BulletRect(-410, 100 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-450, 200 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-490, 300 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-530, 400 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-570, 500 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-610, 600 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(-640, 700 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
        elif (rand == 1):
            offset = random.randint(-25, 25)
            bullet = BulletRect(SCREEN_WIDTH + 410, 100 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 450, 200 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 490, 300 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 530, 400 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 570, 500 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 610, 600 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
            bullet = BulletRect(SCREEN_WIDTH + 650, 700 + offset)
            bullets.add(bullet)
            all_sprites.add(bullet)
        else:
            pygame.time.set_timer(BOSSBULLETSTORM, 300)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed *= -1

class EnemyBoss2(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyBoss2, self).__init__()
        self.surf = pygame.image.load("boss2.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.health = boss2HP
        self.count = 0
        self.speed = 1
        self.currentattack = ""
        self.spinFrame = 0
        self.gravTimer = 0
        img = pygame.image.load("bossSpinSprites.png").convert()
        size = (int(img.get_width() / 18), int(img.get_height()))
        self.spinFrames = [self.cropImage(img, (x, y), size) for y in range(1) for x in range(18)]
        img = pygame.image.load("bossGravFrames.png").convert()
        size = (int(img.get_width() / 7), int(img.get_height()))
        self.gravFrames = [self.cropImage(img, (x, y), size) for y in range(1) for x in range(7)]
        self.evilEye = pygame.image.load("boss2evileye.png").convert()
        img = pygame.image.load("bossSwipeFrames.png").convert()
        size = (int(img.get_width() / 5), int(img.get_height()))
        self.swipeFrames = [self.cropImage(img, (x, y), size) for y in range(1) for x in range(5)]




        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 200
            )
        )

    def cropImage(self, img, position, size):
        frame = pygame.Surface(size)
        frame.blit(img, (0, 0), (position[0] * size[0], position[1] * size[1], size[0], size[1]))
        return frame

    def attack(self):
        rand = random.randint(0, 3)
        pygame.time.set_timer(LAZORBULLETS, 0)
        pygame.time.set_timer(DOWNBULLETS, 0)
        pygame.time.set_timer(BOSSSWIPE, 0)
        self.spinFrame = 0
        self.currentattack = ""
        self.gravTimer = 0
        if rand == 0:
            self.count = 0
            pygame.time.set_timer(LAZORBULLETS, 100)
        if rand == 1:
            self.currentattack = "grav"
            self.gravTimer = pygame.time.get_ticks()
            pygame.time.set_timer(DOWNBULLETS, 200)
        if rand == 2:
            self.gravTimer = pygame.time.get_ticks()
            self.surf = self.evilEye
            self.currentattack = "home"
            newBullet = Bullet(player.rect.centerx+200, player.rect.centery, player.rect.centerx, player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

            newBullet = Bullet(player.rect.centerx - 200, player.rect.centery, player.rect.centerx,
                               player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

            newBullet = Bullet(player.rect.centerx, player.rect.centery + 200, player.rect.centerx,
                               player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

            newBullet = Bullet(player.rect.centerx, player.rect.centery - 200, player.rect.centerx,
                               player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

            newBullet = Bullet(player.rect.centerx + 141, player.rect.centery + 141, player.rect.centerx,
                               player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

            newBullet = Bullet(player.rect.centerx - 141, player.rect.centery + 141, player.rect.centerx,
                               player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

            newBullet = Bullet(player.rect.centerx - 141, player.rect.centery - 141, player.rect.centerx,
                               player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

            newBullet = Bullet(player.rect.centerx + 141, player.rect.centery - 141, player.rect.centerx,
                               player.rect.centery)
            bullets.add(newBullet)
            all_sprites.add(newBullet)

        if rand == 3:
            self.currentattack = "swipe"
            self.gravTimer = pygame.time.get_ticks()
            pygame.time.set_timer(BOSSSWIPE, 800)



    def update(self):
        if self.currentattack == "grav":
            if pygame.time.get_ticks() > self.gravTimer+2500:
                if self.spinFrame <= 0:
                    self.spinFrame = 0
                else:
                    self.spinFrame -= 0.3
            else:
                if self.spinFrame >= len(self.gravFrames)-1:
                    self.spinFrame = len(self.gravFrames)-1
                else:
                    self.spinFrame += 0.3
            self.surf = self.gravFrames[int(self.spinFrame)]
        if self.currentattack == "home":
            if pygame.time.get_ticks() > self.gravTimer + 1000:
                self.surf = self.spinFrames[0]
        if self.currentattack == "swipe":
            if pygame.time.get_ticks() > self.gravTimer+400:
                if self.spinFrame <= 0:
                    self.spinFrame = 0
                else:
                    self.spinFrame -= 0.3
            else:
                if self.spinFrame >= len(self.swipeFrames)-1:
                    self.spinFrame = len(self.swipeFrames)-1
                else:
                    self.spinFrame += 0.3
            self.surf = self.swipeFrames[int(self.spinFrame)]





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

    def attack(self):
        newBullet = Bullet(self.rect.right, self.rect.bottom, player.rect.centerx, player.rect.centery)
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
    def __init__(self, x, y):
        super(ShieldNotif, self).__init__()
        self.surf = pygame.Surface((6, 20))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
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


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(PowerUp, self).__init__()
        self.surf = pygame.image.load("powerup.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
            )
        )

    def update(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerShieldPickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(PowerShieldPickup, self).__init__()
        self.surf = pygame.image.load("powerShield.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
            )
        )

    def update(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerGunPickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(PowerGunPickup, self).__init__()
        self.surf = pygame.image.load("powerShotgun.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
            )
        )

    def update(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Explosion, self).__init__()
        img = pygame.image.load("smallExplosion.png").convert()
        size = (int(img.get_width()/4), int(img.get_height()/1))
        self.flames = [ self.cropImage(img, (x, y), size) for y in range(1) for x in range(4)]
        self.act_frame = 0
        self.surf = self.flames[0]
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

    def cropImage(self, img, position, size):
        frame = pygame.Surface(size)
        frame.blit(img, (0, 0), (position[0]*size[0], position[1]*size[1], size[0], size[1]))
        return frame

    def update(self):
        self.act_frame = self.act_frame+0.2
        if (self.act_frame>=len(self.flames)):
          self.kill()
          return
        self.surf = self.flames[int(self.act_frame)]

class BigExplosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super(BigExplosion, self).__init__()
        img = pygame.image.load("bigExplosion.png").convert()
        size = (int(img.get_width()/3), int(img.get_height()/1))
        self.flames = [ self.cropImage(img, (x, y), size) for y in range(1) for x in range(3)]
        self.act_frame = 0
        self.surf = self.flames[0]
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

    def cropImage(self, img, position, size):
        frame = pygame.Surface(size)
        frame.blit(img, (0, 0), (position[0]*size[0], position[1]*size[1], size[0], size[1]))
        return frame

    def update(self):
        self.act_frame = self.act_frame+0.4
        if (self.act_frame>=len(self.flames)):
          self.kill()
          return
        self.surf = self.flames[int(self.act_frame)]

class PowerHealPickup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(PowerHealPickup, self).__init__()
        self.surf = pygame.image.load("powerHeal.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                x,
                y,
            )
        )

    def update(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


class EnemyStar(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyStar, self).__init__()
        self.surf = pygame.image.load("greenStar.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        randomX = random.randint(30, SCREEN_WIDTH - 30)
        randomY = random.randint(40, SCREEN_HEIGHT - 250)
        for boss in boss2group:
            for m in range(0, 100):
                if abs(randomX - boss.rect.centerx) < 90 and abs(randomY - boss.rect.centery) < 90:
                    randomX = random.randint(30, SCREEN_WIDTH - 30)
                    randomY = random.randint(40, SCREEN_HEIGHT - 250)
                else:
                    break
        for m in range(0, 100):
            if abs(randomX - player.rect.centerx) < 110 and abs(randomY - player.rect.centery) < 110:
                randomX = random.randint(30, SCREEN_WIDTH - 30)
                randomY = random.randint(40, SCREEN_HEIGHT - 250)
            else:
                break
        self.rect = self.surf.get_rect(
            center=(
                randomX,
                randomY,
            )
        )
        self.speed = 5

    def attack(self):
        newBullet = Bullet(self.rect.right, self.rect.bottom, self.rect.right + 600, self.rect.bottom)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.bottom, self.rect.right + 424, self.rect.bottom + 424)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.bottom, self.rect.right, self.rect.bottom + 600)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.left, self.rect.bottom, self.rect.left - 424, self.rect.bottom + 424)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.left, self.rect.bottom, self.rect.left - 600, self.rect.bottom)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.left, self.rect.top, self.rect.left - 424, self.rect.top - 424)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.top, self.rect.right, self.rect.top - 600)
        bullets.add(newBullet)
        all_sprites.add(newBullet)

        newBullet = Bullet(self.rect.right, self.rect.top, self.rect.right + 424, self.rect.top - 424)
        bullets.add(newBullet)
        all_sprites.add(newBullet)


class PlayerShield(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerShield, self).__init__()
        img = pygame.image.load("shieldFrames.png").convert()
        size = (int(img.get_width() / 5), int(img.get_height()))
        self.frames = [self.cropImage(img, (x, y), size) for y in range(1) for x in range(5)]
        self.surf = self.frames[0]
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.spinFrame = 0
        self.rect = self.surf.get_rect(
            center=(
                player.rect.right - 10,
                player.rect.top + 10
            )
        )

    def cropImage(self, img, position, size):
        frame = pygame.Surface(size)
        frame.blit(img, (0, 0), (position[0] * size[0], position[1] * size[1], size[0], size[1]))
        return frame

    def update(self):
        self.spinFrame += 0.7
        if self.spinFrame >= len(self.frames):
            self.surf = self.frames[len(self.frames)-1]
            self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        else:
            self.surf = self.frames[int(self.spinFrame)]
            self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, targetx, targety):
        super(PlayerBullet, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(
            center=(
                player.rect.right - 10,
                player.rect.top
            )
        )
        self.speedX = targetx
        self.speedY = targety

    def update(self):
        self.rect.move_ip(self.speedX, self.speedY)
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, targetx, targety):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(
            center=(
                x,
                y
            )
        )
        self.speedX = (targetx - self.rect.right) / 100
        self.speedY = (targety - self.rect.bottom) / 100



    def update(self):
        self.rect.move_ip(self.speedX, self.speedY)
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
        if self.rect.centerx == self.x and self.rect.centery == self.y:
            self.speedY = 2



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

    def update(self):
        self.rect.move_ip(self.speedX, 0)
        if self.x < 0:
            if self.rect.left > SCREEN_WIDTH:
                self.kill()
        elif self.x > SCREEN_WIDTH:
            if self.rect.right < 0:
                self.kill()

class BackgroundStar(pygame.sprite.Sprite):
  def __init__(self, position=0):
    super(BackgroundStar, self).__init__()
    self.speed = random.uniform(0.2, 0.6)
    self.size = int(self.speed * 4)
    self.surf = pygame.Surface((self.size*2, self.size*2))
    pygame.draw.circle(self.surf, (187, 214, 250), (self.size, self.size), self.size)
    self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
    self.rect = self.surf.get_rect(
       center = (
        random.randint(0, SCREEN_WIDTH+100),
        random.randint(0, position)
        )
    )
    self.realPositionY = self.rect.centery

  def update(self):
    self.realPositionY+=self.speed
    self.rect.centery = int(self.realPositionY)
    if self.rect.top>SCREEN_HEIGHT:
      self.kill()


pygame.mixer.init()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

shootSound = pygame.mixer.Sound("ATTACK5.wav")
shieldSound = pygame.mixer.Sound("TWINKLE.wav")
hitSound = pygame.mixer.Sound("DEAD.wav")
shieldReadySound = pygame.mixer.Sound("POWER UP.wav")
pickupSound = pygame.mixer.Sound("1UP.wav")
gunSound = pygame.mixer.Sound("gun.mp3")
healSound = pygame.mixer.Sound("heal.mp3")
bossDeathSound = pygame.mixer.Sound("bossdeath.wav")

shootSound.set_volume(0.05)
bossDeathSound.set_volume(0.4)
shieldSound.set_volume(0.1)
hitSound.set_volume(0.1)
pickupSound.set_volume(0.1)
shieldReadySound.set_volume(0.1)
gunSound.set_volume(0.2)
healSound.set_volume(0.25)

font = pygame.font.Font(None, 36)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 2000)

ADDBULLET = pygame.USEREVENT + 2
pygame.time.set_timer(ADDBULLET, 1000)

BOSSBULLETSTORM = pygame.USEREVENT + 3
BOSSATTACK = pygame.USEREVENT + 4

POWERGAUGE = pygame.USEREVENT + 5
pygame.time.set_timer(POWERGAUGE, 1000)


ADDSTAR = pygame.USEREVENT + 6
pygame.time.set_timer(ADDSTAR, 1000)

LAZORBULLETS = pygame.USEREVENT + 7

DOWNBULLETS = pygame.USEREVENT + 8

BOSSSWIPE = pygame.USEREVENT + 9


ADDSTAR = pygame.USEREVENT + 6
pygame.time.set_timer(ADDSTAR, 1000)
stars = pygame.sprite.Group()




enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
playerBullets = pygame.sprite.Group()
shieldGroup = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
bossgroup = pygame.sprite.Group()
boss2group = pygame.sprite.Group()
explosions = pygame.sprite.Group()
healthPickups = pygame.sprite.Group()
shieldPickups = pygame.sprite.Group()
gunPickups = pygame.sprite.Group()

powerUps = pygame.sprite.Group()
notifGroup = pygame.sprite.Group()

for i in range(100):
  star = BackgroundStar(SCREEN_HEIGHT)
  stars.add(star)
  all_sprites.add(star)

healthOrbs = []
bossHealthOrbs = []
powerGauge = []

for i in range(0, playerHP):
    healthOrbs.append(HealthOrb(10 + i * 20, 10))
    all_sprites.add(healthOrbs[i])




shieldGauge = 15
for i in range(0, shieldGauge):
    powerGauge.append(ShieldNotif(SCREEN_WIDTH/2 - 60 + i * 6, 10))
    all_sprites.add(powerGauge[i])


powerIndicator = PowerShieldPickup(SCREEN_WIDTH/2 - 60 + shieldGauge*6 + 10, 10)
all_sprites.add(powerIndicator)




running = True

time = 0
shieldDeathTime = 0

selectedPower = "shield"
pityTimer = 3


endTime = 0
kill = 0
IframeTime = 0
win = False
lose = False
game = False

while running:

    if(game == False):
        for sprite in all_sprites.sprites():
            sprite.kill()
        screen.fill((0, 0, 0))

        text = font.render("KULCORP ATTACKS!", True, (63, 14, 175))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 - 300
        screen.blit(text, [text_x, text_y])
        text = font.render("Steruj strza??kami", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 - 200
        screen.blit(text, [text_x, text_y])
        text = font.render("Kliknij Z aby strzela??", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 - 100
        screen.blit(text, [text_x, text_y])
        text = font.render("Kliknij X aby u??y?? specjalnej zdolno??ci", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        text = font.render("gdy masz na to energie", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 + 25
        screen.blit(text, [text_x, text_y])
        text = font.render("Z przeciwnik??w mog?? wypa????", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 + 100
        screen.blit(text, [text_x, text_y])
        text = font.render("inne specjalne zdolno??ci", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 + 125
        screen.blit(text, [text_x, text_y])
        text = font.render("Podno?? plusy aby zdobywa?? energie", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 + 200
        screen.blit(text, [text_x, text_y])
        text = font.render("Wci??nij Z aby zacz????!", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
        text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2 + 300
        screen.blit(text, [text_x, text_y])


        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_z:


                    pygame.mixer.music.load("muzyczka.mp3")
                    pygame.mixer.music.play(loops=-1)
                    pygame.mixer.music.set_volume(0.1)

                    time = 0
                    shieldDeathTime = 0
                    selectedPower = "shield"
                    pityTimer = 3
                    endTime = 0
                    kill = 0
                    win = False
                    lose = False
                    game = True
                    player = Player()
                    all_sprites.add(player)
                    players.add(player)

                    for i in range(100):
                        star = BackgroundStar(SCREEN_HEIGHT)
                        stars.add(star)
                        all_sprites.add(star)

                    healthOrbs = []
                    bossHealthOrbs = []
                    powerGauge = []

                    for i in range(0, playerHP):
                        healthOrbs.append(HealthOrb(10 + i * 20, 10))
                        all_sprites.add(healthOrbs[i])

                    shieldGauge = 15
                    for i in range(0, shieldGauge):
                        powerGauge.append(ShieldNotif(SCREEN_WIDTH / 2 - 60 + i * 6, 10))
                        all_sprites.add(powerGauge[i])

                    powerIndicator = PowerShieldPickup(SCREEN_WIDTH / 2 - 60 + shieldGauge * 6 + 10, 10)
                    all_sprites.add(powerIndicator)

                    pygame.time.set_timer(ADDENEMY, 2000)
                    pygame.time.set_timer(ADDBULLET, 1000)
                    pygame.time.set_timer(POWERGAUGE, 1000)
                    pygame.time.set_timer(ADDSTAR, 1000)
    else:
        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_z and not lose:
                    if pygame.time.get_ticks() > time + 300:
                        new_bullet = PlayerBullet(0, -20)
                        shootSound.play()
                        playerBullets.add(new_bullet)
                        all_sprites.add(new_bullet)
                        time = pygame.time.get_ticks()
                if event.key == K_x and not lose:
                    if shieldGauge >= 15:
                        if selectedPower == "shield":
                            playerShield = PlayerShield()
                            shieldSound.play()
                            shieldGroup.add(playerShield)
                            all_sprites.add(playerShield)
                            shieldDeathTime = pygame.time.get_ticks()
                        elif selectedPower == "gun":
                            gunSound.play()
                            bullet = PlayerBullet(0, -20)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(-2.5, -17.5)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(2.5, -17.5)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(-5, -15)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(5, -15)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(-2.5, -12.5)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(2.5, -12.5)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(-10, -10)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)

                            bullet = PlayerBullet(10, -10)
                            playerBullets.add(bullet)
                            all_sprites.add(bullet)
                        else:
                            if(player.health < playerHP-1):
                                healSound.play()
                                healthOrbs[player.health].kill()
                                healthOrbs[player.health] = HealthOrb(10 + (player.health) * 20, 10)
                                all_sprites.add(healthOrbs[player.health])
                                player.health += 1
                                healthOrbs[player.health].kill()
                                healthOrbs[player.health] = HealthOrb(10 + (player.health) * 20, 10)
                                all_sprites.add(healthOrbs[player.health])
                                player.health += 1
                            elif (player.health < playerHP):
                                healSound.play()
                                healthOrbs[player.health].kill()
                                healthOrbs[player.health] = HealthOrb(10 + (player.health) * 20, 10)
                                all_sprites.add(healthOrbs[player.health])
                                player.health += 1



                        shieldGauge = 0
                        #print("Aktywacja tarczy!")
                        for s in powerGauge:
                            s.kill()

            elif event.type == QUIT:
                running = False


            elif event.type == ADDSTAR:
                star = BackgroundStar()
                stars.add(star)
                all_sprites.add(star)

            elif event.type == BOSSSWIPE:
                bullet = BulletRect(random.choice((-200, SCREEN_WIDTH+200)), player.rect.centery)
                bullets.add(bullet)
                all_sprites.add(bullet)

            elif event.type == ADDENEMY:
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

            elif event.type == POWERGAUGE:
                if shieldGauge < 15:
                    #print(shieldGauge)
                    if shieldGauge > 15:
                        shieldGauge = 15
                    powerGauge[shieldGauge] = ShieldNotif(SCREEN_WIDTH / 2 - 60 + shieldGauge * 6, 10)
                    all_sprites.add(powerGauge[shieldGauge])
                    shieldGauge += 1



                    if shieldGauge == 15:
                        shieldReadySound.play()

            elif event.type == BOSSATTACK:

                for boss in bossgroup.sprites():
                    kill = 9
                    boss.attack()
                for boss2 in boss2group.sprites():
                    boss2.attack()

            elif event.type == LAZORBULLETS:
                for boss in boss2group.sprites():
                    newBullet = Bullet(boss.rect.left+boss.count*1.75, boss.rect.top, boss.rect.left-600+boss.count*30,
                                       boss.rect.top-600)
                    bullets.add(newBullet)
                    all_sprites.add(newBullet)

                    newBullet = Bullet(boss.rect.right, boss.rect.top+boss.count*1.75, boss.rect.right + 600,
                                       boss.rect.top - 600 + boss.count * 30)
                    bullets.add(newBullet)
                    all_sprites.add(newBullet)

                    newBullet = Bullet(boss.rect.right-boss.count*1.75, boss.rect.bottom, boss.rect.right + 600 - boss.count * 30,
                                       boss.rect.bottom + 600)
                    bullets.add(newBullet)
                    all_sprites.add(newBullet)

                    newBullet = Bullet(boss.rect.left, boss.rect.bottom-boss.count*1.75, boss.rect.left - 600,
                                       boss.rect.bottom + 600 - boss.count * 30)
                    bullets.add(newBullet)
                    all_sprites.add(newBullet)

                    boss.spinFrame += 0.5
                    if boss.spinFrame >= len(boss.spinFrames):
                        boss.surf = boss.spinFrames[0]
                    else:
                        boss.surf = boss.spinFrames[int(boss.spinFrame)]

                    boss.count += 1

            elif event.type == DOWNBULLETS:
                x = random.randint(0, SCREEN_WIDTH)
                newBullet = Bullet(x, SCREEN_HEIGHT, x,
                                   0)
                bullets.add(newBullet)
                all_sprites.add(newBullet)

            elif event.type == BOSSBULLETSTORM:
                for boss in bossgroup.sprites():
                    newBullet = Bullet(boss.rect.right + 10, boss.rect.bottom - 20, player.rect.centerx,
                                       player.rect.centery)
                    bullets.add(newBullet)
                    all_sprites.add(newBullet)
                    newBullet = Bullet(boss.rect.left - 10, boss.rect.bottom - 20, player.rect.centerx, player.rect.centery)
                    bullets.add(newBullet)
                    all_sprites.add(newBullet)

        pressed_keys = pygame.key.get_pressed()

        stars.update()

        enemies.update()
        bullets.update()
        bossgroup.update()
        boss2group.update()
        explosions.update()
        playerBullets.update()
        player.update(pressed_keys)
        powerUps.update()
        gunPickups.update()
        shieldPickups.update()
        healthPickups.update()
        shieldGroup.update()




        screen.fill((0, 0, 0))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if win:
            text = font.render("Uda??o si??!", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
            text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            if pygame.time.get_ticks() > endTime + 11000:
                pygame.time.set_timer(ADDENEMY, 0)
                pygame.time.set_timer(ADDBULLET, 0)
                pygame.time.set_timer(BOSSATTACK, 0)
                pygame.time.set_timer(LAZORBULLETS, 0)
                pygame.time.set_timer(DOWNBULLETS, 0)
                pygame.time.set_timer(BOSSSWIPE, 0)
                game = False
        if lose:
            text = font.render("Nie ??yjesz!", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_x = SCREEN_WIDTH / 2 - text_rect.width / 2
            text_y = SCREEN_HEIGHT / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            if pygame.time.get_ticks() > endTime + 11000:
                pygame.time.set_timer(ADDENEMY, 0)
                pygame.time.set_timer(ADDBULLET, 0)
                pygame.time.set_timer(BOSSATTACK, 0)
                pygame.time.set_timer(LAZORBULLETS, 0)
                pygame.time.set_timer(DOWNBULLETS, 0)
                pygame.time.set_timer(BOSSSWIPE, 0)
                game = False

        if pygame.sprite.groupcollide(players, bullets, False, True):
            if pygame.time.get_ticks() > IframeTime + 500:
                healthOrbs[player.health - 1].kill()
                player.health -= 1
                #print("STAN HP:", player.health)
                hitSound.play()
                IframeTime = pygame.time.get_ticks()
                if player.health <= 0:
                    explosion = BigExplosion((player.rect.centerx, player.rect.centery))
                    explosions.add(explosion)
                    all_sprites.add(explosion)
                    player.kill()
                    endTime = pygame.time.get_ticks()
                    pygame.mixer.music.load("lose.mp3")
                    pygame.mixer.music.play(loops=1)
                    pygame.mixer.music.set_volume(0.3)
                    lose = True

        pygame.sprite.groupcollide(enemies, shieldGroup, True, False)
        pygame.sprite.groupcollide(bullets, shieldGroup, True, False)
        if pygame.sprite.groupcollide(players, powerUps, False, True):
            if shieldGauge < 15:
                shieldGauge += 3
                #pickupSound.play()
                if shieldGauge > 15:
                    shieldGauge = 15
                powerGauge[shieldGauge - 3].kill()
                powerGauge[shieldGauge - 3] = ShieldNotif(SCREEN_WIDTH / 2 - 60 + (shieldGauge - 3) * 6, 10)
                all_sprites.add(powerGauge[shieldGauge - 3])
                powerGauge[shieldGauge - 2].kill()
                powerGauge[shieldGauge - 2] = ShieldNotif(SCREEN_WIDTH / 2 - 60 + (shieldGauge - 2) * 6, 10)
                all_sprites.add(powerGauge[shieldGauge - 2])
                powerGauge[shieldGauge - 1].kill()
                powerGauge[shieldGauge-1] = ShieldNotif(SCREEN_WIDTH / 2 - 60 + (shieldGauge-1) * 6, 10)
                all_sprites.add(powerGauge[shieldGauge-1])
                if shieldGauge == 15:
                    shieldReadySound.play()

        if pygame.sprite.groupcollide(players, shieldPickups, False, True):
            pickupSound.play()
            selectedPower = "shield"
            powerIndicator.kill()
            powerIndicator = PowerShieldPickup(SCREEN_WIDTH / 2 - 60 + 100, 10)
            all_sprites.add(powerIndicator)

        if pygame.sprite.groupcollide(players, healthPickups, False, True):
            pickupSound.play()
            selectedPower = "heal"
            powerIndicator.kill()
            powerIndicator = PowerHealPickup(SCREEN_WIDTH / 2 - 60 + 100, 10)
            all_sprites.add(powerIndicator)

        if pygame.sprite.groupcollide(players, gunPickups, False, True):
            pickupSound.play()
            selectedPower = "gun"
            powerIndicator.kill()
            powerIndicator = PowerGunPickup(SCREEN_WIDTH / 2 - 60 + 100, 10)
            all_sprites.add(powerIndicator)


        enemiesShot = pygame.sprite.groupcollide(enemies, playerBullets, True, True)
        if enemiesShot:
            for enemyShot in enemiesShot:
                oneUp = PowerUp(enemyShot.rect.centerx, enemyShot.rect.centery)
                powerUps.add(oneUp)
                all_sprites.add(oneUp)
                if pityTimer == 0:
                    pickupChance = 4
                else:
                    pickupChance = random.randint(0, pityTimer)
                if pickupChance == 4:
                    powerChoice = random.randint(0, 2)
                    pityTimer = 3
                    if powerChoice == 0:
                        powerpickup = PowerHealPickup(enemyShot.rect.centerx, enemyShot.rect.centery)
                        healthPickups.add(powerpickup)
                        all_sprites.add(powerpickup)
                    elif powerChoice == 1:
                        powerpickup = PowerGunPickup(enemyShot.rect.centerx, enemyShot.rect.centery)
                        gunPickups.add(powerpickup)
                        all_sprites.add(powerpickup)
                    else:
                        powerpickup = PowerShieldPickup(enemyShot.rect.centerx, enemyShot.rect.centery)
                        shieldPickups.add(powerpickup)
                        all_sprites.add(powerpickup)
                else:
                    pityTimer-=1
                explosion = Explosion((enemyShot.rect.centerx, enemyShot.rect.centery))
                explosions.add(explosion)
                all_sprites.add(explosion)
            kill += 1


            if kill == 8:
                for i in range(0, bossHP):
                    bossHealthOrbs.append(BossHealthOrb(SCREEN_WIDTH - i * 3, 10))
                    all_sprites.add(bossHealthOrbs[i])
                boss = EnemyBoss()
                bossgroup.add(boss)
                all_sprites.add(boss)
                pygame.time.set_timer(ADDENEMY, 5000)
                pygame.time.set_timer(BOSSATTACK, 3000)
            if kill == 17:
                for i in range(0, boss2HP):
                    bossHealthOrbs.append(BossHealthOrb(SCREEN_WIDTH - i * 3, 10))
                    all_sprites.add(bossHealthOrbs[i])
                boss = EnemyBoss2()
                boss2group.add(boss)
                all_sprites.add(boss)
                pygame.time.set_timer(ADDENEMY, 5000)
                pygame.time.set_timer(BOSSATTACK, 4000)

        if pygame.sprite.groupcollide(bossgroup, playerBullets, False, True):
            for boss in bossgroup.sprites():
                bossHealthOrbs[boss.health - 1].kill()
                boss.health -= 1


                if boss.health <= 0:
                    explosion = BigExplosion((boss.rect.centerx, boss.rect.centery))
                    explosions.add(explosion)
                    all_sprites.add(explosion)
                    boss.kill()
                    bossDeathSound.play()
                    pygame.time.set_timer(ADDENEMY, 2000)
                    pygame.time.set_timer(BOSSATTACK, 0)
                    kill = 9


        if pygame.sprite.groupcollide(boss2group, playerBullets, False, True):
            for boss2 in boss2group.sprites():

                bossHealthOrbs[boss2.health - 1].kill()
                boss2.health -= 1

                if boss2.health <= 0:
                    boss2.kill()

                    pygame.mixer.music.load("win.mp3")
                    pygame.mixer.music.play(loops=1)
                    pygame.mixer.music.set_volume(0.1)

                    for enemy in enemies.sprites():
                        enemy.kill()
                    for bullet in bullets.sprites():
                        bullet.kill()
                    explosion = BigExplosion((boss2.rect.centerx, boss2.rect.centery))
                    explosions.add(explosion)
                    all_sprites.add(explosion)
                    pygame.time.set_timer(ADDENEMY, 0)
                    pygame.time.set_timer(ADDBULLET, 0)
                    pygame.time.set_timer(BOSSATTACK, 0)
                    pygame.time.set_timer(LAZORBULLETS, 0)
                    pygame.time.set_timer(DOWNBULLETS, 0)
                    pygame.time.set_timer(BOSSSWIPE, 0)

                    win = True
                    endTime = pygame.time.get_ticks()

        if pygame.time.get_ticks() > shieldDeathTime + 1000:
            for shield in shieldGroup.sprites():
                shield.kill()


        # screen.blit(player.surf, player.rect)

    pygame.display.flip()
    clock.tick(60)
