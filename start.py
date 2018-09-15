import pygame
from random import randint 
from Data.program import *
log('lib load complete!')


def loop():
    try:
        log('Game load complete!')

        score = 0
        cub_score = 0
        direction = 'up'
        red_direction = 'up'
        pause = False

        x_nimiq = round(randint(0, size - 30))
        y_nimiq = round(randint(0, size - 30))

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
        
        log('Enter in main loop.')

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
                            FPS = 5
                    elif event.key == pygame.K_r:
                        restart()
                        pass
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
                    log('Respawning...')
                    boom(x_cub, y_cub)
                    boom(x, y)
                    message('Respawning...', 'white')
                    pygame.display.update()
                    x = randint(0, size)
                    y = randint(0, size)
                    x_cub = randint(0, size)
                    y_cub = randint(0, size)
                    clock.tick(2)
                
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
                    x_change = -10
                    boom(x, y)
                elif x <= 0:
                    y_change = 0
                    x_change = 10
                    boom(x, y)
                elif y >= size - 20:
                    y_change = -10
                    x_change = 0
                    boom(x, y)
                elif y <= 0:
                    y_change = 10
                    x_change = 0
                    boom(x, y)
                
                elif x_nimiq >= size - 20: x = 1
                elif x_nimiq <= 0: x_nimiq = size - 21
                elif y_nimiq >= size - 20: y_nimiq = 1
                elif y_nimiq <= 0: y_nimiq = size - 21
                
                elif x_cub >= size - 20:
                    y_change_cub = 0
                    x_change_cub = -10
                    boom(x_cub, y_cub)
                elif x_cub <= 0:
                    y_change_cub = 0
                    x_change_cub = 10
                    boom(x_cub, y_cub)
                elif y_cub >= size - 20:
                    y_change_cub = -10
                    x_change_cub = 0
                    boom(x_cub, y_cub)
                elif y_cub <= 0:
                    y_change_cub = 10
                    x_change_cub = 0
                    boom(x_cub, y_cub)

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
                    mustChange = (False)
                    mustStop = (False)
                    
                elif mustChange:
                    y_change_cub = randint(-5, 5)
                    x_change_cub = randint(-5, 5)
                elif mustStop:
                    x_change_cub = y_change_cub = 0

                x_cub += x_change_cub
                y_cub += y_change_cub
                
                x += x_change
                y += y_change


                red_car_move(red_direction, x_cub, y_cub)
                car_move( direction, x, y)

                draw_nimiq(x_nimiq, y_nimiq)
                
                if (x >= x_nimiq - 10
                        and x <= x_nimiq + 10
                        and y >= y_nimiq - 10
                        and y <= y_nimiq + 10):
                    score += 1
                    if mode == 'One player': 
                        message('like a boss, ' + player_i, 'green', x_nimiq + 16, y_nimiq)
                    else: 
                        message('like a boss', 'green', x_nimiq + 16, y_nimiq)
                    log(player_i + '`s score: ' + str(score))
                    x_nimiq = round(randint(0, size - 10) / 10.0) * 10.0
                    y_nimiq = round(randint(0, size - 10) / 10.0) * 10.0
                    
                elif (x_cub >= x_nimiq - 10
                    and x_cub <= x_nimiq + 10
                    and y_cub >= y_nimiq - 10
                    and y_cub <= y_nimiq + 10):
                    cub_score += 1
                    log(two_player_i + '`s score: ' + str(cub_score))
                    if mode == 'One player': 
                        message('like a boss, ' + two_player_i, 'green', x_nimiq + 16, y_nimiq)
                    else: 
                        message('like a noob', 'white', x_nimiq + 16, y_nimiq)
                    x_nimiq = round(randint(0, size - 30))
                    y_nimiq = round(randint(0, size - 30))

                message(player_i + '`s score: ' + str(score), 'white', size/10, 10)
                message(two_player_i + '`s score: ' + str(cub_score), 'white', size - size/6, 10)
                if mode != 'One player':
                    message(player_i + ' vs ' + two_player_i, 'white', size/2, 10)
                else:
                    message(player_i + ' on ' + mode, 'white', size/2, 10)
                pygame.display.update()
                clock.tick(FPS)
            else:
                message('game paused!', 'white', size/2, size/2, 'med')
                pygame.display.update()
                clock.tick(FPS)

        save()
        my_exit()
        pass
            
    except Exception as e: 
        log('Fatal Error in main loop: ')
        log(e)
        pass

loop()
log('Exited! \r\n')
        
