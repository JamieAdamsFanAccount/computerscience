# Special thanks to http://programarcadegames.com/python_examples/show_file.php?file=moving_sprites.py
 
import pygame

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

basex = 100;
basey = 100;
 
x = 0;
y = 0;

class Block(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
 
        self.image = pygame.Surface([basex, basey])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
 
class Player(Block):
    def update(self, x, y):
        self.rect.x = x;
        self.rect.y = y;

class Player2(Block):
    def update(self, x, y):
        self.rect.x = x;
        self.rect.y = y;
 
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode([screen_width, screen_height])

playing = True;
 
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()

player = Player(red)
all_sprites_list.add(player)

wall = Wall(blue)
all_sprites_list.add(wall)

movescale = 5;

while playing == True:

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False;
    if pressed[pygame.K_ESCAPE]:
        playing = False;

    if pressed[pygame.K_d]:
        self.rect.x = self.rect.x + movescale;
    elif pressed[pygame.K_a]:
        self.rect.x = self.rect.x - movescale;
    if pressed[pygame.K_w]:
        self.rect.y = self.rect.y - movescale;
    elif pressed[pygame.K_s]:
        self.rect.y = self.rect.y + movescale;

    screen.fill(white)

    all_sprites_list.draw(screen)
    all_sprites_list.update()
     
    clock.tick(60)
    pygame.display.flip()
 
pygame.quit()