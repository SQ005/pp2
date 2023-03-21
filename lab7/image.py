#1///
import pygame
import time
pygame.init()

base = pygame.image.load("mickeyclock.png")
h1 = pygame.image.load("hand-1.png")
h2 = pygame.image.load("hand-2.png")

window = pygame.display.set_mode((1000, 750))

pygame.display.set_caption("MickeyClock")

check = True
while check:
    c_time = time.localtime()

    minutes = c_time.tm_min
    seconds = c_time.tm_sec

    minutes_angle = (minutes / 60) * 360
    seconds_angle = (seconds / 60) * 360

    h1_rotated = pygame.transform.rotate(h1, -minutes_angle)
    h2_rotated = pygame.transform.rotate(h2, -seconds_angle)

    window.blit(base, (0, 0))

    h1_x = 1000 / 2 - h1_rotated.get_width() / 2
    h1_y = 750 / 2 - h1_rotated.get_height() / 2
    window.blit(h1_rotated, (h1_x, h1_y))

    h2_x = 1000 / 2 - h2_rotated.get_width() / 2
    h2_y = 750 / 2 - h2_rotated.get_height() / 2
    window.blit(h2_rotated, (h2_x, h2_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
            pygame.quit()

    pygame.time.wait(1000)

#2///
# import pygame
# pygame.init()
# pygame.mixer.music.load("birge.mp3")
# pygame.mixer.music.queue('bird.mp3')
# pygame.mixer.music.play(-1)
# img = pygame.image.load('wave.jpg')
# W,H = 1200,800
# sc = pygame.display.set_mode((W,H))
# pygame.display.set_caption("Music")
# pygame.display.set_icon(pygame.image.load("mickeyclock.jpeg"))

# WHITE = (255,255,255)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
# FPS = 60
# vol = 1.0
# sc.blit(img,(0,0))
# clock = pygame.time.Clock()
# flPause = False
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 flPause = not flPause
#                 if flPause:
#                     pygame.mixer.music.pause()
#                 else:
#                     pygame.mixer.music.unpause()
#             if event.key == pygame.K_LEFT:
#                 vol -= 0.1
#                 pygame.mixer.music.set_volume(vol)
#                 print(pygame.mixer.music.get_volume())
#             elif event.key == pygame.K_RIGHT:
#                 vol += 0.1
#                 pygame.mixer.music.set_volume(vol)
#                 print(pygame.mixer.music.get_volume())
            
            
#     clock.tick(FPS)
#     pygame.display.update()

#3///
# import pygame
# pygame.init()
# W,H = 800,600
# sc = pygame.display.set_mode((W,H))
# pygame.display.set_caption("Circle")
# WHITE = (255,255,255)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)

# FPS = 60
# clock = pygame.time.Clock()

# x = W // 2
# y = H // 2
# speed = 20

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         x -= speed
#     elif keys[pygame.K_RIGHT]:
#         x += speed
#     elif keys[pygame.K_UP]:
#         y -= speed
#     elif keys[pygame.K_DOWN]:
#         y += speed

#     sc.fill(WHITE)
#     pygame.draw.circle(sc,RED,(x,y), 25)
#     pygame.display.update()
#     clock.tick(FPS)