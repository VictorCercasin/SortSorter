import math

#Takes the screen, the list, and the width and height of the screen
#This should be called every time the list changes



def AlgDrawerRanderer(pygame, screen, list: list[int], drawerRectangle: list[int], info, alg):
    # drawerRectangle[x, y, width, heigh]
    font = pygame.font.Font('freesansbold.ttf', math.floor( drawerRectangle[3]/10))
    font2 = pygame.font.Font('freesansbold.ttf', math.floor( drawerRectangle[3]/10))
 
    # create a text surface object,
    # on which text is drawn on it.
    textAlg = font2.render( alg, True, (255, 0, 100))
    textComp = font.render("Comparisons: " + str(info['Comparisons']), True, (255, 0, 100))
    textSwap = font.render("Swaps: " + str(info['Swaps']), True, (255, 0, 100))
    
    # create a rectangular object for the
    # text surface object
    textAlgtRect = textComp.get_rect()
    textComptRect = textComp.get_rect()
    textSwapRect = textComp.get_rect()
    
    # set the center of the rectangular object.
    textAlgtRect.center = (drawerRectangle[0] + drawerRectangle[2]/5,drawerRectangle[1] +  drawerRectangle[3]/10,)
    textComptRect.center = ((drawerRectangle[0] + drawerRectangle[2]) - (drawerRectangle[0] + drawerRectangle[2])/5, drawerRectangle[1] +  drawerRectangle[3]/10)
    textSwapRect.center = ((drawerRectangle[0] + drawerRectangle[2]) - (drawerRectangle[0] + drawerRectangle[2])/5, drawerRectangle[1] +  2 * drawerRectangle[3]/10)
    widthUnit = drawerRectangle[2] / len(list)
    heightUnit = drawerRectangle[3] / max(list) - (drawerRectangle[3] / max(list))/20
    for i in range(len(list)):
        if info['Colors'][i] == 0:
            pygame.draw.rect(screen, (255, 255, 255), (drawerRectangle[0] + widthUnit * i, drawerRectangle[1] + drawerRectangle[3] - heightUnit * list[i], widthUnit, heightUnit * list[i]))
            # print("Cor: branco")
        if info['Colors'][i] == 1:
            pygame.draw.rect(screen, (255, 0, 0), (drawerRectangle[0] + widthUnit * i, drawerRectangle[1] + drawerRectangle[3] - heightUnit * list[i], widthUnit, heightUnit * list[i]))
            # print("Cor: Vermelho")
        if info['Colors'][i] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (drawerRectangle[0] + widthUnit * i, drawerRectangle[1] + drawerRectangle[3] - heightUnit * list[i], widthUnit, heightUnit * list[i]))
            # print("Cor: Verde")
        if info['Colors'][i] == 3:
            pygame.draw.rect(screen, (255,255,0), (drawerRectangle[0] + widthUnit * i, drawerRectangle[1] + drawerRectangle[3] - heightUnit * list[i], widthUnit, heightUnit * list[i]))
            # print("Cor: Amarelo")
    screen.blit(textAlg, textAlgtRect)
    screen.blit(textComp, textComptRect)
    screen.blit(textSwap, textSwapRect)

