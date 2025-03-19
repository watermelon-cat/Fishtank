#alejandro, dean, jose, jovaun, nat
import pygame
import random
import time


pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Fish Simulator")
clock = pygame.time.Clock()
#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
numClicks = 1

#bikinibottom houses
spongebobhouse = pygame.image.load("spongehouse.png").convert_alpha()
spongebobhouse = pygame.transform.scale(spongebobhouse, (300, 300))
pygame.Surface.set_colorkey (spongebobhouse, [255,0,255])

patrickhouse = pygame.image.load("patrickrock2.png").convert_alpha()
patrickhouse = pygame.transform.scale(patrickhouse, (260, 260))
pygame.Surface.set_colorkey (patrickhouse, [255,0,255])

squidhouse = pygame.image.load("squidwardhouse.png").convert_alpha()
squidhouse = pygame.transform.scale(squidhouse, (500, 500))
pygame.Surface.set_colorkey (squidhouse, [255,0,255])

#sand
sizes1 = []
positions1 = []
colors1 = []

for i in range(25000):
    sizes1.append(random.randrange(2,5)) #push in 1 number
    positions1.append((random.randrange(0, 1000),random.randrange(650, 700))) #push in a 2-slot TUPLE #fist is xpos 2nd is y pos
    colors1.append((random.randrange(185,200),random.randrange(170,180),random.randrange(125,135))) #push in a 3-slot TUPLE


class Fish:
    def __init__(self):
        self.fishx = random.randint(40, 65)
        self.fishy = random.randint(30, 55)
        self.fishImage = pygame.image.load("fishsilver.png").convert_alpha()
        self.fishImage = pygame.transform.scale(self.fishImage, (self.fishx ,self.fishy))
        pygame.Surface.set_colorkey (self.fishImage, [255,0,255])
        self.fishImageleft = pygame.image.load("silverfishleft.png").convert_alpha()
        self.fishImageleft = pygame.transform.scale(self.fishImageleft, (self.fishx ,self.fishy))
        pygame.Surface.set_colorkey (self.fishImageleft, [255,0,255])
        self.xpos = random.randint(0, 950)
        self.ypos = random.randint(0, 640)
        self.speed = random.randint(1,2)
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
        if self.xpos <= 0 or self.xpos >= 950:
            self.xDir *= -1
        if self.ypos <= 0 or self.ypos>= 640:
            self.yDir *= -1

    def draw(self, screen):
        if self.xDir == 1:
            screen.blit(self.fishImage, (self.xpos, self.ypos))
        else:
            screen.blit(self.fishImageleft, (self.xpos, self.ypos))
            
class jellyfish:
    def __init__ (self):
        self.xpos = random.randint(0, 950)
        self.ypos = random.randint(0, 640)
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

            

        
        if self.xpos <= 0 or self.xpos >= 950:
            self.xv *= -1
        if self.ypos >= 640:
            self.yv = -100
              
            
    def draw(self):
        pygame.draw.rect(screen,(255,0,250), (self.xpos, self.ypos, 25 ,25))

jelly = []


class Fishfood:
    def __init__(self):
        self.xpos = -10
        self.ypos = -10
        self.isAlive = False
        self.foodImage = pygame.image.load("krabbypatty.png").convert_alpha()
        self.foodImage = pygame.transform.scale(self.foodImage, (20 ,20))
        pygame.Surface.set_colorkey (self.foodImage, [255,0,255])
    def move(self):
        if self.isAlive == True: #only shoot live bullets
            self.ypos += 1 #move down when shot
        else:
            self.xpos = -10
            self.ypos = -10
        if self.ypos > 660: #check if you've hit the bottom of the screen
            self.isAlive = False #set to dead
            self.xpos = -10 #reset to offscreen positoin
            self.ypos = -10
        
    def draw(self):
        if self.isAlive:
            #pygame.draw.rect(screen, (235, 174, 52), (self.xpos, self.ypos, 10, 10))
            screen.blit(self.foodImage, (self.xpos, self.ypos))


# instantiate a object
fishes = []
food = []
for i in range(1):
    food.append(Fishfood())

