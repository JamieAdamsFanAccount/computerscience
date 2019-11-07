# Special thanks to http://programarcadegames.com/python_examples/show_file.php?file=moving_sprites.py
 
import pygame

white = (255, 255, 255)
blue = (0, 0, 255)

basex = 100;
basey = 100;
 
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([basex, basey])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
 
class Player(Block):
    def update(self, pressed):
        if pressed[pygame.K_d]:
            player.rect.x = player.rect.x + movescale;
        elif pressed[pygame.K_a]:
            player.rect.x = player.rect.x - movescale;

        if pressed[pygame.K_w]:
            player.rect.y = player.rect.y - movescale;
        elif pressed[pygame.K_s]:
            player.rect.y = player.rect.y + movescale;
 
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode([screen_width, screen_height])

playing = True;
 
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)

movescale = 5;

while playing == True:

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False;
    if pressed[pygame.K_ESCAPE]:
        playing = False;

    screen.fill(white)
 
    player.update(pressed)
    all_sprites_list.draw(screen)
 
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()