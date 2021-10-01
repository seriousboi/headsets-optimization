import pygame



def text(window,message,size,color,anchor,x,y):

    font = pygame.font.SysFont("courier new", size)
    text = font.render(message,True,color)
    area = text.get_rect()
    width= area.width
    height= area.height

    vect= {"topleft":[0,0],
           "bottomleft":[0,-2],
           "topright":[-2,0],
           "bottomright":[-2,-2],
           "midtop":[-1,0],
           "midleft":[0,-1],
           "midbottom":[-1,-2],
           "midright":[-2,-1],
           "center":[-1,-1]}

    x= x + vect[anchor][0]*width/2
    y= y + vect[anchor][1]*height/2

    return window.blit(text,(x,y))



def drawCost(window,x,y,status,cost):
    pygame.draw.rect(window,(245,105,255),(x,y,300,50),0)
    pygame.draw.rect(window,(150,150,150),(x,y,300,50),1)
    text(window,"coût transport: "+str(cost)+"€",20,(0,0,0),"center",x+150,y+25)



def drawFeasability(window,x,y,status):
    if status == "infeasible":
        pygame.draw.rect(window,(250,5,5),(x,y,250,50),0)
        pygame.draw.rect(window,(50,50,50),(x,y,250,50),1)
        text(window,"pas de solution",20,(0,0,0),"center",x+125,y+25)
    else:
        pygame.draw.rect(window,(135,235,190),(x,y,250,50),0)
        pygame.draw.rect(window,(150,150,150),(x,y,250,50),1)
        text(window,"solution réalisable",20,(0,0,0),"center",x+125,y+25)



def drawButton(window,x,y):
    hitbox = pygame.draw.rect(window,(250,200,5),(x,y,180,50),0)
    pygame.draw.rect(window,(225,150,0),(x,y,180,50),2)
    text(window,"optimiser",25,(0,0,0),"center",x+90,y+25)
    return hitbox



def drawTable(window,x,y,cellWidth,cellHeight,nameWidth,page):
    factoriesColor = (220,250,0)
    headsetsColor = (180,250,0)
    citiesColor = (0,250,200)
    cellsColor = (135,250,0)

    pygame.draw.rect(window,factoriesColor,(x+nameWidth,y,cellWidth*9,cellHeight),0)
    pygame.draw.rect(window,(150,150,150),(x+nameWidth,y,cellWidth*9,cellHeight),1)
    pygame.draw.rect(window,headsetsColor,(x+nameWidth,y+cellHeight,cellWidth*9,cellHeight),0)
    pygame.draw.rect(window,(150,150,150),(x+nameWidth,y+cellHeight,cellWidth*9,cellHeight),1)
    pygame.draw.rect(window,cellsColor,(x+nameWidth,y+cellHeight*2,cellWidth*9,cellHeight*7),0)
    pygame.draw.rect(window,(150,150,150),(x+nameWidth,y+cellHeight*2,cellWidth*9,cellHeight*7),1)
    pygame.draw.rect(window,citiesColor,(x,y+cellHeight*2,nameWidth,cellHeight*7),0)
    pygame.draw.rect(window,(150,150,150),(x,y+cellHeight*2,nameWidth,cellHeight*7),1)

    for i in range(1,7):
        pygame.draw.line(window,(150,150,150),(x,y+cellHeight*2+cellHeight*i),(x+nameWidth+cellWidth*9,y+cellHeight*2+cellHeight*i))
    for i in range(1,9):
        pygame.draw.line(window,(150,150,150),(x+nameWidth+cellWidth*i,y+cellHeight),(x+nameWidth+cellWidth*i,y+cellHeight*9))
    pygame.draw.line(window,(150,150,150),(x+nameWidth+cellWidth*3,y),(x+nameWidth+cellWidth*3,y+cellHeight))
    pygame.draw.line(window,(150,150,150),(x+nameWidth+cellWidth*6,y),(x+nameWidth+cellWidth*6,y+cellHeight))

    cityNames = ["Lille","Clichy","Reims","Amiens","Strasbourg","Rennes","Clermont","Orléans","Nantes","Besançon",
    "Vincennes","Marseille","Bordeaux","Dijon","Montpellier","Limoges","Metz","Toulouse","CaenS","Poitiers","Bayonne"]

    text(window,"Bordeaux",25,(0,0,0),"center",x+nameWidth+cellWidth*3/2,y+cellHeight/2)
    text(window,"Lyon",25,(0,0,0),"center",x+nameWidth+cellWidth*9/2,y+cellHeight/2)
    text(window,"Nanterre",25,(0,0,0),"center",x+nameWidth+cellWidth*15/2,y+cellHeight/2)

    for i in range(3):
        text(window,"Grosson",15,(0,0,0),"center",x+nameWidth+cellWidth*(1+i*6)/2,y+cellHeight*3/2)
        text(window,"Rapdeouf",15,(0,0,0),"center",x+nameWidth+cellWidth*(3+i*6)/2,y+cellHeight*3/2)
        text(window,"Zoukafon",15,(0,0,0),"center",x+nameWidth+cellWidth*(5+i*6)/2,y+cellHeight*3/2)

    for i in range(7):
        text(window,cityNames[i+page*7],20,(0,0,0),"center",x+nameWidth/2,y+cellHeight*(5+i*2)/2)



def fillTable(window,x,y,cellWidth,cellHeight,nameWidth,page,shipping):
    for factory in range(3):
        for city in range(7):
            for headset in range(3):
                text(window,str(int(shipping[factory][city+7*page][headset].x)),20,(0,0,0),"center",x+nameWidth+cellWidth/2+cellWidth*(headset+3*factory),y+cellHeight*5/2+cellHeight*city)
