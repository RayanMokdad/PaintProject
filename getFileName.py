from pygame import *
from getname import *
  
screen = display.set_mode((1000,800))
display.set_caption("Right Click to type")
font.init()                                 # must have this in your program for my font to work

comicFont = font.SysFont("Comic Sans MS", 20)

screen.fill((222,222,222))
running =True
y = 20
message = ""
while running:
    click = False
    
    for e in event.get():
        if e.type== MOUSEBUTTONDOWN:
            if e.button ==1:
                backcanvas= screen.copy()
        
            
        if e.type == QUIT:
            running = False
                
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if mb[2]==1:
        txt = getName(screen,False)                     # this is how you would call my getName function
                                            # your main loop will stop looping until user hits enter
        
    if mb[0]==1:
        screen.blit(backcanvas,(0,0))
        txtPic = comicFont.render(txt, True, (255,0,0))
        screen.blit(txtPic,(mx,my))

    display.flip()

font.quit()
del comicFont

quit()
