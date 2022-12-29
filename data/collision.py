import pygame


def check_collision(objects):
    for i, object1 in enumerate(objects):
        for object2 in objects[i + 1 :]:
            rect1 = object1.image.get_rect(topleft=(object1.x, object1.y))
            rect2 = object2.image.get_rect(topleft=(object2.x, object2.y))
            if rect1.colliderect(rect2):
                print("Kolizja między obiektami!", object1, object2)
