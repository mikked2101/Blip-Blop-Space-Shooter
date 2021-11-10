# Kritisk oppsett

import pygame
successes, failures = pygame.init()
print(f"{successes} successes and {failures} failures")

# Musikk
music = 'blip_blop_music.wav'
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

# Lager variabler for senere bruk

# Skjerm
size = width, height = 600, 800
screen = pygame.display.set_mode(size)

# Klokke
clock = pygame.time.Clock()
FPS = 60

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Spiller
player = pygame.image.load("fighter_1.png")
x_vel = 0
y_vel = 0
player_vel = 5
player_rect = player.get_rect(center=(width//2, height//2))

# Fiender
boss = pygame.image.load("enemy_1.png")
boss = pygame.transform.flip(boss, False, True)
boss_rect = boss.get_rect(center=(width//2, -300))
boss_speed = [0, 1]

"""ball = pygame.image.load("badeball.png")
ball = pygame.transform.scale(ball, (50, 50))
ball_rect = ball.get_rect()
ball_speed = [1, 1]"""

# Kuler
obullet = pygame.image.load("oransj_kule.png")
obullet = pygame.transform.scale(obullet, (15, 25))
bullets = []
bullet_speed = [0, -7]
player_cooldown = 10

obossbullet = pygame.image.load("blaa_kule.png")
obossbullet = pygame.transform.scale(obossbullet, (15, 25))
bossbullets = []
bossbullet_speed = [0, 7]
o_bosscooldown = 60

cooldown = 0
bosscooldown = 0


# Spilløkken

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pressed = pygame.key.get_pressed()

# Gir farter til spilleren avhengig av hvilken tast de trykker
        if pressed[pygame.K_w] and pressed[pygame.K_s]:
            y_vel = 0
        elif pressed[pygame.K_w]:
            y_vel = -1
        elif pressed[pygame.K_s]:
            y_vel = 1
        else:
            y_vel = 0

        if pressed[pygame.K_a] and pressed[pygame.K_d]:
            x_vel = 0
        elif pressed[pygame.K_a]:
            x_vel = -1
        elif pressed[pygame.K_d]:
            x_vel = 1
        else:
            x_vel = 0


# Her skyter jeg kuler
        """if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_rect.centerx - 50, player_rect.centery])
                bullets.append([player_rect.centerx + 35, player_rect.centery])"""
        """if event.type == pygame.KEYUP:"""

    # Sier her at kulene skal skyte kontinuerlig med en gitt "cooldown"
    cooldown += 1
    if cooldown == player_cooldown:
        bullets.append([player_rect.centerx - 50, player_rect.centery])  # FIKS spiller spriten
        bullets.append([player_rect.centerx + 35, player_rect.centery])
        cooldown = 0

    bosscooldown += 1
    if bosscooldown == o_bosscooldown:
        bossbullets.append([boss_rect.centerx - 50, boss_rect.centery])  # FIKS spiller spriten
        bossbullets.append([boss_rect.centerx + 35, boss_rect.centery])
        bosscooldown = 0

    # Her stoppes spilleren ved kantene på brettet
    if player_rect.left < 0:
        player_rect.move_ip(-player_rect.left, 0)
    elif player_rect.right > width:
        player_rect.move_ip(width - player_rect.right, 0)

    if player_rect.top < 0:
        player_rect.move_ip(0, -player_rect.top)
    elif player_rect.bottom > height:
        player_rect.move_ip(0, height - player_rect.bottom)

    # Beveger karakteren med gitte x- og y-farter.
    player_rect.move_ip(player_vel * x_vel, player_vel * y_vel)

    # Beveger prosjektiler
    for b in range(len(bullets)):
        bullets[b][1] += bullet_speed[1]

    for b in range(len(bossbullets)):
        bossbullets[b][1] += bossbullet_speed[1]

    # Fjerner prosjektiler
    for bullet in bullets[:]:
        if bullet[1] < 0:
            bullets.remove(bullet)

    for bullet in bossbullets[:]:
        if bullet[1] > height:
            bossbullets.remove(bullet)

    # Beveger fiender
    if boss_rect.centery < 100:
        boss_rect = boss_rect.move(boss_speed)

    # Sjekker kollisjoner
    for bullet in bullets[:]:
        if pygame.Rect(bullet[0], bullet[1], 0, 0).colliderect(boss_rect) == True:
            bullets.remove(bullet)
            
    """ball_rect = ball_rect.move(ball_speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed[1] = -ball_speed[1]"""

# Her tegner jeg objektene på nytt og fyller skjærmen med sort
    screen.fill(BLACK)

    for bullet in bullets:
        screen.blit(obullet, pygame.Rect(bullet[0], bullet[1], 0, 0))

    for bullet in bossbullets:
        screen.blit(obossbullet, pygame.Rect(bullet[0], bullet[1], 0, 0))

    screen.blit(boss, boss_rect)
    screen.blit(player, player_rect)
    """screen.blit(ball, ball_rect)"""
    pygame.display.update()

pygame.display.quit()  # Hvis jeg går ut av spill-loopen, vil spillvinduet lukke seg, slik at jeg kan bruke terminalen.
pygame.mixer.music.stop()
