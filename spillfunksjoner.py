import pygame


def pause(width, height, screen, running):

    pausetext = pygame.font.SysFont("couriernew", 115)
    text_surf, text_rect = text_objects("Paused", pausetext)
    text_rect.center = ((width/2), (height/2))
    screen.blit(text_surf, text_rect)


