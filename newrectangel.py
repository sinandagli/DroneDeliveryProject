import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving rectangle")

x = 200
y = 100
width = 1
height = 1
vel = 1
run = True
bitisx=100
bitisy=50
distancex = bitisx-x
distancey = bitisy-y
artısx=0
artısy=0

if(distancex > 0 & distancey > 0):
    if ((distancex) > distancey):
        artısx = distancex / distancey
        artısy = 1
    elif (distancex < distancey):
        artısy = distancey / distancex
        artısx = 1
    else:
        artısy = 1
        artısx = 1

elif (distancex > 0):
    if (distancex > distancey):
        artısx = distancex / distancey
        artısy = -1
    elif (distancex < distancey):
        artısy = distancey / distancex
        artısx = 1
    else:
        artısy = -1
        artısx = -1

elif (distancey > 0):
    if ((distancex) > distancey):
        artısx = distancex / distancey
        artısy = 1
    elif (distancex < distancey):
        artısy = distancey / distancex
        artısx = -1
    else:
        artısy = -1
        artısx = -1
else:
    if ((distancex) > distancey):
        artısx = -(distancex / distancey)
        artısy = -1
    elif (distancex < distancey):
        artısy = -(distancey / distancex)
        artısx = -1
    else:
        artısy = -1
        artısx = -1
xList=[]
yList=[]
image = pygame.image.load('images\square.png')
arrived=False
while run:
    if (arrived == False):
        pygame.time.delay(100)
        x=x+artısx
        y=y+artısy
        win.fill((0,0,0))

        for i in range(len(xList)):
            pygame.draw.rect(win, (255, 0, 0), (xList[i], yList[i], width, height))

        win.blit(image, (x, y))

        print(f'x= {x}, y={y}')
        xList.append(x+50)
        yList.append(y+50)
        pygame.display.update()

        if(float(x)==float(bitisx)):
            arrived=True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break















