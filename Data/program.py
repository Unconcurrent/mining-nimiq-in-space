from random import randint
import pygame, sys, os
from tkinter import Tk, Text, Label, Button, END
try: from Data.colors import all_colors as ac
except: 
    print('You can`t open this file!!!')
    exit()


path = os.path.abspath(os.path.dirname(sys.argv[0]))
size = 800
blue = (100, 100, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
brun = (170, 85, 0)
orange = (255, 72.8, 36.4)
purple = (51, 0, 255)

def player(def_player):
    screen_text = smallfont.render(str(def_player), True, white)
    game_display.blit(screen_text, [350, 10])
    pygame.display.update()


def car_move(direction, x, y):
    try:
        if direction == 'right':
            car = pygame.transform.rotate(img, 270)
        elif direction == 'left':
            car = pygame.transform.rotate(img, 90)
        elif direction == 'up':
            car = img
        elif direction == 'down':
            car = pygame.transform.rotate(img, 180)
            
        elif direction == 'right-up':
            car = pygame.transform.rotate(img, 320)
        elif direction == 'right-down':
            car = pygame.transform.rotate(img, 220)
        elif direction == 'left-up':
            car = pygame.transform.rotate(img, 40)
        elif direction == 'left-down':
            car = pygame.transform.rotate(img, 140)

        game_display.blit(car, (x, y))
    except: space_button_click()
    
def red_car_move(red_direction, cub_x, cub_y):
    if red_direction == 'right':
        red_head = pygame.transform.rotate(red_img, 270)
    elif red_direction == 'left':
        red_head = pygame.transform.rotate(red_img, 90)
    elif red_direction == 'up':
        red_head = red_img
    elif red_direction == 'down':
        red_head = pygame.transform.rotate(red_img, 180)
        
    elif red_direction == 'right-up':
        red_head = pygame.transform.rotate(red_img, 320)
    elif red_direction == 'right-down':
        red_head = pygame.transform.rotate(red_img, 220)
    elif red_direction == 'left-up':
        red_head = pygame.transform.rotate(red_img, 40)
    elif red_direction == 'left-down':
        red_head = pygame.transform.rotate(red_img, 140)
        
    game_display.blit(red_head, (cub_x, cub_y))  

def text_object(text, color, font_size):
    if font_size == 'small':
        text_sulrface = smallfont.render(text, True, color)
    elif font_size == 'med':
        text_sulrface = medfont.render(text, True, color)
    elif font_size == 'large':
        text_sulrface = largefont.render(text, True, color)
    return text_sulrface, text_sulrface.get_rect()

def message(msg, color, font_size = 'small', x_coor = 0, y_coor = 0):
    if x_coor == 0 and y_coor == 0:
        text_surf, text_rect = text_object(msg, get_color(color), font_size)
        text_rect.center = (size/2), ( size/2)
        game_display.blit(text_surf, text_rect)
    else:
        text_surf, text_rect = text_object(msg, get_color(color), font_size)
        text_rect.center = (x_coor), (y_coor)
        game_display.blit(text_surf, text_rect)
    pygame.display.update()


def cub_score_message(cub_score):
    screen_text = smallfont.render(two_player_i + '`s score: ' + str(cub_score), True, white)
    game_display.blit(screen_text, [630, 10])
    pygame.display.update()


def player_score(def_player, score):
    screen_text = smallfont.render(def_player + '`s score: ' + str(score), True, white)
    game_display.blit(screen_text, [10, 10])
    pygame.display.update()


def game_init():
    global clock, smallfont, medfont, largefont, game_display, img, red_img, nimiq_img, background
    try:
        log('initialization game...')
        
        pygame.init()
        pygame.display.set_caption('Kyky')
        
        log('initialization skin`s...')
        background = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  '\\Data\\space.jpg')
        img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  '\\Data\\rocket.png')
        red_img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  '\\Data\\red_rocket.png')
        nimiq_img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  '\\Data\\mini_nimiq.png')
        log('skin`s initialization complete!')
        
        clock = pygame.time.Clock()
        smallfont = pygame.font.SysFont('Comic Sans MS', 17)
        medfont = pygame.font.SysFont('Comic Sans MS', 50)
        largefont = pygame.font.SysFont('Comic Sans MS', 80)
        game_display = pygame.display.set_mode((size, size))
    except: 
        log('game initialization faild!')


