import pgzrun
# import pgzero.screen "si tu clique gauche +ctrl tu peux voir d'ou il l'import"


WIDTH = 800
HEIGHT = 600
center = [400, 300]




menu_visible = True
space_pressed = False

score = 0
all_bricks = []


for y in range (25,200, 30): #ou 0, 7 * 100, 30)
    for x in range(50, 750, 200):#ou 0, 8 * 100, 100)
        brick = Actor("brick_purple_lvl1", anchor = ["left", "top"])
        brick.pos = [x, y] #en haut a gauche
        all_bricks.append(brick)
for y in range ( 25,150,30):
    for x in range(150, 750,200):
        brick2 = Actor("brick_green_lvl1", anchor = ["left", "top"])
        brick2.pos = [x, y] #en haut a gauche
        all_bricks.append(brick2)


player = Actor("player_cyan_1")
player_2 = Actor("player_cyan_2")
player.pos = [WIDTH/2, 550]


def on_mouse_move(pos):
    player.x = pos[0]
ball = Actor("ball")
ball.pos = [WIDTH/2, 500]
ball_speed = [5, -5] # [X, Y]


def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1
def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1





##--Update--##


def update_menu():
    
    if not music.is_playing('bgs_contemplation2') and not ball.bottom >= HEIGHT:
        music.play("bgs_contemplation2")
        music.set_volume(0.1)
        

#--in_game--#

def update():
    
    
    global space_pressed, score, ball_speed
    if space_pressed == True:
        new_x = ball.pos[0] + ball_speed[0]
        new_y = ball.pos[1] + ball_speed[1]
        ball.pos = [new_x, new_y]
        if ball.right > WIDTH or ball.left < 0:
            invert_horizontal_speed()
        if ball.top < 0:
            invert_vertical_speed()
            
        


        if ball.colliderect(player):
            invert_vertical_speed()
            sounds.laserfire02.play()


            

    for brick in all_bricks or brick2 in all_bricks:
        if ball.colliderect(brick):
            sounds.sf_rock_brique_hit.play()
            all_bricks.remove(brick)
            invert_vertical_speed()
            score = score + 42
            
    if menu_visible == True:
        update_menu()
    else:
        update()

        
        



# --affichage--


# click_to_start
def on_mouse_down(pos, button):
    global bgs_title_visible
    if button == mouse.LEFT and start_button.collidepoint(pos):
        sounds.confirme.play()
        bgs_title_visible = False
bgs_title_visible = True


def draw():

    if bgs_title_visible == True:
        draw_menu()    
    else:
        draw_game()

## YOU WON
    if score == 1638:
        sounds.win.play()
        screen.clear()
        screen.draw.text("Congratulations, \n you found the meaning of life,\n the universe, and everything !", center=[WIDTH/2, HEIGHT/2],
                         color = "firebrick", gcolor= "papayawhip",owidth=0.25, ocolor="peachpuff", fontsize=40, fontname="magneto")
        screen.draw.text("Your score: " + str(score), (25,500),fontname="magneto", fontsize=40)
        return 
    

## YOU LOST
    if ball.bottom >= HEIGHT:
        sounds.death.play()
        music.stop()
        screen.clear()
        

        screen.draw.text("GAME \n OVER", center=[WIDTH/2, HEIGHT/2],color = "firebrick", gcolor= "papayawhip",owidth=0.25, ocolor="peachpuff", fontsize=72, fontname="magneto")
        game_over_img.draw()
        screen.draw.text("Your score: " + str(score), (25,500),fontname="magneto", fontsize=40)
        return 
        
game_over_img = Actor("rest_in_peperoni", center=(200,300))



##------TITLE-----##



bgs_title = Actor("bg_space_menu_v2", center=(400,300))
start_button = Actor("start_button_1", center=(400,350))


def draw_menu():
    screen.clear()
    bgs_title.draw()
    start_button.draw()
    screen.draw.text("Space", (594,539),fontname="magneto", fontsize=20)
    return   


##-----GAME-----##

def on_key_down(key):
    global space_pressed
    if key == keys.SPACE:
        space_pressed = True
        
bgs_game = Actor("bg5", center=(500,400))

def draw_game():
    screen.clear() 
    bgs_game.draw()
    for brick in all_bricks:    
        brick.draw()
     
    player.draw()
    ball.draw()

    screen.draw.text(str(score), (25,230),fontname="magneto", fontsize=40)
    return    



# Dernier ligne only ! 
pgzrun.go() 
# Dernier ligne only ! 
