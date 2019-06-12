import arcade

WIDTH = 1360
HEIGHT = 700

p1_reload_time = False

p2_reload_time = False


p1_x = 100
p1_y = 100

p2_x = 1260
p2_y = 600

p1_mag = 10

p2_mag = 10

RCTRL_pressed = False

G_pressed = False


bullet2_x = p2_x
bullet2_y = p2_y

p1gun_x = 100

p2gun_x = 1260



p1current_health = 100

p2current_health = -100

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
    arcade.draw_text('press i for instructions',WIDTH/2 - 200,HEIGHT/2 - 200,arcade.color.ORANGE,30),
    arcade.draw_text('press p to play',WIDTH/2 - 150,HEIGHT/2,arcade.color.ORANGE,30)

def player1_healthbar(health):
    arcade.draw_xywh_rectangle_filled(0, HEIGHT, 100, -20, arcade.color.RED),
    arcade.draw_xywh_rectangle_filled(0,HEIGHT,p1current_health,-20,arcade.color.GREEN),
    arcade.draw_text('player2',0,HEIGHT - 35,arcade.color.BLACK)

def player2_healthbar(health):
    arcade.draw_xywh_rectangle_filled(WIDTH,HEIGHT,-100,-20,arcade.color.RED),
    arcade.draw_xywh_rectangle_filled(WIDTH,HEIGHT,p2current_health,-20,arcade.color.GREEN),
    arcade.draw_text('player1',WIDTH-60,HEIGHT- 35,arcade.color.BLACK)

def instruction_screen(instructions):
    arcade.draw_text('for player 2 use WASD keys to move. for player 1 use the arrow keys',0,HEIGHT/1.5,arcade.color.BLACK,25),
    arcade.draw_text('for player 2 you fire with g. for player 1 you fire with RCTRL',0,HEIGHT/1.9,arcade.color.BLACK,25),
    arcade.draw_text('if your health gets too low you disapear',0,HEIGHT/2.3,arcade.color.BLACK,25)
    arcade.draw_text('have fun',0,HEIGHT/2.7,arcade.color.BLACK,25)












player_1 =  arcade.draw_xywh_rectangle_filled(p1_x,p1_y,20,50,arcade.color.BLUE),\
            arcade.draw_circle_filled(p1_x + 10,p1_y,20,arcade.color.BLACK),\
            arcade.draw_xywh_rectangle_filled(p1_x+20,p1_y+30,10,5,arcade.color.BLACK)

player1_halthbar =  arcade.draw_xywh_rectangle_filled(0,HEIGHT,50,-20,arcade.color.GREEN)

menue = arcade.draw_text('unreal tournement 2019',WIDTH/2,HEIGHT/2,arcade.color.ORANGE,30)

player2_halthbar = arcade.draw_xywh_rectangle_filled(WIDTH,HEIGHT,-50,-20,arcade.color.GREEN)


player_2 = arcade.draw_xywh_rectangle_filled(p2_x,p2_y,20,50,arcade.color.RED),\
           arcade.draw_circle_filled(p2_x + 10,p2_y+ 50,20,arcade.color.BLACK),\
           arcade.draw_xywh_rectangle_filled(p2_x,p2_y+30,10,5,arcade.color.BLACK)

instructions = arcade.draw_text('for player1 use WASD keys to move. for player 2 use the arrow keys',WIDTH/2,HEIGHT/2,arcade.color.BLACK,30)


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
    global p1current_health
    global p2current_health
    global current_screen
    global p1gun_x
    global p2gun_x
    global WIDTH
    global p1_reload_time
    global p2_reload_time
    global p1_mag
    global p2_mag

    if current_screen == 'menue':
        player1_health = 5
        p1current_health = 100
        player1_alive = True
        player2_health = 5
        p2current_health = -100
        player2_alive = True

    if current_screen == 'Instructions':
        player1_alive = True

    if p1_reload_time == True and p1_mag <= 10:
        p1_mag += 0.1

    if p2_reload_time == True and p2_mag <= 10:
        p2_mag += 0.1


    if p2_up == True:
        p2_y += 7

    if p2_y >= 645:
         p2_up = False

    if p2_down == True:
        p2_y -= 7

    if p2_y <= 0:
        p2_down = False

    if p2_left == True:
        p2_x -= 7

    if p2_x <=0:
        p2_left = False


    if p2_right == True:
        p2_x += 7

    if p2_x >=1350:
        p2_right = False

    if p2_x <=WIDTH/2:
        p2_left = False

    if p1_up == True:
        p1_y += 7

    if p1_y >= 645:
         p1_up = False

    if p1_down == True:
        p1_y -= 7

    if p1_y <= 0:
        p1_down = False

    if p1_left == True:
        p1_x -= 7

    if p1_x <=0:
        p1_left = False

    if p1_right == True:
        p1_x += 7

    if p1_x >=WIDTH/2:
        p1_right = False

    for bullet1 in bullet_list1:
        bullet1[0] -= 20
        bullet1[1] += 0

        if bullet1[0] == -15:
            del bullet_list1[0]




    for bullet1 in bullet_list1:
        if bullet1[0] in range (p1_x, p1_x + 20) and  bullet1[1] in range (p1_y -20 , p1_y + 50 ) and current_screen == 'Game':
            player1_health -= 1
            p1current_health -= 20







    if player1_health == 0:
        player1_alive = False

    for bullet2 in bullet_list2:
        if bullet2[0] in range(p2_x, p2_x + 20) and bullet2[1] in range(p2_y - 20, p2_y + 50) and current_screen == 'Game':
            player2_health -= 1
            p2current_health += 20

    if player2_health == 0:
        player2_alive = False

    for bullet2 in bullet_list2:
        bullet2[0] += 20
        bullet2[1] += 0

        if bullet2[0] == 1360:
            del bullet_list2[0]

    if current_screen == 'end':
        p1current_health = 100
        p2current_health = -100

    if player1_alive == False or player2_alive == False:
        current_screen = 'end'










