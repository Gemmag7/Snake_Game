#installing essential libraries
import pygame
import random
import time

snake_speed = 15


#Setting default window size
window_x = 720
window_y = 480

#Defining colours 
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#Initialising game 
pygame.init()

#Initialising the game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

#Frames per Second Controller
fps = pygame.time.Clock()

#Defining snake default position
snake_position = [100, 50]

#Defining first 4 blocks of the snake body
snake_body = [
    [100,50], 
    [90, 50], 
    [80, 50], 
    [70,50]
    ]

#fruit position
fruit_position = [random.randrange(1, (window_x //10)) * 10, 
                 random.randrange(1, (window_y //10))* 10]

fruit_spawn = True

#Setting the default snake direction to right
direction = 'RIGHT'
change_to = direction

#Setting the inital score to 0
score = 0

#Display Score Function
def show_score(choice, color, font, size):
    #Creating font object 
    score_font = pygame.font.SysFont(font, size)

    #Creating the  display surface object 
    score_surface = score_font.render('Score: ' + str(score), True, color)

    #Creating a rectangular object for text
    score_rectangle = score_surface.get_rect()

    #Displaying the text
    game_window.blit(score_surface, score_rectangle)


#Creating the Game Over function
def game_over():
    #Creating the font object 
    my_font = pygame.font.SysFont('times new roman', 50)

    #Creating a text surface which text will display
    game_over_surface = my_font.render('Your score is: ' + str(score), True, red)

    #
    game_over_rectangle = game_over_surface.get_rect()

    #
    game_over_rectangle.midtop = (window_x/2, window_y/4)

    #
    game_window.blit(game_over_surface, game_over_rectangle)
    pygame.display.flip()

    #
    time.sleep(2)

    #
    pygame.quit()

    #Quit the program 
    quit()

#Main Funtion
while True:
    
    #Handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to ='DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    #If 2 keys are pressed at once, then direction of snake should not be able to mover in both directions
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to =='DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to =='LEFT' and direction!= 'RIGHT':
        direction = 'LEFT'
    if change_to =='RIGHT' and direction != 'LEFT':
        direction='RIGHT'

    #Moving the snake 
    if direction =='UP':
        snake_position[1] -=10
    if direction == 'DOWN':
        snake_position[1] +=10
    if direction == 'LEFT':
        snake_position[0] -=10
    if direction =='RIGHT':
        snake_position[0] +=10

    #Snake body growing function
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] ==fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x //10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1],10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    #Game Over Funtions
    if snake_position[0]< 0 or snake_position[0] > window_x -10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y -10:
        game_over()

    #Touching Snake Body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    #Displaying score througout game 
    show_score(1, white, 'times new roman', 20)

    #Refresh game screen 
    pygame.display.update()

    #Refresh rate 
    fps.tick(snake_speed)