from random import randint
from time import time
import pygame, sys, os
from tkinter import Tk, Text, Label, Button, END
try: from Data.colors import all_colors as ac
except: 
    print('You can`t open this file!!!')
    quit()


path = os.path.abspath(os.path.dirname(sys.argv[0]))
size = 700
score = 0
cub_score = 0

def ps():
    '''
    Plaform slash.
    '''
    import platform
    if platform.system() == 'Windows':
        a = '\\'
    else:
        a = '/'
    del platform
    return a
ps = ps()
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

def message(msg, color, x_coor = 0, y_coor = 0, font_size = 'small'):
    if x_coor == 0 and y_coor == 0:
        text_surf, text_rect = text_object(msg, get_color(color), font_size)
        text_rect.center = (size/2), ( size/2)
        game_display.blit(text_surf, text_rect)
    else:
        text_surf, text_rect = text_object(msg, get_color(color), font_size)
        text_rect.center = (x_coor), (y_coor)
        game_display.blit(text_surf, text_rect)

def game_init():
    global clock, smallfont, medfont, largefont, game_display, img, red_img, nimiq_img, background
    try:
        log('initialization game...')
        
        pygame.init()
        pygame.display.set_caption('Kyky')
        game_display = pygame.display.set_mode((size, size))
        timer = time()
        
        log('initialization skin`s...')
        background = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  ps+'Data'+ps+'space.jpg')
        img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  ps+'Data'+ps+'rocket.png')
        red_img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  ps+'Data'+ps+'red_rocket.png')
        nimiq_img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) +  ps+'Data'+ps+'mini_nimiq.png')
        log('skin`s initialization complete!')

        log('initialization fonts...')
        clock = pygame.time.Clock()
        if ps == '/': smallfont = pygame.font.SysFont(None, calc_fonts('small'))
        else: smallfont = pygame.font.SysFont('Comic Sans MS', calc_fonts('small'))
        medfont = pygame.font.SysFont('Comic Sans MS', calc_fonts('med'))
        largefont = pygame.font.SysFont('Comic Sans MS', calc_fonts('large'))
        log('fonts initialization complete!')
    except Exception as e: 
        log('game initialization faild!')
        log(e)
        my_exit()

def calc_fonts(font_size = None):
    if font_size == None or font_size == 'small':
        return int(size/29)
    elif font_size == 'med':
        return int(size/19)
    elif font_size == 'large':
        a = size/2
        return int(size/8)
        
    

def space_button_click():
    global player_i, mode, snake_speed, min_cub_move_speed, max_cub_move_speed, two_player_i
    
    player_i = f_textBox.get(1.0, END + "-1c")
    two_player_i = s_textBox.get(1.0, END + "-1c")

    if len(player_i.strip()) != 0:
        log('loading game...')
        log(player_i)
        log(two_player_i)
        if str_mode == 'One player':
            max_cub_move_speed = 10
            min_cub_move_speed = -10
            snake_speed = 10
            mode = 'One player'
            log(mode)
            window.destroy()
            game_init()
                
        elif str_mode == 'Two player`s':
            max_cub_move_speed = 10
            min_cub_move_speed = -10
            snake_speed = 4
            mode = 'Two player`s'
            log(mode)
            window.destroy()
            game_init()
    else:
        log('No name!')
        w_label.config(text = 'No name!!!')

           
def btn_mode_click():
    global str_mode
    if str_mode == 'One player':
        str_mode = 'Two player`s'
        distroy_all_win()
        create_all_win('t')
    else:
        str_mode = 'One player'
        distroy_all_win()
        create_all_win()
    try: s_textBox.insert('1.0', 'AI')
    except: print
        
    f_textBox.insert('1.0', 'Kyky')
    btn_mode.configure(text=str_mode)

def main_window():
    global window, str_mode
    
    log('loading interface...')

    window = Tk()
    window.title('Ky')
    str_mode = 'One player'

    create_all_win()
   
    f_textBox.insert('1.0', 'Kyky')
    s_textBox.insert('1.0', 'Ade_Caro')
    log('interface load complete!')
    
    window.mainloop()

