from random import randint 
import pygame
from Data import program as p
from Data.program import size, player_i, two_player_i, min_cub_move_speed, max_cub_move_speed, game_display, mode, clock, snake_speed, background
p.log('lib load complete!')


def loop():
    global score, cub_score
    try:
        p.log('game load complete!')

        score = 0
        cub_score = 0
        direction = 'up'
        red_direction = 'up'
        pause = False

        x_nimiq = round(randint(0, size - 30) / 10.0) * 10.0
        y_nimiq = round(randint(0, size - 30) / 10.0) * 10.0

        x = size / 2
        y = size / 2
        x_cub = 500
        y_cub = 400
        x_change = 0
        y_change = 0
        x_change_cub = 0
        y_change_cub = 0

        speed = 5

        FPS = 30
        
        p.log('Enter in main loop.')

        game_exit = False
        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = - speed
                    elif event.key == pygame.K_DOWN:
                        y_change = speed
                    elif event.key == pygame.K_LEFT:
                        x_change = - speed
                    elif event.key == pygame.K_RIGHT:
                        x_change = speed                       
                    elif event.key == pygame.K_q: 
                        if pause:
                            pause = False
                            FPS = 30
                        else:
                            pause = True
                            FPS = 1
                    elif mode != 'One player':
                        if event.key == pygame.K_w:
                            y_change_cub = - speed
                        elif event.key == pygame.K_s:
                            y_change_cub = speed
                        elif event.key == pygame.K_a:
                            x_change_cub = - speed
                        elif event.key == pygame.K_d:
                            x_change_cub = speed
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
                    elif mode != 'One player':
                        if event.key == pygame.K_a or event.key == pygame.K_d:
                            x_change_cub = 0
                        elif event.key == pygame.K_w or event.key == pygame.K_s:
                            y_change_cub = 0
                                        
            if not pause:

                x_nimiq = randint(x_nimiq - 1, x_nimiq + 1)
                y_nimiq = randint(y_nimiq - 1, y_nimiq + 1)
                game_display.blit(background, [0, 0])

                
                if (y_change > 0 and x_change == 0):
                    direction = 'down'
                elif (y_change < 0 and x_change == 0):
                    direction = 'up'
                elif (y_change == 0 and x_change > 0):
                    direction = 'right'
                elif (y_change == 0 and x_change < 0):
                    direction = 'left'
                elif (y_change > 0 and x_change > 0):
                    direction = 'right-down'
                elif (y_change < 0 and x_change > 0):
                    direction = 'right-up'
                elif (y_change < 0 and x_change < 0):
                    direction = 'left-up'
                elif (y_change > 0 and x_change < 0):
                    direction = 'left-down'
                    
                if (y_change_cub > 0 and x_change_cub == 0):
                    red_direction = 'down'
                elif (y_change_cub < 0 and x_change_cub == 0):
                    red_direction = 'up'
                elif (y_change_cub == 0 and x_change_cub > 0):
                    red_direction = 'right'
                elif (y_change_cub == 0 and x_change_cub < 0):
                    red_direction = 'left'
                elif (y_change_cub > 0 and x_change_cub > 0):
                    red_direction = 'right-down'
                elif (y_change_cub < 0 and x_change_cub > 0):
                    red_direction = 'right-up'
                elif (y_change_cub < 0 and x_change_cub < 0):
                    red_direction = 'left-up'
                elif (y_change_cub > 0 and x_change_cub < 0):
                    red_direction = 'left-down'

                if (x >= x_cub - 10
                    and x <= x_cub + 10
                    and y >= y_cub - 10
                    and y <= y_cub + 10):
                    if mode == 'Two player`s': 
                        score += -1
                        cub_score += -1
                    else:
                        score += -1
                    p.log('Respawning...')
                    p.boom(two_player_i, x_cub, y_cub)
                    p.boom(player_i, x, y)
                    p.message('Respawning...', 'white', 'large')
                    clock.tick(2)
                    x = randint(0, size)
                    y = randint(0, size)
                    x_cub = randint(0, size)
                    y_cub = randint(0, size)
                
                if mode == 'One player':
                    mustChange = (randint(0, 30) == 1)
                    mustStop = (randint(0, 280) == 1)
                    y_cub_y_nimiq = (y_cub == y_nimiq or y_cub == y_nimiq + 5 or y_cub == y_nimiq - 5)
                    x_cub_x_nimiq = (x_cub == x_nimiq or x_cub == x_nimiq + 5 or x_cub == x_nimiq - 5)
                else:
                    mustChange = False
                    mustStop = False
                    y_cub_y_nimiq = False
                    x_cub_x_nimiq = False

                if x >= size - 20:
                    y_change = 0
                    x_change = 0
                    x = 1
                    p.boom(player_i, x, y)
                    score += -1
                elif x <= 0:
                    y_change = 0
                    x_change = 0
                    x = size - 21
                    p.boom(player_i, x, y)
                    score += -1
                elif y >= size - 20:
                    y_change = 0
                    x_change = 0
                    y = 1
                    p.boom(player_i, x, y)
                    score += -1
                elif y <= 0:
                    y_change = 0
                    x_change = 0
                    y = size - 21
                    p.boom(player_i, x, y)
                    score += -1

                elif x_cub >= size - 20:
                    y_change_cub = 0
                    x_change_cub = 0
                    x_cub = 1
                    p.boom(two_player_i, x_cub, y_cub)
                    if mode == 'Two player`s': 
                        cub_score += -1
                elif x_cub <= 0:
                    y_change_cub = 0
                    x_change_cub = 0
                    x_cub = size - 21
                    p.boom(two_player_i, x_cub, y_cub)
                    if mode == 'Two player`s': 
                        cub_score += -1
                elif y_cub >= size - 20:
                    y_change_cub = 0
                    x_change_cub = 0
                    y_cub = 1
                    p.boom(two_player_i, x_cub, y_cub)
                    if mode == 'Two player`s': 
                        cub_score += -1
                elif y_cub <= 0:
                    y_change_cub = 0
                    x_change_cub = 0
                    y_cub = size - 21
                    p.boom(two_player_i, x_cub, y_cub)
                    if mode == 'Two player`s': 
                        cub_score += -1

                elif y_cub_y_nimiq:
                    y_change_cub = 0
                    if x_cub <= x_nimiq:
                        x_change_cub = int(max_cub_move_speed)
                    elif x_cub >= x_nimiq:
                        x_change_cub = - int(max_cub_move_speed)
                    mustChange = (0 == 1)
                    mustStop = (0 == 1)
                    
                elif x_cub_x_nimiq:
                    x_change_cub = 0
                    if y_cub <= y_nimiq:
                        y_change_cub = int(max_cub_move_speed)
                    elif y_cub >= y_nimiq:
                        y_change_cub = - int(max_cub_move_speed)
                    mustChange = (0 == 1)
                    mustStop = (0 == 1)
                    
                elif mustChange:
                    y_change_cub = randint(min_cub_move_speed, max_cub_move_speed)
                    x_change_cub = randint(min_cub_move_speed, max_cub_move_speed)
                elif mustStop:
                    x_change_cub = y_change_cub = 0

                x_cub += x_change_cub
                y_cub += y_change_cub
                
                x += x_change
                y += y_change


                p.red_car_move(red_direction, x_cub, y_cub)
                p.car_move( direction, x, y)

                p.draw_nimiq(x_nimiq, y_nimiq)
                pygame.display.update()
                
                if (x >= x_nimiq - 10
                        and x <= x_nimiq + 10
                        and y >= y_nimiq - 10
                        and y <= y_nimiq + 10):
                    score += 1
                    if mode == 'One player': 
                        p.message('like a boss, ' + player_i, 'green', 'small', x_nimiq + 16, y_nimiq)
                    else: 
                        p.message('like a boss', 'green', 'small', x_nimiq + 16, y_nimiq)
                    p.log(player_i + '`s score: ' + str(score))
                    x_nimiq = round(randint(0, size - 10) / 10.0) * 10.0
                    y_nimiq = round(randint(0, size - 10) / 10.0) * 10.0
                    
                elif (x_cub >= x_nimiq - 10
                    and x_cub <= x_nimiq + 10
                    and y_cub >= y_nimiq - 10
                    and y_cub <= y_nimiq + 10):
                    cub_score += 1
                    p.log(two_player_i + '`s score: ' + str(cub_score))
                    if mode == 'One player': 
                        p.message('like a boss, ' + two_player_i, 'green', 'small', x_nimiq + 16, y_nimiq)
                    else: 
                        p.message('like a noob', 'white', 'small', x_nimiq + 16, y_nimiq)
                    x_nimiq = round(randint(0, size - 30) / 10.0) * 10.0
                    y_nimiq = round(randint(0, size - 30) / 10.0) * 10.0

                p.player_score(player_i, score)
                p.cub_score_message(cub_score)
                if mode != 'One player':
                    p.player(player_i + ' vs ' + two_player_i)
                else:
                    p.player(player_i + ' on ' + mode)
                clock.tick(FPS)
            else:
                p.message('game paused!', 'white', 'med', size/2, size/2)
                clock.tick(FPS)
                
        if mode == 'One player':   
            if score > cub_score:
                game_display.fill(p.get_color('white'))
                pygame.display.update()
                msg = 'You WIN!!!'
            elif score < cub_score:
                game_display.fill(p.get_color('black'))
                msg = 'You lose.'
            else: msg = 'Tie'
        else:
            if cub_score > score: msg = two_player_i + ' WIN!'    
            elif cub_score < score: msg = player_i + ' WIN!'      
            else: msg = 'TIE!!!'
                    
        p.message(msg, 'gold') 
        clock.tick(2)
        game_display.fill(p.get_color('blue'))
        p.message('Closing the game... Your score: ' + str(score) + ', ' + two_player_i + '`s score: ' + str(cub_score),
                       'white')
        clock.tick(2)
        p.save_exit(player_i, score, two_player_i, cub_score)
            
    except Exception as e: 
        p.log('Error: ')
        p.log(e)
        p.my_exit(1)

loop()
        