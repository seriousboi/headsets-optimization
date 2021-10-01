from model import createModel
from display import *
from mip import OptimizationStatus
import pygame



def runInterface():
    pygame.init()
    window = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("CasquOpt")
    running = True
    status = "noResults"
    cost = 0
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
                    model , shipping = createModel()
                    status = model.optimize()
                    if status == OptimizationStatus.OPTIMAL:
                        cost = int(model.objective_value)
                        status = "optimal found"
                    else:
                        status = "infeasible"

        hitboxes = drawInterface(window,shipping,page,status,cost)
        pygame.display.update()

    pygame.display.quit()



def drawInterface(window,shipping,page,status,cost):
    cellWidth = 80
    cellHeight = 50
    nameWidth = 220

    window.fill((70,215,250))
    drawTable(window,30,30,cellWidth,cellHeight,nameWidth,page)
    if status == "optimal found":
        fillTable(window,30,30,cellWidth,cellHeight,nameWidth,page,shipping)
        drawCost(window,650,500,status,cost)
        drawFeasability(window,300,500,status)
    elif status == "infeasible":
        drawFeasability(window,300,500,status)
    text(window,"page "+str(page+1),20,(0,0,0),"midbottom",30+5+100,30+480)
    hitboxes = [text(window,"<<",20,(0,0,0),"bottomleft",30+5,30+480),text(window,">>",20,(0,0,0),"bottomright",30+5+200,30+480)]
    hitboxes += [drawButton(window,30,30)]

    return hitboxes
