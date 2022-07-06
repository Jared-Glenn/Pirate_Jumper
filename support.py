import pygame
from os import walk

def import_folder(path):
    animation_list = []
    for _, __, img_file in walk(path):
        for image in img_file:
            image_path = path + '/' + image
            image_file = pygame.image.load(image_path).convert_alpha()
            animation_list.append(image_file)
    return animation_list

