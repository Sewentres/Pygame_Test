import pygame


class GameObject:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= speed
        if keys[pygame.K_s]:
            self.y += speed
        if keys[pygame.K_a]:
            self.x -= speed
        if keys[pygame.K_d]:
            self.x += speed

    def check_collision(object1, object2):
        rect1 = object1.image.get_rect(topleft=(object1.x, object1.y))
        rect2 = object2.image.get_rect(topleft=(object2.x, object2.y))
        return rect1.colliderect(rect2)