def on_draw():
        global bullet_list1
        global bullet_list2
        global p1_x
        global p1_y
        global p2_x
        global p2_y
        global RCTRL_pressed


        arcade.start_render()
        if current_screen == 'Game':
            player1_healthbar(player1_halthbar)
            arcade.draw_text('current mag:{}'.format(p1_mag //1),1235,650,arcade.color.BLACK)
            player2_healthbar(player2_halthbar)
            arcade.draw_text('current mag:{}'.format(p2_mag//1), 0, 650, arcade.color.BLACK)

        if current_screen == 'Instructions':
            instruction_screen(instructions)
            arcade.set_background_color(arcade.color.WHITE)
            draw_player1(player_1)
            draw_player2(player_2)
            for bullet1 in bullet_list1 :
                arcade.draw_xywh_rectangle_filled(bullet1[0], bullet1[1] + 20, 40, 5, arcade.color.RED),




            for bullet2 in bullet_list2:
                arcade.draw_xywh_rectangle_filled(bullet2[0] - 10, bullet2[1] + 20, 40, 5, arcade.color.BLUE)

        if current_screen == 'Game':
            if player1_alive == True:
                draw_player1(player_1)
            if player2_alive == True:
                draw_player2(player_2)
            arcade.set_background_color(arcade.color.WHITE)

        if current_screen == 'menue':
            menue_screen(menue)
            arcade.set_background_color(arcade.color.BLACK)
            p1_x = 100
            p1_y = 100

            p2_x = 1260
            p2_y = 500


        if current_screen == 'Game':
            if player1_alive == True:
                for bullet1 in bullet_list1:
                    arcade.draw_xywh_rectangle_filled(bullet1[0], bullet1[1] + 20, 40, 5, arcade.color.RED)

            if player2_alive == True:
                for bullet2 in bullet_list2:
                    arcade.draw_xywh_rectangle_filled(bullet2[0] - 10,bullet2[1] + 20, 40, 5, arcade.color.BLUE)

        if current_screen == 'end':
            if player2_alive == False:
                arcade.draw_xywh_rectangle_filled(0,0,WIDTH,HEIGHT,arcade.color.BLACK)
                arcade.draw_text('Blue wins press Escape to go to menu',WIDTH/2 -100 - 250,HEIGHT/2,arcade.color.RED,30)

            if player1_alive == False:
                arcade.draw_xywh_rectangle_filled(0,0,WIDTH,HEIGHT,arcade.color.BLACK)
                arcade.draw_text('Red wins press Escape to go to menu', WIDTH/2 - 100 - 250, HEIGHT / 2, arcade.color.RED,30)





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
    global RCTRL_pressed
    global G_pressed
    global p1_mag
    global p2_mag
    global p1_reload_time
    global p2_reload_time

    if key == arcade.key.ESCAPE:
        current_screen = 'menue'
        p1_mag = 10
        p2_mag = 10

    if key == arcade.key.P and current_screen == 'menue' :
        current_screen = 'Game'
    if key == arcade.key.I:
        current_screen = 'Instructions'


    if current_screen == 'Game' or current_screen == 'Instructions':
        if key == arcade.key.RCTRL and p1_mag >=1 and p1_reload_time == False:
            bullet_list1.append([p2_x,p2_y])
            p1_mag -= 1


        if key == arcade.key.R and p2_mag !=10 :
            p2_reload_time = True


        if key == arcade.key.G and p2_mag >= 1 and p2_reload_time == False:
            bullet_list2.append([p1_x,p1_y])
            p2_mag -= 1

        if key == arcade.key.RSHIFT and p1_mag != 10 :
           p1_reload_time = True

        if key == arcade.key.RCTRL:
            RCTRL_pressed = True

        if key == arcade.key.G:
            G_pressed = True

        if key == arcade.key.W :
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
    global RCTRL_pressed
    global G_pressed
    global p1_reload_time
    global p2_reload_time
    global p1_mag
    global p2_mag
    if key == arcade.key.RCTRL:
        RCTRL_pressed = False

    if key == arcade.key.G:
        G_pressed = False

    if key == arcade.key.R and p2_mag !=10:
        p2_reload_time = False

    if key == arcade.key.RSHIFT and p1_mag !=10 :
        p1_reload_time = False



    if key == arcade.key.UP :
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

    if key == arcade.key.SPACE:
        space_pressed = False

    if key == arcade.key.Q:
        q_pressed = False

    if p1_y == HEIGHT:
        p1_y -= 3


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
    global p1_x
    global p1_y
    arcade.draw_xywh_rectangle_filled(p1_x, p1_y, 20, 50, arcade.color.BLUE), \
    arcade.draw_circle_filled(p1_x  + 10, p1_y +50 , 20, arcade.color.BLACK), \
    arcade.draw_xywh_rectangle_filled( p1_x +20 , p1_y + 20, 10, 5, arcade.color.BLACK)


def draw_player2(player):
    global p2_x
    global p2_y
    arcade.draw_xywh_rectangle_filled(p2_x, p2_y, 20, 50, arcade.color.RED), \
    arcade.draw_circle_filled(p2_x + 10, p2_y + 50, 20, arcade.color.BLACK), \
    arcade.draw_xywh_rectangle_filled(p2_x  - 10, p2_y + 20, 10, 5, arcade.color.BLACK)





if __name__ == '__main__':
    setup()
