import pygame
import random
import time


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fish Simulator")
clock = pygame.time.Clock()
#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
numClicks = 1

class Fish:
    def __init__(self):
        self.fishImage = pygame.image.load("fishsilver.png").convert_alpha()
        self.fishImage = pygame.transform.scale(self.fishImage, (40,40))
        pygame.Surface.set_colorkey (self.fishImage, [255,0,255])
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        self.speed = 1
        self.xDir = random.randint(-1,1)
        self.yDir = random.randint(-1,1)
        self.last_change_time = time.time() #grab starting time

    def move(self):
        # Move the fish
        self.xpos += self.xDir* self.speed
        self.ypos += self.yDir * self.speed

        # Change direction every 3 seconds
        if time.time() - self.last_change_time > 3:  
            self.xDir = random.randint(-1,1)
            self.yDir = random.randint(-1,1)
            self.last_change_time = time.time() #reset the time

        # Check for collision with walls and change direction
        if self.xpos <= 0 or self.xpos >= 750:
            self.xDir *= -1
        if self.ypos <= 0 or self.ypos>= 550:
            self.yDir *= -1

    def draw(self, screen):
        screen.blit(self.fishImage, (self.xpos, self.ypos))

class jellyfish:
    def __init__ (self):
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        self.xv = 1
        self.yv = 1
        self.last_boost_time = time.time()
    def move (self):
        self.xpos += self.xv
        self.ypos += self.yv

        if time.time() - self.last_boost_time > 5:
            self.yv = -5
            self.last_boost_time = time.time()
        if self.ypos < 20:
            self.yv = 1

            

        
        if self.xpos <= 0 or self.xpos >= 800:
            self.xv *= -1
        if self.ypos >= 550:
            self.yv = -100
              
            
    def draw(self):
        pygame.draw.rect(screen,(255,0,250), (self.xpos, self.ypos, 25 ,25))

jelly = []



# instantiate a fish object
fishes = []

running = True
while running:# Game loop########################################################
    clock.tick(60)
    print(mousePos)

    #input/event section-----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >500:
                numClicks += 1
                print(numClicks)
                fishes.append(Fish())
            elif mousePos[0] > 0 and mousePos[0] < 100 and mousePos[1] >500:
                jelly.append(jellyfish())
            elif mousePos[0] >50 and mousePos[0] < 150 and mousePos[1] >500:
                print("REMOVEEOEOOEOEOEO")
                fishes.pop(-1)
            elif mousePos[0] >50 and mousePos[0] < 200 and mousePos[1] >500:
                jelly.pop(-1)
                
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos       
            

    #physics/update section--------------------------
    for i in range(len(fishes)):
        fishes[i].move()
    for j in range(len(jelly)):
        jelly[j].move()

    #render section----------------------------------
    # Fill the screen with a background color
    screen.fill((0, 150, 255))
    pygame.draw.rect(screen, (192,192,192), (0, 500, 50, 100))
    pygame.draw.rect(screen, (255,0,200), (50, 500, 50, 100))
    pygame.draw.rect(screen, (255,0,0), (100, 500, 50, 100))
    pygame.draw.rect(screen, (200,0,0), (150, 500, 50, 100))

    # Draw the fish
    for i in range(len(fishes)):
        fishes[i].draw(screen)
    for j in range(len(jelly)):
        jelly[j].draw()

    # Update the display
    pygame.display.flip()

    #end of game loop!#######################################################

pygame.quit()
