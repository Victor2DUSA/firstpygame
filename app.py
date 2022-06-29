from tkinter import CENTER
import pygame 
from sys import exit


def display_score(): 
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center= (400,50))
    screen.blit(score_surf,score_rect)
    return current_time


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
# test_font = pygame.font.Font(fonttype, font size)
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')
test_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

text_surface = test_font.render("My  game", False, (64,64,64))
text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_position = 600
snail_rect = snail_surface.get_rect(midbottom=(600,300))

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
# Drawing a rectangle
player_rect = player_surface.get_rect(midbottom=(40,300))


game_name = test_font.render('Pixel Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,50))

game_message = test_font.render("Press space to run", False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,350))

"""Key board mechanics 
1. keyboard input 
2. jump + gravity 
3.creating a floor 
"""
player_gravity = 0
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2.5)
player_stand_recct = player_stand.get_rect(center = (400,200))




while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #key board input 
        if game_active:
            if event.type == pygame.KEYDOWN: 
                if  event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.x = 800
                start_time = int(pygame.time.get_ticks()/1000)


    if game_active:
        screen.blit(test_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen, '#c0e8ec', text_rect,)
        # pygame.draw.rect(screen, '#c0e8ec', text_rect,10)
        # screen.blit(text_surface, text_rect)
        score = display_score()
        
        snail_rect.x -=4
        if snail_rect.right <= -10: 
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # player_rect.left += 1
        screen.blit(player_surface, player_rect)

        # if player_rect.colliderect(snail_rect): 
        #     print("collision")

        #keyboord input 
        # if keys[pygame.K_SPACE]:
        #     print("jump")
        
        

        #player
        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: 
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #collisions
        if snail_rect.colliderect(player_rect):
            game_active = False 
    else: 
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_recct)
        score_message = test_font.render(f"Your Score: {score}", False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name, game_name_rect)
        

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)
    

    pygame.display.update()
    clock.tick(60) 