def space_button_click():
    global player_i, mode, snake_speed, min_cub_move_speed, max_cub_move_speed, two_player_i
    log('loading game...')
    
    player_i = textBox.get(1.0, END + "-1c")
    two_player_i = two_textBox.get(1.0, END + "-1c")

    log(player_i)

    if str_mode == 'One player':
        max_cub_move_speed = 10
        min_cub_move_speed = -10
        snake_speed = 10
        mode = 'One player'
        log(mode)
        if len(player_i.strip()) != 0:
            window.destroy()
            game_init()
            
    elif str_mode == 'Two player`s':
        max_cub_move_speed = 10
        min_cub_move_speed = -10
        snake_speed = 4
        mode = 'Two player`s'
        log(mode)
        if len(player_i.strip()) != 0:
            window.destroy()
            game_init()
    else:
        log('no name!')

           
def btn_mode_click():
    global str_mode
    if str_mode == 'One player':
        str_mode = 'Two player`s'
    else:
        str_mode = 'One player'

    btn_mode.configure(text=str_mode)


def main_window():
    global label, textBox, window, two_textBox
    global close_btn, w_label, str_mode, btn_mode
    
    log('loading interface...')

    window = Tk()
    window.title('Ky')
    str_mode = 'One player'

    w_label = Label(window, text='You need a name.')
    label = Label(window, text='               What is you name?              ')
    textBox = Text(window, width=10, height=1)
    two_textBox = Text(window, width=10, height=1)

    mode_label = Label(window, text='Select game mode:')
    help_label1 = Label(window, text='One player, ')
    help_label2 = Label(window, text='Two player`s.')
    btn_mode = Button(window, text=str_mode, command=btn_mode_click)

    space_btn = Button(window, text='Go to Mining Nimiq (beta)', command = space_button_click)
    close_btn = Button(window, text='Exit', command=my_exit)

    w_label.pack()
    label.pack()
    textBox.pack()
    two_textBox.pack()
    mode_label.pack()
    help_label1.pack()
    help_label2.pack()
    btn_mode.pack()
    space_btn.pack()
    close_btn.pack()    
   
    textBox.insert('1.0', 'Kyky')
    two_textBox.insert('1.0', 'Ade_Caro')
    log('interface load complete!')
    
    window.mainloop()

def save_exit(player_i, save_score, two_player_i, save_cub_score):
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\Data\\Score.txt'
    log(path)
    f = open(path, "w")
    f.write(
        'Last ' + player_i + '`s' + ' score: ' + str(save_score) + ', '+ two_player_i +'`s score: ' + str(save_cub_score) + '\n')
    f.close()
    my_exit()
    
def draw_nimiq(x_nimiq, y_nimiq):
    game_display.blit(nimiq_img, (x_nimiq, y_nimiq))
    
    
def my_exit(code = 0):
    log('exiting...')
    try: 
        window.destroy()
        log('window is destroyed.')
    except:
        log('window is alerty destroyed.')
    pygame.quit()
    log('exit complete!')
    exit(int(code))

def boom(player, x, y): 
    if player == player_i: 
        img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) + '\\Data\\boom.png' ) 
        game_display.blit(img, [x, y])
    elif player == two_player_i:
        img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) + '\\Data\\boom.png')
        game_display.blit(img, [x, y])
    pygame.display.update()
    clock.tick(10)
    
def log(msg):
    try:
        log_file = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\Data\\log.txt'
        print(msg)
        if os.path.isfile(log_file) == False:
            f = open(log_file, 'w+', 1)
            f.write(str(msg))
            f.write('\r\n')
            f.close()
        else:
            f = open(log_file, 'a')
            f.write(str(msg))
            f.write('\r\n')
            f.close()
    except: 
        print('Error you can`t open this file!')
        quit()
def get_color(colo_r):
    color_code = str(ac.get(colo_r))
    color_code = str(color_code[1:])
    color = tuple(int(color_code[i:i+2], 16) for i in (0, 2 ,4))
    return color

    
main_window()  