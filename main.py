# Example file showing a basic pygame "game loop"
import pygame
import random
import time
import math

import pygame.draw
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
pygame.display.set_caption("Trignometry Function Sketcher")
clock = pygame.time.Clock()
running = True



font = pygame.font.Font('./trig-grapher/fonts/LycheeSoda.ttf', 24)
font2 = pygame.font.Font('./trig-grapher/fonts/LycheeSoda.ttf', 12)
font3 = pygame.font.Font('./trig-grapher/fonts/lemonmilk.otf', 18)
titleFont  = pygame.font.Font('./trig-grapher/fonts/LycheeSoda.ttf', 72)
font4 = pygame.font.Font('./trig-grapher/fonts/LycheeSoda.ttf', 44)


background =pygame.image.load('./trig-grapher/assets/background.png') 
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

angle_text_rect = pygame.Rect(150, 200, 142, 32)
period_text_rect = pygame.Rect(400, 200, 142, 32)
amplitude_text_rect = pygame.Rect(690, 200, 142, 32)
b_text_rect = pygame.Rect(1090, 200, 142, 32)


color_tan_btn = 'lightblue'
color_cos_btn = 'pink'
color_sin_btn = '#f7b065'

tan_btn_rect = pygame.draw.rect(screen, color_tan_btn, (490, 300, 140, 42), 0, 2)
cos_btn_rect = pygame.draw.rect(screen, color_cos_btn, (tan_btn_rect.x + 100, 300, 120, 42), 0,2)
sin_btn_rect = pygame.draw.rect(screen, color_sin_btn, (cos_btn_rect.x + 120, 300, 80, 42), 0,2)



is_sin_btn_pressed = False
is_tan_btn_pressed = False
is_cos_btn_pressed = False



def drawLine(w:int, h: int, angle:int, func:str, period:int):
    pygame.draw.line(screen, 'black', (0,h/2), (w,  h/2), 5)
    pygame.draw.line(screen, 'black', (40, 0), (40, 720), 5)   
    prev_x  = 40
    prev_y = h/2
    p = 90/period

    if p < 90:
        angle = int (angle * period)
    elif p > 90:
        angle = int(angle * period)

    if func == 's':
        for i in range(angle):
            
            ratio_of_angle = (w-40)/angle
            
            sine_value = math.sin(math.radians(i))
            if sine_value > 0 or sine_value ==  math.sin(math.radians(0)):
                pygame.draw.line(screen, 'green',(prev_x, prev_y), ((i * ratio_of_angle) + 40, h/2 -(sine_value * h/2)))
                prev_x = (i * ratio_of_angle) + 40
                prev_y = h/2 -(sine_value * h/2)
            elif sine_value < 0:
                pygame.draw.line(screen, 'red',(prev_x, prev_y), ((i * ratio_of_angle) + 40,  h/2 -(sine_value * h/2)))
                prev_x = (i * ratio_of_angle) + 40
                prev_y = h/2 -(sine_value * h/2)
    elif func == 'c':
            prev_x  = 40
            prev_y = 0
            ratio_of_angle = (w-40)/angle
            for i in range(angle):
                cos_value = math.cos(math.radians(i))
                if cos_value > 0 or cos_value ==  math.cos(math.radians(0)):
                    pygame.draw.line(screen, 'green',(prev_x, prev_y), ((i * ratio_of_angle) + 40, h/2 -(cos_value * h/2)), 3)
                    prev_x = (i * ratio_of_angle) + 40
                    prev_y = h/2 -(cos_value * h/2)
                elif cos_value < 0:
                    pygame.draw.line(screen, 'red',(prev_x, prev_y), ((i * ratio_of_angle) + 40,  h/2 -(cos_value * h/2)), 3)
                    prev_x = (i * ratio_of_angle) + 40
                    prev_y = h/2 -(cos_value * h/2)
    elif func == 't':
            prev_x  = 40
            prev_y = h/2
            ratio_of_angle = (w - 40)/angle
            for i in range(angle):
                if not i % p == 0:
                    tan_value = math.tan(math.radians(i))
                    if tan_value > 0 or tan_value ==  math.tan(math.radians(0)):
                        pygame.draw.line(screen, 'green',(prev_x, prev_y), ((i * ratio_of_angle) + 40, h/2 -(tan_value * h/2)))
                        prev_x = (i * ratio_of_angle) + 40
                        prev_y = h/2 -(tan_value * h/2)
                    elif tan_value < 0:
                        pygame.draw.line(screen, 'red',(prev_x, prev_y), ((i * ratio_of_angle) + 40,  h/2 -(tan_value * h/2)))
                        prev_x = (i * ratio_of_angle) + 40
                        prev_y = h/2 -(tan_value * h/2)
                
         
      
