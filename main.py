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

    while states['state'] == consts.STATE_RUNNING:
        handle_user()

        screen.draw_screen(game_field.field)

        # If the player lost or won, it prints a screen and then closes the game screen
        # if game_field.flag_contact(soldier.get_upper_body()):
        #     states['state'] = consts.STATE_WON
        #     screen.draw_win_screen()
        #     sleep(3)
        # if game_field.mine_contact(soldier.get_feet()):
        #     states['state'] = consts.STATE_LOST
        #     screen.draw_lose_screen()
        #     sleep(3)



def handle_user():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

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
    pygame.time.delay(100)


if __name__ == '__main__':
    # game_field.create()
    # game_field.print_field()
    main()
