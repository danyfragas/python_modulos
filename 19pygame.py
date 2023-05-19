# exercício 19: Faça um programa que abra e reproduza um aúdio em arquivo mp3

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ihateu.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.quit()
