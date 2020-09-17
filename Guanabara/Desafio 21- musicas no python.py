import pygame

pygame.init()

pygame.mixer.music.load('Teste.mp3')
pygame.mixer.music.play()
pygame.event.wait()