def drawPoints(w:int, h:int ,angle: int, period: int):
    period = (90 / period)
    ratio = int(angle/period)
    ratio_of_angle = (w-40)/angle
    for i in range(ratio):
        if not i == 0:
            sine_value = math.sin(math.radians((i * period)))
            font_surf = font.render(f'{i * period}', False, (0,0,0))
            x = ((i * period )* ratio_of_angle) + 40
            pygame.draw.line(screen, 'black', (x, (h/2) - 20), (x, (h/2) + 20), 4)
            screen.blit(font_surf, (x - 10, (h/2) + 30))

def drawAmplitude(amplitude, b):
    if not b or b == 0:
        max_point = amplitude
        min_point = amplitude * -1
    
        pygame.draw.line(screen, 'black', (10, 0), (40, 0), 10)
        pygame.draw.line(screen, 'black', (10, 720), (40, 720), 10)
        max_font = font.render(f'{max_point}' ,False, (0, 255, 0))
        min_font = font.render(f'{min_point}' ,False, (255, 0, 0))
        screen.blit(max_font,(10, 10) )
        screen.blit(min_font,(10, 690))

  
    if b and b != 0:
        if b < 0:
            max_point = amplitude - (b * -1)
            min_point = (amplitude * -1) - (b * -1)
    

            pygame.draw.line(screen, 'black', (10, 0), (40, 0), 10)
            pygame.draw.line(screen, 'black', (10, 720), (40, 720), 10)
            max_font = font.render(f'{max_point}' ,False, (0, 255, 0))
            min_font = font.render(f'{min_point}' ,False, (255, 0, 0))
            screen.blit(max_font,(10, 10) )
            screen.blit(min_font,(10, 690))
        else:
            max_point = amplitude + b
            min_point = (amplitude * -1) + (b)
    

            pygame.draw.line(screen, 'black', (10, 0), (40, 0), 10)
            pygame.draw.line(screen, 'black', (10, 720), (40, 720), 10)
            max_font = font.render(f'{max_point}' ,False, (0, 255, 0))
            min_font = font.render(f'{min_point}' ,False, (255, 0, 0))
            screen.blit(max_font,(10, 10) )
            screen.blit(min_font,(10, 690))


def isAnInteger(unicode):
    number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

    for i in number_list:
        if unicode == i:
            return True
        
    return False



func = 'c'
ANGLE = 360
ratio = SCREEN_WIDTH/360
PERIOD = 0.5
AMPLITUDE = 1
b = -2

angle_text = ''
period_text = ''
amplitude_text = ''
b_text = ''


trig_graph_started = False
selected_angle_rect = False
selected_period_rect = False
selected_amplitude_rect = False
selected_b_rect = False

angle_font =  font2.render(f'{angle_text}' ,False, 'black')
period_font =  font2.render(f'{period_text}' ,False,  'black')
amplitude_font =  font2.render(f'{amplitude_text}' ,False,  'black')
b_font =  font2.render(f'{b_text}' ,False,  'grey')

a_font =  font3.render(f'Angle: ' ,True, 'black')
p_font =  font3.render(f'Period: ' ,True,  'black')
amp_font =  font3.render(f'Amplitude:' ,True,  'black')
ba_font =  font3.render(f'B-value(use 0 if none): ' ,True, 'black')



