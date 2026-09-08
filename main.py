import sys
from time import sleep

import pygame

import consts
import screen
import soldier
import game_field

states = {
    "state": consts.STATE_RUNNING,
}

def main():
    pygame.init()
    pygame.display.set_caption('Kaboom')
    game_field.create()
    soldier.create()
    clock = pygame.time.Clock()

    while states['state'] == consts.STATE_RUNNING:
        pygame.time.delay(50)

        handle_user()

        screen.draw_screen(game_field.field, soldier.position['y'], soldier.position['x'])

        # If the player lost or won, it prints a screen and then closes the game screen
        if game_field.flag_contact(soldier.get_upper_body()):
            states['state'] = consts.STATE_WON
            print('won!')
            screen.screen_win()
            sleep(3)
        if game_field.mine_contact(soldier.get_feet()):
            states['state'] = consts.STATE_LOST
            print('lose!')
            screen.screen_lose()
            sleep(3)

        clock.tick(60)



def handle_user():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        screen.draw_mines(game_field.field)
        sleep(1)
    else:
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
