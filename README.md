# 10c-cpt-brandon
10c-cpt-brandon created by GitHub Classroom

import arcade

WIDTH = 1360
HEIGHT = 700

p1_x = 100
p1_y = 100

p2_x = 1260
p2_y = 100


bullet2_x = p2_x
bullet2_y = p2_y

p1current_health = 50

space_pressed = False

bullet1_speed = 0

q_pressed = False

p1_up = False
p1_down = False
p1_left = False
p1_right = False

p2_up = False
p2_down = False
p2_left = False
p2_right = False

player1_alive = True

player1_health = 5

player2_alive = True

player2_health = 5

current_screen = 'menue'

def menue_screen(screen):
    arcade.draw_text('unreal tournement 2019', WIDTH / 2 - 250, HEIGHT / 2 + 200, arcade.color.ORANGE, 30),
    arcade.draw_text('instructions',WIDTH/2 - 150,HEIGHT/2 - 200,arcade.color.ORANGE,30),
    arcade.draw_text('play',WIDTH/2 - 85,HEIGHT/2,arcade.color.ORANGE,30)

def player1_healthbar(health):
    arcade.draw_xywh_rectangle_filled(0,HEIGHT,p1current_health,-20,arcade.color.GREEN)









player_1 =  arcade.draw_xywh_rectangle_filled(p1_x,p1_y,20,50,arcade.color.BLUE),\
            arcade.draw_circle_filled(p1_x + 10,p1_y,20,arcade.color.BLACK),\
            arcade.draw_xywh_rectangle_filled(p1_x+20,p1_y+30,10,5,arcade.color.BLACK)

player1_halthbar =  arcade.draw_xywh_rectangle_filled(0,HEIGHT,50,-20,arcade.color.GREEN)

menue = arcade.draw_text('unreal tournement 2019',WIDTH/2,HEIGHT/2,arcade.color.ORANGE,30)



player_2 = arcade.draw_xywh_rectangle_filled(p2_x,p2_y,20,50,arcade.color.RED),\
           arcade.draw_circle_filled(p2_x + 10,p2_y+ 50,20,arcade.color.BLACK),\
           arcade.draw_xywh_rectangle_filled(p2_x,p2_y+30,10,5,arcade.color.BLACK)




def update(delta_time):
    global p2_y
    global p2_x
    global p2_up
    global p2_down
    global p2_right
    global p2_left
    global bullet_list1
    global bullet_list2
    global p1_y
    global p1_x
    global p1_up
    global p1_down
    global p1_right
    global p1_left
    global player1_alive
    global player1_health
    global player2_alive
    global player2_health

    if current_screen == 'menue':
        player1_health = 5
        player1_alive = True
        player2_health = 5
        player2_alive = True



    if p2_up == True:
        p2_y += 7

    if p2_down == True:
        p2_y -= 7

    if p2_left == True:
        p2_x -= 7

    if p2_right == True:
        p2_x += 7

    if p1_up == True:
        p1_y += 7

    if p1_down == True:
        p1_y -= 7

    if p1_left == True:
        p1_x -= 7

    if p1_right == True:
        p1_x += 7

    for bullet1 in bullet_list1:
        bullet1[0] -= 20
        bullet1[1] += 0

    for bullet1 in bullet_list1:
        if bullet1[0] in range (p1_x, p1_x + 20) and  bullet1[1] in range (p1_y -20 , p1_y + 50 ):
            player1_health -= 1

    if player1_health == 0:
        player1_alive = False

    for bullet2 in bullet_list2:
        if bullet2[0] in range(p2_x, p2_x + 20) and bullet2[1] in range(p2_y - 20, p2_y + 50):
            player2_health -= 1

    if player2_health == 0:
        player2_alive = False

    for bullet2 in bullet_list2:
        bullet2[0] += 20
        bullet2[1] += 0







