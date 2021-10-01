from model import createModel
from display import *
import pygame



def runInterface():
    pygame.init()
    window = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("CasquOpt")
    running = True
    resultsOn = False
    page = 0
    shipping = []

    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.QUIT])

    while running:

        events= pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hitboxes[0].collidepoint(event.pos):
                    page = (page-1)%3
                elif hitboxes[1].collidepoint(event.pos):
                    page = (page+1)%3
                elif hitboxes[2].collidepoint(event.pos):
                    resultsOn = True
                    model , shipping = createModel()
                    model.optimize()

        hitboxes = drawInterface(window,shipping,page,resultsOn)
        pygame.display.update()

    pygame.display.quit()



def drawInterface(window,shipping,page,resultsOn):
    cellWidth = 80
    cellHeight = 50
    nameWidth = 220

    window.fill((70,215,250))
    drawTable(window,30,30,cellWidth,cellHeight,nameWidth,page)
    if resultsOn:
        fillTable(window,30,30,cellWidth,cellHeight,nameWidth,page,shipping)
    text(window,"page "+str(page+1),20,(0,0,0),"midbottom",30+5+100,30+480)
    hitboxes = [text(window,"<<",20,(0,0,0),"bottomleft",30+5,30+480),text(window,">>",20,(0,0,0),"bottomright",30+5+200,30+480)]
    hitboxes += [drawButton(window,30,30)]

    return hitboxes
