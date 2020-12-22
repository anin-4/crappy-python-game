import pygame
import random

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)


gamewidow=pygame.display.set_mode((900,600))
pygame.display.set_caption("snakes")
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

#secondary function
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewidow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

#gameloop
def game_loop():
    exit_game=False
    game_over=False
    snake_x=450
    snake_y=300
    snake_size=10
    velocity_x=0
    velocity_y=0
    score=0
    food_x=random.randrange(0,900)
    food_y=random.randrange(0,600)
    food_size=10
    fps=30
    snake_list=[]
    snake_length=1

    while not exit_game:
        if game_over==True:
            gamewidow.fill(black)
            text_screen("GAME OVER",white,350,300)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                           game_loop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:

                    if event.key==pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=10
                        velocity_x=0
            
            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=1
                snake_length+=2
                food_x=random.randrange(10,890)
                food_y=random.randrange(10,590)

            gamewidow.fill(black)
            text_screen("score:"+ str(score*10),red,4,4)
            pygame.draw.rect(gamewidow,white,[food_x,food_y,food_size,food_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over=True
            plot_snake(gamewidow,red,snake_list,snake_size)
        #pygame.draw.rect(gamewidow,red,[snake_x,snake_y,snake_size,snake_size])
        pygame.display.update()
        clock.tick(fps)

    #quit game
    pygame.quit()
    quit()
game_loop()