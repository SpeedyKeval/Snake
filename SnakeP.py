import pygame, time, math
from pygame.locals import *

################################## Constants ##################################

FRAME_HEIGHT = 300
FRAME_WIDTH  = 400
FRAME_COLOR = [255,255,255]
speed = 25.0

snake_length_number = 15 # Initial Lenght of the Snake
Snake_Width = 5 # Width of Snake
SNAKE_COLOR = [255,105,180]
SNAKE_THICKNESS = 2
DIRECTION = [True, False]
GAP = [5, 5]
x,y = 1,1
snake_length_number_count = 1

Food_Ball_Size = 2 # Radius of the food of the ball
FOOD_BALL_COLOR = [139,99,108]

pos = [FRAME_WIDTH//2+10, FRAME_HEIGHT//2-10]
pos_x, pos_y = None, FRAME_HEIGHT//2-10

flag_x_0 = False
flag_y_0 = None

gameflag = True

############################### Class for Snake ###############################

class SnakeBall():
    def __init__(self, pos):
        self.__color = SNAKE_COLOR
        self.pos = pos
        self.__radius = Snake_Width
        self.__THICKNESS = SNAKE_THICKNESS
        self.DIRECTION = DIRECTION
        
    def pro(self):
        return self.__color, self.pos, self.__radius, self.__THICKNESS
    
############################## Class for food #################################
        
class Food():
    def __init__(self):
        from random import randint
        self.pos = [randint(10,FRAME_WIDTH-30),randint(10,FRAME_HEIGHT-20)]
        self.scale = (14,15)
        self.image = pygame.image.load('apple.png')
        
    def showimage(self):
        image = pygame.transform.scale(self.image,self.scale)
        return image
        
    def getpos(self):
        return self.pos
################################ Additional ###################################

def gap():
    global GAP
    if DIRECTION[0]:
        GAP[0] = 5
    else:
        GAP[0] = 0
        
    if DIRECTION[1]:
        GAP[1] = 5
    else:
        GAP[1] = 0
        
gap()

def pos_list_fun():
    pos_list = []
    for i in range(snake_length_number):
        pos_list.append(SnakeBall([pos[0]-(i*GAP[0]), pos[1]-(i*GAP[1])]))
    return pos_list

pos_list = pos_list_fun()
pos_x = pos_list[0].pos[0]
pos_y = pos_list[0].pos[1]

################################ Food Object ##################################

food = Food()

############################### String to Text ################################

def text(string,style="monospace",size=15,width=1,color=(255,255,0)):
        ''' Text for display it on the screen, as string cannot be '''
        myfont = pygame.font.SysFont(style, size)
        # render text
        label = myfont.render(string, size, color)
        return label

############################### Collision #####################################

def collision(snakemouth):
    global Snake_Width, flag_y_0, food, snake_length_number_count, speed
    length = math.sqrt((food.getpos()[0]-snakemouth.pos[0])**2+(food.getpos()[1]-snakemouth.pos[1])**2)
        
    if 0 < length <= Snake_Width+14:
        #print (length,Snake_Width)
        flag_y_0 = True
        pos_list.append(SnakeBall(pos_list[-1].pos))
        pos_list.append(SnakeBall(pos_list[-1].pos))
        pos_list.append(SnakeBall(pos_list[-1].pos))
        snake_length_number_count += 1
        if snake_length_number_count % 10 == 0:
            speed -= 1.0
        del (food)
        return Food()
    for i in pos_list:
        if pos_list[0] != i:
            #snakecollide = math.sqrt(((pos_list[0].pos[0]-i.pos[0])**2) + ((pos_list[0].pos[1]-i.pos[1])**2))
            #if 0 < snakecollide < 2:
            print (pos_list.index(i))
            if pos_list[0].pos == [i.pos[0]+Snake_Width,i.pos[1]+Snake_Width]:
                #del(food)
                snake.blit(text('Game Over',size=50),(FRAME_WIDTH//5,FRAME_HEIGHT//3))
    
################################ Main #########################################

snake = pygame.display.set_mode((FRAME_WIDTH,FRAME_HEIGHT))

pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

pygame.init()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    if gameflag:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        
        snake.fill(FRAME_COLOR)
            
        snake.blit(food.showimage(), food.getpos())
        
        for i in pos_list:
            pygame.draw.circle( snake, i.pro()[0], i.pro()[1], i.pro()[2], i.pro()[3])
        
        food_1 = collision(pos_list[0])
        
        if flag_y_0:
            food = food_1
            flag_y_0 = False
        
        for i in range(len(pos_list)-1,0,-1):
            pos_list[i].pos = [pos_list[i-1].pos[0],
                     pos_list[i-1].pos[1]]
                
        if keys != None:
            
            if keys[K_LEFT] and ( not pos_list[0].DIRECTION[0] ):
                x = -2
                
                pos_x = pos_list[0].pos[0]
                pos_y = pos_list[0].pos[1]
                pos_list[0].DIRECTION[1] = not pos_list[0].DIRECTION[1]
                pos_list[0].DIRECTION[0] = not pos_list[0].DIRECTION[0]
                
                flag_x_0 = True
                
                    
            elif keys[K_UP] and ( not pos_list[0].DIRECTION[1] ):
                y = -2
    
                pos_x = pos_list[0].pos[0]
                pos_y = pos_list[0].pos[1]
                pos_list[0].DIRECTION[0] = not pos_list[0].DIRECTION[0]
                pos_list[0].DIRECTION[1] = not pos_list[0].DIRECTION[1]
                
                
                flag_x_0 = True 
                
            elif keys[K_DOWN] and ( not pos_list[0].DIRECTION[1] ):
                y = 2
                
                pos_x = pos_list[0].pos[0]
                pos_y = pos_list[0].pos[1]
                
                pos_list[0].DIRECTION[0] = not pos_list[0].DIRECTION[0]
                pos_list[0].DIRECTION[1] = not pos_list[0].DIRECTION[1]
                flag_x_0 = True
                
            elif keys[K_RIGHT] and (not pos_list[0].DIRECTION[0]):
                x = 2
                
                pos_x = pos_list[0].pos[0]
                pos_y = pos_list[0].pos[1]
                
                pos_list[0].DIRECTION[1] = not pos_list[0].DIRECTION[1]
                pos_list[0].DIRECTION[0] = not pos_list[0].DIRECTION[0]
                flag_x_0 = True
            else:
                
                if flag_x_0:
                    if pos_list[0].DIRECTION[0]:
                        pos_list[0].pos[0] = pos_list[0].pos[0] + x
                    elif pos_list[0].DIRECTION[1]:
                        pos_list[0].pos[1] = pos_list[0].pos[1] + y
                    
                else:
                    pos_list[0].pos = [ pos_list[0].pos[0]+2, pos_list[0].pos[1]+0]
                                
        for i in pos_list:
            
            if i.pos[0] >= FRAME_WIDTH or i.pos[0] <= 0:
                gameflag = False
                #i.pos[0] = i.pos[0] % FRAME_WIDTH
            
            if i.pos[1] >= FRAME_HEIGHT or i.pos[1] <=0:
                gameflag = False
                #i.pos[1] = i.pos[1] % FRAME_HEIGHT
    else:
        snake.fill((0,0,0))
        snake.blit(text('Game Over',size=50),(FRAME_WIDTH//5,FRAME_HEIGHT//3))
    
    time.sleep (speed / 1000.0)
    pygame.display.update()
    clock.tick(60)
                
pygame.quit()