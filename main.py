import pygame

import consts
import screen
import soldier
import game_field

states = {
    "state": 'running',
    'running': True,
}

def main():
    pygame.init()
    pygame.display.set_caption('Kaboom')
    game_field.create()

    while states['running']:
        handle_user()
        screen.draw_screen(game_field.field)


def handle_user():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            states['running'] = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        soldier.move(consts.MOVE_DOWN)
    if keys[pygame.K_UP]:
        soldier.move(consts.MOVE_UP)
    if keys[pygame.K_RIGHT]:
        soldier.move(consts.MOVE_RIGHT)
    if keys[pygame.K_LEFT]:
        soldier.move(consts.MOVE_LEFT)


if __name__ == '__main__':
    # game_field.create()
    # game_field.print_field()
    main()
