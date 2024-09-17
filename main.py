import pygame
import assets
import configs
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
from objects.game_start_message import GameStartMsg
from objects.game_over_message import GameOvertMsg
from objects.score import Score
import random
pygame.init()
pygame.display.set_caption("FLAPPYBIRDHHAB","assets/sprites/redbird-upflap.png")
screen=pygame.display.set_mode((configs.SCREEN_WIDTH,configs.SCREEN_HEIGHT))
clock=pygame.time.Clock()
column_craete_event=pygame.USEREVENT
running=True
gameOver=False
gamestart=False
speedAddGame=3

assets.load_sprites()
assets.load_audios()
assets.play_audio("m")
sprites=pygame.sprite.LayeredUpdates()
def create_sprites():
    backs = ["bsky", "forest", "background","l2","l3"]
    back=backs[random.randint(0,4)]
    Background(back,0,sprites)
    Background(back,1,sprites)

    Floor(0,sprites)
    Floor(1,sprites)

    return Bird(sprites),GameStartMsg(sprites),Score(sprites)

bird,gameStartedMsg,score=create_sprites()





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==column_craete_event:
            Column(sprites)
        if event.type== pygame.KEYDOWN:
            if (event.key==pygame.K_SPACE or event.key==pygame.K_UP ) and not gamestart and not gameOver:
                gamestart=True
                gameStartedMsg.kill()
                pygame.time.set_timer(column_craete_event, millis=2500)
            if (event.key==pygame.K_RETURN ) and gameOver:
                gameOver=False
                gamestart=False
                configs.FPS=60
                sprites.empty()
                bird,gameStartedMsg,score=create_sprites()


        bird.handle_event(event,gameOver)
    screen.fill(0)


    sprites.draw(screen)
    if gamestart and not gameOver:
        sprites.update()

    if bird.chack_collision(sprites) and not gameOver:
        gameOver=True
        gamestart=False
        GameOvertMsg(sprites)
        pygame.time.set_timer(column_craete_event, millis=0)
        assets.play_audio("hit")
    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed() :
            score.value+=1
            assets.play_audio("point")
            if score.value >0 and score.value % speedAddGame ==0:
                configs.FPS+=speedAddGame


    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
