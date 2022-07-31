# tocando audio
import pygame
# iniciar o mixer
pygame.mixer.init()
# iniciar o pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
print('\033[46m~\033[m'*30)
print('\033[34;41m TOCANDO ROSALIAAAAA          \033[m')
print('\033[46m~\033[m'*30)
pygame.mixer.music.play()
# quando o evento terminar, encerrar o programa
pygame.event.wait()
