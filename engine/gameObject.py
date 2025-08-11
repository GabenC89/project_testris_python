import pygame

class GameObject:

    def __init__(self, pos_x, pos_y, width, height, image_path = None, fill_color = (0,0,0)):
        if image_path != None:
            image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(image, (width, height))
        
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height