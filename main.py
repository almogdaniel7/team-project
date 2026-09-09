import sys
from time import sleep

import pygame

import consts
import database
import screen
import soldier
import game_field
# Rotem Dar 216360271
# Almog Daniel 217408707

states = {
    "state": consts.STATE_RUNNING,
}
key_press_timer = [0, 0]

def main():
    pygame.init()
    pygame.display.set_caption('Kaboom')
    game_field.create()
    soldier.create()
    clock = pygame.time.Clock()
    database.create_new_file()

    while states['state'] == consts.STATE_RUNNING:
        pygame.time.delay(50)

        handle_user()

        screen.draw_screen(game_field.field, soldier.position['row'], soldier.position['col'])

        # If the player lost or won, it prints a screen and then closes the game screen
        if game_field.flag_contact(soldier.get_upper_body()):
            states['state'] = consts.STATE_WON

            pygame.mixer.music.load(consts.WIN_SOUND)
            pygame.mixer.music.play()

            screen.screen_win()
            sleep(3)
        if game_field.mine_contact(soldier.get_feet()):
            states['state'] = consts.STATE_LOST

            pygame.mixer.music.load(consts.LOSE_SOUND)
            pygame.mixer.music.play()
            # Loop meant to wait until sound has finished playing
            while pygame.mixer.music.get_busy():
                pass
            pygame.mixer.music.load(consts.GAME_OVER_SOUND)
            pygame.mixer.music.play()

            screen.screen_lose()
            sleep(3)

        clock.tick(60)


def handle_user():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            num = event.unicode # get the unicode value of the key
            if '1' <= num <= '9': # check if the key is a digit between 1 and 9
                # saves the time when the key was pressed
                key_press_timer[0] = num
                key_press_timer[1] = pygame.time.get_ticks()

        if event.type == pygame.KEYUP: # detects when a key was released
            if key_press_timer[0] == event.unicode:
                # finds for how long the key was pressed
                time = pygame.time.get_ticks() - key_press_timer[1]
                # if pressed for more than a second, it is a long press then
                if time > 1000:
                    coordinates = database.extract_data(int(event.unicode))
                    if coordinates:
                        soldier.update_location(coordinates)
                else:
                    database.write_to_file(game_field.field, [soldier.position['row'], soldier.position['col']], int(event.unicode))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        screen.draw_mines(game_field.field, soldier.position['row'], soldier.position['col'])
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
    main()