def create_all_win(mode = 's'):
    global f_label, f_textBox, s_textBox, s_label
    global close_btn, w_label, str_mode, btn_mode, mode_label
    global help_label2, space_btn, close_btn, help_label1

    
    w_label = Label(window, text='')
    label = Label(window, text='               What is you name?              ')
    f_label = Label(window, text='First player.')
    f_textBox = Text(window, width=10, height=1)
    s_label = Label(window, text = 'Second player.')
    s_textBox = Text(window, width=10, height=1)

    mode_label = Label(window, text='Select game mode:')
    help_label1 = Label(window, text='One player, ')
    help_label2 = Label(window, text='Two player`s.')
    btn_mode = Button(window, text=str_mode, command=btn_mode_click)

    space_btn = Button(window, text='Go to Mining Nimiq (beta)', command = space_button_click)
    close_btn = Button(window, text='Exit', command=my_exit)

    w_label.pack()
    f_label.pack()
    f_textBox.pack()
    if mode == 't':
        s_label.pack()
        s_textBox.pack()
    mode_label.pack()
    help_label1.pack()
    help_label2.pack()
    btn_mode.pack()
    space_btn.pack()
    close_btn.pack()

def distroy_all_win():
    global f_label, f_textBox, s_textBox, s_label
    global close_btn, w_label, str_mode, btn_mode, mode_label
    global help_label2, space_btn, close_btn, help_label1
    
    w_label.destroy()
    f_label.destroy()
    f_textBox.destroy()
    try:
        s_label.destroy()
        s_textBox.destroy()
    except: print
    mode_label.destroy()
    help_label1.destroy()
    help_label2.destroy()
    btn_mode.destroy()
    space_btn.destroy()
    close_btn.destroy()
    del w_label, f_label, f_textBox, mode_label, help_label1, help_label2, btn_mode, space_btn, close_btn

    

def save():
    if mode == 'One player':   
        if score > cub_score:
            game_display.fill(get_color('white'))
            msg = 'You WIN!!!'
        elif score < cub_score:
            game_display.fill(get_color('black'))
            msg = 'You lose.'
        else: msg = 'Tie'
    else:
        if cub_score > score: msg = two_player_i + ' WIN!'    
        elif cub_score < score: msg = player_i + ' WIN!'      
        else: msg = 'TIE!!!'
                    
    message(msg, 'gold')
    pygame.display.update()
    clock.tick(2)
    log('Saving...')
    game_display.fill(get_color('blue'))
    message('Closing the game... Your score: ' + str(score) + ', ' + two_player_i + '`s score: ' + str(cub_score), 'white')
    pygame.display.update()
    clock.tick(2)
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + ps+'Score.txt'
    log(path)
    write(
        'Last ' + player_i + '`s' + ' score: ' + str(score) + ', '+ two_player_i +'`s score: ' + str(cub_score) + '\n', 'Score.txt')
    log('Saved')
    
def draw_nimiq(x_nimiq, y_nimiq):
    game_display.blit(nimiq_img, (x_nimiq, y_nimiq))
    
    
def my_exit():
    try:
        log('exiting...')
        try: 
            window.destroy()
            log('window is destroyed.')
        except:
            log('window is alerty destroyed.')
        pygame.quit()
        log('exit complete!')
        quit()
    except:
        print('Error on exit')
        quit()

def boom(x, y): 
    img = pygame.image.load(os.path.abspath(os.path.dirname(sys.argv[0])) + ps+'Data'+ps+'boom.png' ) 
    game_display.blit(img, [x, y])
        
    
def log(msg):
    try:
        log_file =  ps+'Data'+ps+'log.txt'
        print(msg)
        write(str(msg), log_file)
        write('\r\n', log_file)
    except Exception as e: 
        print('Error in log!: ')
        print(str(e))
        my_exit()
def get_color(colo_r):
    color_code = str(ac.get(colo_r))
    color_code = str(color_code[1:])
    color = tuple(int(color_code[i:i+2], 16) for i in (0, 2 ,4))
    return color

def is_file(file, current_path = True):
    if current_path: a = os.path.isfile(path+ps+file)
    else: a = os.path.isfile(file)
    return a

def write(text, file_name = 'Temp.py'):
    if is_file(file_name):
        f = open(path+ps+file_name, 'a')
    elif not is_file(file_name):
        f = open(path+ps+file_name, 'w')
    f.write(text)
    f.close()
    del f

def restart():
    log('Restarting...')
    save()
    pygame.quit()
    main_window()
    
main_window()  
