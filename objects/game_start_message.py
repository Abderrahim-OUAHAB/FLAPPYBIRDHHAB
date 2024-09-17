import pygame.sprite

import assets
import configs
from layer import Layer

class GameStartMsg(pygame.sprite.Sprite):
    def __init__(self,*groups):
        self._layer=Layer.UI
        self.image=assets.get_sprite("message")
        self.rect=self.image.get_rect(center=(configs.SCREEN_WIDTH *0.5,configs.SCREEN_HEIGHT*0.5))
        super().__init__(*groups)