def on_draw():
        global bullet_list1
        global bullet_list2

        arcade.start_render()

        player1_healthbar(player1_halthbar)



        if current_screen == 'Game':
            if player1_alive == True:
                draw_player1(player_1)
            if player2_alive == True:
                draw_player2(player_2)
            arcade.set_background_color(arcade.color.WHITE)

        if current_screen == 'menue':
            menue_screen(menue)
            arcade.set_background_color(arcade.color.BLACK)


        if current_screen == 'Game':
            if player1_alive == True:
                for bullet1 in bullet_list1:
                    arcade.draw_xywh_rectangle_filled(bullet1[0], bullet1[1] + 20, 40, 5, arcade.color.RED)

            if player2_alive == True:
                for bullet2 in bullet_list2:
                    arcade.draw_xywh_rectangle_filled(bullet2[0] - 10,bullet2[1] + 20, 40, 5, arcade.color.BLUE)


            if player2_alive == False:
                arcade.draw_xywh_rectangle_filled(0,0,WIDTH,HEIGHT,arcade.color.BLACK)
                arcade.draw_text('player 1 wins',WIDTH/2 - 250,HEIGHT/2,arcade.color.RED,30)

            elif player1_alive == False:
                arcade.draw_xywh_rectangle_filled(0,0,WIDTH,HEIGHT,arcade.color.BLACK)
                arcade.draw_text('player 2 wins', WIDTH/2 - 250, HEIGHT / 2, arcade.color.RED,30)





def on_key_press(key, modifiers):
    global space_pressed
    global q_pressed
    global bullet_list1
    global bullet_list2
    global p2_y
    global p2_x
    global p2_up
    global p2_down
    global p2_right
    global p2_left
    global p1_y
    global p1_x
    global p1_up
    global p1_down
    global p1_right
    global p1_left
    global current_screen

    if key == arcade.key.ESCAPE:
        current_screen = 'menue'

    if key == arcade.key.P:
        current_screen = 'Game'


    if current_screen == 'Game':
        if key == arcade.key.SPACE:
            bullet_list1.append([p2_x,p2_y])
        if key == arcade.key.Q:
            bullet_list2.append([p1_x,p1_y])

        if key == arcade.key.Q:
            q_pressed = True

        if key == arcade.key.W:
            p1_up = True
        if key == arcade.key.S:
            p1_down = True
        if key == arcade.key.A:
            p1_left = True
        if key == arcade.key.D:
            p1_right = True

        if key == arcade.key.UP:
            p2_up = True
        if key == arcade.key.DOWN:
            p2_down = True
        if key == arcade.key.LEFT:
            p2_left = True
        if key == arcade.key.RIGHT:
            p2_right = True




def on_key_release(key, modifiers):
    global space_pressed
    global q_pressed
    if key == arcade.key.SPACE:
        space_pressed = False

    if key == arcade.key.Q:
        q_pressed = False
    global p1_y
    global p1_x
    global p1_up
    global p1_down
    global p1_right
    global p1_left
    global p2_y
    global p2_x
    global p2_up
    global p2_down
    global p2_right
    global p2_left
    if key == arcade.key.UP:
        p2_up = False
    if key == arcade.key.DOWN:
        p2_down = False
    if key == arcade.key.LEFT:
        p2_left = False
    if key == arcade.key.RIGHT:
        p2_right = False

    if key == arcade.key.W:
        p1_up = False
    if key == arcade.key.S:
        p1_down = False
    if key == arcade.key.A:
        p1_left = False
    if key == arcade.key.D:
        p1_right = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    global bullet_list1
    bullet_list1 = []

    global bullet_list2
    bullet_list2 = []

    arcade.run()






def draw_player1(player):
    arcade.draw_xywh_rectangle_filled(p1_x, p1_y, 20, 50, arcade.color.BLUE), \
    arcade.draw_circle_filled(p1_x + 10, p1_y +50 , 20, arcade.color.BLACK), \
    arcade.draw_xywh_rectangle_filled(p1_x +20 , p1_y + 20, 10, 5, arcade.color.BLACK)


def draw_player2(player):
    arcade.draw_xywh_rectangle_filled(p2_x, p2_y, 20, 50, arcade.color.RED), \
    arcade.draw_circle_filled(p2_x + 10, p2_y + 50, 20, arcade.color.BLACK), \
    arcade.draw_xywh_rectangle_filled(p2_x - 10, p2_y + 20, 10, 5, arcade.color.BLACK)

def player1_movement_press(key):
    global p1_y
    global p1_x
    global p1_up
    global p1_down
    global p1_right
    global p1_left
    if key == arcade.key.UP:
        p1_up = True
    if key == arcade.key.DOWN:
        p1_down = True
    if key == arcade.key.LEFT:
        p1_left = True
    if key == arcade.key.RIGHT:
        p1_right = True

def player1_movement_release(key):
    global p1_y
    global p1_x
    global p1_up
    global p1_down
    global p1_right
    global p1_left
    if key == arcade.key.UP:
        p1_up = False
    if key == arcade.key.DOWN:
        p1_down = False
    if key == arcade.key.LEFT:
        p1_left = False
    if key == arcade.key.RIGHT:
        p1_right = False




if __name__ == '__main__':
    setup()