running = True
while running:# Game loop########################################################
    clock.tick(60)
    print(mousePos)

    #input/event section-----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >700:
                numClicks += 1
                print(numClicks)
                fishes.append(Fish())
            elif mousePos[0] >50 and mousePos[0] < 100 and mousePos[1] >700 and len(fishes) >= 1:
                print("REMOVEEOEOOEOEOEO")
                fishes.pop(-1)
            elif mousePos[0] > 100 and mousePos[0] < 150 and mousePos[1] >700:
                jelly.append(jellyfish())
            elif mousePos[0] >150 and mousePos[0] < 200 and mousePos[1] >700 and len(jelly) >= 1:
                jelly.pop(-1)
            
            if mousePos[0] > 0 and mousePos[0] < 1000 and mousePos[1] <700:
                for i in range (len(food)):#find the first llive missile to move
                    if food[i].isAlive == False:#only fire missiles that aren't already goind
                        food[i].isAlive = True#set it to alive
                        food[i].xpos = mousePos[0]#set the missile position to the aliens posistion
                        food[i].ypos = mousePos[1]
                        break
                    
                print("FOD")
                
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
                                
    for i in range (len(food)):
        for k in range(len(fishes)):
            if food[i].isAlive:
                if food[i].xpos != fishes[k].xpos:
                    if food[i].xpos > fishes[k].xpos:
                        fishes[k].xpos += 3
                        fishes[k].xDir = 1
                    elif food[i].xpos < fishes[k].xpos:
                        fishes[k].xpos -= 3
                        fishes[k].xDir = -1
                else:
                    fishes[k].xpos = food[i].xpos
                if food[i].ypos != fishes[k].ypos:
                    if food[i].ypos > fishes[k].ypos:
                        fishes[k].ypos += 3
                        fishes[k].yDir = 1
                    elif food[i].ypos < fishes[k].ypos:
                        fishes[k].ypos -= 3
                        fishes[k].yDir = -1
                else:
                    fishes[k].ypos = food[i].ypos
            
    for i in range (len(food)): # check for collision with each food in the list
        for k in range(len(fishes)):
            if food[i].isAlive: #only get hit by live food
                if food[i].xpos > fishes[k].xpos: #check if food is right of the left side of the fish
                    if food[i].xpos+20 < fishes[k].xpos + 40: # check is the food is left of the right side
                        if food[i].ypos+20 < fishes[k].ypos + 40: #check if the food is above the fish bottom
                            if food[i].ypos+20 > fishes[k].ypos: #check is the food is below the top of the fish
                                print("FOOD ATE") #for testing
                                #food.pop(-1)
                                food[i].isAlive = False
                                food[i].ypos = -10
                                food[i].xpos = -10
                                #time.sleep(1)
            

    #physics/update section--------------------------
    for i in range(len(fishes)):
        fishes[i].move()
    for j in range(len(jelly)):
        jelly[j].move()
    
    for i in range(len(food)):
        food[i].move()


    #render section----------------------------------
    # Fill the screen with a background color
    screen.fill((0, 150, 255))
        
    #draw the gravel
    for i in range(25000):
        pygame.draw.circle(screen, colors1[i], (positions1[i][0], positions1[i][1]), sizes1[i])
        
    pygame.draw.rect(screen, (201, 199, 189), (0, 700, 1000, 100)) #interface
    pygame.draw.rect(screen, (114, 114, 115), (0, 700, 50, 100)) #silver add
    pygame.draw.rect(screen, (217, 68, 65), (50, 700, 50, 100)) #silver remove
    pygame.draw.rect(screen, (230, 108, 230), (100, 700, 50, 100)) #jelly add
    pygame.draw.rect(screen, (217, 68, 65), (150, 700, 50, 100)) #jelly remove
    
    screen.blit(spongebobhouse, (650, 370))
    screen.blit(patrickhouse, (60, 500))
    screen.blit(squidhouse, (250, 300))
    
    # Draw the fish
    for i in range(len(fishes)):
        fishes[i].draw(screen)

    for j in range(len(jelly)):
        jelly[j].draw()
   
    for i in range (len(food)):
        food[i].draw()

    
    # Update the display
    pygame.display.flip()

    #end of game loop!#######################################################

pygame.quit()

