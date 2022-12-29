import pygame


class GameObject:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.collision = False

    def move(self, speed, objects):
        keys = pygame.key.get_pressed()
        new_x = self.x
        new_y = self.y
        if keys[pygame.K_w]:
            new_y -= speed
        if keys[pygame.K_s]:
            new_y += speed
        if keys[pygame.K_a]:
            new_x -= speed
        if keys[pygame.K_d]:
            new_x += speed

        rect1 = self.image.get_rect(topleft=(new_x, new_y))
        collision = False
        for object in objects:
            if object == self:
                continue
            rect2 = object.image.get_rect(topleft=(object.x, object.y))
            if rect1.colliderect(rect2):
                collision = True
                break

        if not collision:
            self.x = new_x
            self.y = new_y

    def render(self, surface, scale=1):
        scale_matrix = pygame.transform.scale(self.image, (32 * scale, 32 * scale))
        surface.blit(scale_matrix, (self.x, self.y))
