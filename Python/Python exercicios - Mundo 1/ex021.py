import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
# pygame.event.wait() Não funcionou pois não tinha um evento para iniciar a música (tipo um enter)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)