delay_time = 0


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not trig_graph_started:
            # print(f"Mouse coords: {pygame.mouse.get_pos()}\nAngle: {((pygame.mouse.get_pos()[0]) - 40) / ratio}")
            if angle_text_rect.collidepoint(pygame.mouse.get_pos()):
                selected_angle_rect = True
            elif period_text_rect.collidepoint(pygame.mouse.get_pos()):
                selected_period_rect = True
            elif amplitude_text_rect.collidepoint(pygame.mouse.get_pos()):
                selected_amplitude_rect = True
            elif b_text_rect.collidepoint(pygame.mouse.get_pos()):
                selected_b_rect = True
            else:
                selected_angle_rect = False
                selected_b_rect = False
                selected_amplitude_rect = False
                selected_period_rect = False
            
            if tan_btn_rect.collidepoint(pygame.mouse.get_pos()):
                is_tan_btn_pressed = True
                is_sin_btn_pressed = False
                is_cos_btn_pressed = False

            elif sin_btn_rect.collidepoint(pygame.mouse.get_pos()):
                is_sin_btn_pressed = True
                is_tan_btn_pressed = False
                is_cos_btn_pressed = False
           
            elif cos_btn_rect.collidepoint(pygame.mouse.get_pos()):
                is_cos_btn_pressed = True
                is_sin_btn_pressed = False
                is_tan_btn_pressed = False

            if generate_btn_rect.collidepoint(pygame.mouse.get_pos()) and not (angle_text == '' or period_text == '' or b_text == '' or amplitude_text == ''):
                print("generate")
                ANGLE = int(angle_text)
                PERIOD = float(period_text)
                b = int(b_text)
                AMPLITUDE = int(amplitude_text)
                trig_graph_started = True
            
        if event.type == pygame.KEYDOWN and not trig_graph_started: # bro wtf is this code shouldve just made a function to make the code readibility better
          #  if not (amplitude_font.get_width()) >= 100 and not (angle_font.get_width()) >= 100 and not (b_font.get_width()) >= 100 and not (period_font.get_width()) >= 100:
            if isAnInteger(event.unicode) or event.key == pygame.K_BACKSPACE:
              
                if selected_angle_rect:
                    if event.key == pygame.K_BACKSPACE:
                        angle_text = angle_text[:-1]
                    else:
                        angle_text += event.unicode
                    angle_font =  font.render(f'{ angle_text}' ,False,'black')
                    
                elif selected_period_rect:
                    if event.key == pygame.K_BACKSPACE:
                        period_text = period_text[:-1]
                    else:
                        period_text += event.unicode
                    period_font =  font.render(f'{period_text}' ,False, 'black')
                elif selected_amplitude_rect :
                    if event.key == pygame.K_BACKSPACE:
                        amplitude_text = amplitude_text[:-1]
                    else:
                        amplitude_text += event.unicode
                    amplitude_font =  font.render(f'{amplitude_text}' ,False, 'black')
                elif selected_b_rect:
                    if event.key == pygame.K_BACKSPACE:
                        b_text = b_text[:-1]
                    else:
                        b_text += event.unicode
                    b_font =  font.render(f'{b_text}' ,False, 'black')
            # else:
            #    if selected_angle_rect:
            #        if event.key == pygame.K_BACKSPACE:
            #            angle_text = angle_text[:-1]
            #        angle_font =  font.render(f'{ angle_text}' ,False, (0, 255, 0))
                    
            #    elif selected_period_rect:
            #        if event.key == pygame.K_BACKSPACE:
            #            period_text = period_text[:-1]
           #         period_font =  font.render(f'{period_text}' ,False, (0, 255, 0))
            #    elif selected_amplitude_rect :
           #        if event.key == pygame.K_BACKSPACE:
            #        amplitude_font =  font.render(f'{amplitude_text}' ,False, (0, 255, 0))
            #    elif selected_b_rect:
            #        if event.key == pygame.K_BACKSPACE:
            #            b_text = b_text[:-1]
            #        b_font =  font.render(f'{b_text}' ,False, (0, 255, 0))
            
    if trig_graph_started:
        if is_sin_btn_pressed:
            func = 's'
        elif is_cos_btn_pressed:
            func = 'c'
        elif is_tan_btn_pressed:
            func = 't'

        screen.fill("white")

        
        drawLine(SCREEN_WIDTH, SCREEN_HEIGHT, ANGLE, func, PERIOD)
        drawPoints(SCREEN_WIDTH, SCREEN_HEIGHT, ANGLE, PERIOD)
        drawAmplitude(AMPLITUDE,b)
        # flip() the display to put your work on screen

        if func == 't':
            font_surf = font.render('Straight Red Lines indicate Asymptotes!', True, (0,0,0))
            screen.blit(font_surf, ((((SCREEN_WIDTH-40)/2) - 150), 600))
    else:
        screen.blit(background, background.get_rect())
        #if (angle_font.get_width() + 30) >= angle_text_rect.w:  angle_text_rect.w = angle_font.get_width() + 30
        pygame.draw.rect(screen, '#dddddd', angle_text_rect, 0, 2)
        screen.blit(a_font, (angle_text_rect.x - 90, angle_text_rect.y))

       # if (period_font.get_width() + 30) >= period_text_rect.w:  period_text_rect.w = period_font.get_width() + 30
        pygame.draw.rect(screen, '#dddddd', period_text_rect, 0, 2)
        screen.blit(p_font, (period_text_rect.x - 90, period_text_rect.y))

        #if (amplitude_font.get_width() + 30) >= amplitude_text_rect.w:  amplitude_text_rect.w = amplitude_font.get_width() + 30
        pygame.draw.rect(screen, '#dddddd', amplitude_text_rect, 0, 2)
        screen.blit(amp_font, (amplitude_text_rect.x - 130, amplitude_text_rect.y))

       # if (b_font.get_width() + 30) >= b_text_rect.w:  b_text_rect.w = b_font.get_width() + 30
        pygame.draw.rect(screen, '#dddddd', b_text_rect, 0, 2)
        screen.blit(ba_font, (b_text_rect.x - 240, b_text_rect.y))

        tan_func_font = font4.render('tan', True, 'black')
        if is_tan_btn_pressed:
            color_tan_btn = '#017dc2'
            color_sin_btn = 'orange'
            color_cos_btn = 'pink'
        elif is_cos_btn_pressed:
            color_cos_btn = '#f73c71'
            color_tan_btn = 'lightblue'
            color_sin_btn = 'orange'
        elif is_sin_btn_pressed:
            color_sin_btn = '#d95218'
            color_tan_btn = 'lightblue'
            color_cos_btn = 'pink'

        tan_btn_rect = pygame.draw.rect(screen, color_tan_btn, (490, 300, 140, 42), 0, 2)
        screen.blit(tan_func_font, ((tan_btn_rect.x) + 10, tan_btn_rect.y -3))

        cos_btn_rect = pygame.draw.rect(screen, color_cos_btn, (tan_btn_rect.x + 100, 300, 120, 42), 0,2)
        cos_func_font = font4.render('cosine', True, 'black')
        screen.blit(cos_func_font, ((cos_btn_rect.x) + 10, cos_btn_rect.y -3))

        sin_btn_rect = pygame.draw.rect(screen, color_sin_btn, (cos_btn_rect.x + 120, 300, 80, 42), 0,2)
        sin_func_font = font4.render('sine', True, 'black')
        screen.blit(sin_func_font, ((sin_btn_rect.x) + 10, sin_btn_rect.y -3))



        generate_font = font4.render('Generate', True, 'white')

        generate_btn_rect  = pygame.draw.rect(screen, 'lightgreen', (490, 640, 300, 42), 0, 8)
        screen.blit(generate_font, ((generate_btn_rect.x) + 70, generate_btn_rect.y -3))

        color = ['green', 'red', 'blue', 'orange', 'purple', 'magenta', 'yellow']
        color_chosen_timestamp = time.time()

        if delay_time == 0:
            title_color = random.choice(color)
            delay_time = time.time()
        elif (color_chosen_timestamp -  delay_time) >= 0.75: 
            title_color = random.choice(color)
            delay_time = time.time()


        title_surf = titleFont.render('Trignometric Graphs', True, title_color)

        screen.blit(title_surf, (300, 0))
        screen.blit(angle_font, (angle_text_rect.x + 10, angle_text_rect.y + 5))
        screen.blit(period_font, (period_text_rect.x + 10, period_text_rect.y + 5))
        screen.blit(amplitude_font, (amplitude_text_rect.x + 10, amplitude_text_rect.y + 5))
        screen.blit(b_font, (b_text_rect.x + 10, b_text_rect.y + 5))

    

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()