from pygame import *


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

mixer.init()
mixer.music.load("jungles.ogg")

money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Monster(GameSprite):
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x <= 620:
            self.direction = "left"

        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.image = Surface((wall_width , wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, self.rect)

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN', True, (0,255,0))
lose = font.render('YOU LOSE', True, (255,0,0))

game = True
finish = False


player = Player('hero.png', 5, 420, 4)
monster = GameSprite('cyborg.png', 600, 280, 2)
final = GameSprite('treasure.png', 580, 400, 0) 
w1 = Wall(150,200,50,100,20,450,10)
w2 = Wall(150,200,50,100,100,10,5)
w3 = Wall(150,200,50,100,20,10,340)
w4 = Wall(150,200,50,100,100,10,360)
w5 = Wall(150,200,50,100,20,10,360)
w6 = Wall(150,200,50,100,20,10,360)
w7 = Wall(150,200,50,100,20,10,360)
w8 = Wall(150,200,50,100,20,10,360)
w9 = Wall(150,200,50,100,20,10,360)
w10 = Wall(150,200,50,100,20,10,360)






game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background,(0, 0))
    if not finish:
        player.reset()
        monster.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        monster.update()
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200,200))
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(lose, (200,200))
            money.play()

        player.update()        

    display.update()
    clock.tick(FPS)
