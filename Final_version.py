import random
import math
import pygame
pygame.init() #инициализация
size = 500
win = pygame.display.set_mode((size, size))  #создаем окно
pygame.display.set_caption("Game")

# класс еда

class Food (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Show(self):
        pygame.draw.rect(win, (250, 0, 0), (self.x - 5, self.y - 5, 10, 10))

    def was_eaten(self):
        self.x = random.randint(edge, size - edge)
        self.y = random.randint(edge, size - edge)

# класс точка

class Point (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# функция расстояния

def distance(a, b):
    return math.sqrt((a.x-b.x) ** 2 + (a.y - b. y) ** 2)

# функция "покушать"

def Eat(t, f):
    if distance(t, f) <= 5 + speed / 2:
        t.Tail()
        f.was_eaten()
        

#класс, где прописываются все функции
class Snake():
    def __init__(self, x, y, xspeed, yspeed, length, history, alive):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.length = length
        self.history = [Point (self.x, self.y)]
        self.alive = alive

#изменение положения и присваивание нужных координат
    def Upd(self):
        self.x += self.xspeed
        self.y += self.yspeed
        for i in range(self.length - 1, 0, -1):
            self.history[i].x = self.history[i-1].x            
            self.history[i].y = self.history[i-1].y
        self.history[0].x = self.x
        self.history[0].y = self.y

#контроль длины змеи
    def Tail(self):
        self.length += 1
        pos = Point(self.x, self.y)
        self.history.append(pos)
            
#рисуем
    def Show(self):
        for j in range(0, self.length):
            pygame.draw.rect(win, (250, 250, 250), (self.history[j].x - speed / 2, self.history[j].y - speed / 2, speed, speed))

#движение клавишами
    def Key_Pressed(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and (self.xspeed != 20):
            self.dir(-1, 0)
        if keys[pygame.K_d] and (self.xspeed != -20):
            self.dir(1, 0)
        if keys[pygame.K_w] and (self.yspeed != 20):
            self.dir(0, -1)
        if keys[pygame.K_s] and (self.yspeed != -20):
            self.dir(0, 1)
#направление
    def dir (self, x, y):
        self.xspeed = x * speed
        self.yspeed = y * speed

#случай на границе
    def on_edge(self):
        if self.x < 0:
            self.x = size
        elif self.x > size:
            self.x = 0
        elif self.y < 0:
            self.y = size
        elif self.y > size:
            self.y = 0

#змея умирает
    def ISDEAD(self):
        for i in range(1, self.length - 1):
            if distance (self.history[0], self.history[i]) == 0:
                game_over()

#Game over
def game_over():
    Tom.xspeed = 0
    Tom.yspeed = 0
    Tom.alive = False
    print()
    print("-----------GAME___OVER------------")
    print()
    print("Your length was", Tom.length)


Tom = Snake (size / 2, size / 2, 0, 0, 1, [], True)
edge = 25
A = Food (random.randint(edge, size - edge), random.randint(edge, size - edge))
speed = 20


#начало игры

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
# update
    if (Tom.alive):
        win.fill((0, 0, 0))
        Tom.Key_Pressed()
        Eat(Tom, A)
        A.Show()
        Tom.Show()
        Tom.Upd()
        Tom.on_edge()
        Tom.ISDEAD()
        pygame.display.update()
    
            
pygame.quit()
