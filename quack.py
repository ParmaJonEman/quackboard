import keyboard
import pygame

pygame.mixer.init()
quack_sound = pygame.mixer.Sound('quack.mp3')

def on_key_press(event):
    quack_sound.play()

keyboard.on_press(on_key_press)

keyboard.wait()
