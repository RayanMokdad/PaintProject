#Rayan Mokdad
#suCUTElent paint project
#This program allows users to draw,decorate and play around with their own canvas. This program includes:
#A paintbrush, pencil, spraycan, eraser, elipse, filled elipse, rectangle, filled rectangle,
#load, save and stamp tools.
#It also includes extra tools including:
#
#
from math import *
from pygame import *
from random import *
from tkinter import *
from getname import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
font.init()
from sys import platform
print(platform)


root = Tk()             
root.withdraw()#hides extra window
init()

import os
if "win" in platform:
    os.environ['SDL_VIDEO_WINDOW_POS'] = '0,100'#so screen stays same place
else:
    os.environ['SDL_VIDEO_WINDOW_POS'] = '120,0'
size=width,height= 1200,700
screen=display.set_mode(size)

#colours
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(127,210,250)
CC=black

#music
wahooS = mixer.Sound("wahoo.wav")
woohooS = mixer.Sound("woohoo.wav")
yohoS = mixer.Sound("yoho.wav")
mhmS = mixer.Sound("mhm.wav")
fartS = mixer.Sound("fart.wav")
mamaS = mixer.Sound("mama.wav")
button = mixer.Sound("button.wav")
mixer.music.load("music.mp3")
mixer.music.play(-1) #plays the sound track on loop


#full background
back=image.load("background4.jpg")
backbig=transform.smoothscale(back,(1200,800))
screen.blit(backbig, (0, 0))

#title
title=image.load("title6.png")
title=transform.smoothscale(title,(600,450))
screen.blit(title,(258,-195))

#canvas
canvasrect=Rect(150,115,800,560)
whiteb=image.load("white.jpg")
whiteb=transform.smoothscale(whiteb,(800,560))
screen.blit(whiteb, (150,115))
#draw.rect(screen,black,(147,112,805,565),4)

#wheel
wheel=image.load("wheel.png")
draw.circle(screen,0,(1076,150),95)
colourwheel=transform.smoothscale(wheel,(198,198))
screen.blit(colourwheel, (985, 59))

#black colour box button
blackRect=Rect(1150,210,40,40)
draw.rect(screen,black,blackRect)
draw.rect(screen,white,blackRect,2)

#DEFINING RECTS
#tool rects
paintbrushRect= Rect(990,255,75,75)
spraycanRect=Rect(990,345,75,75)
eraserRect=Rect(1090,255,75,75)
pencilRect=Rect(1090,345,75,75)
lineRect=Rect(990,435,75,75)
squarefilledRect=Rect(990,525,75,75)
ovalfilledRect=Rect(990,615,75,75)
squareunfilledRect=Rect(1090,525,75,75)
ovalunfilledRect=Rect(1090,615,75,75)
highlightRect=Rect(1090,435,75,75)
diceRect=Rect(1040,703,70,70)
#sticker rects
cutesuccRect=Rect(35,110,75,75)
cactusRect=Rect(35,203,75,75)
smilesuccRect=Rect(35,296,75,75)
pinksuccRect=Rect(35,389,75,75)
awwsuccRect=Rect(35,482,75,75)
familyRect=Rect(35,574,75,75)
#undo redo rects 
undoRect=Rect(145,688,50,50)
redoRect=Rect(210,688,50,50)
#extra tool rects
saveRect=Rect(898,688,50,50)
loadRect=Rect(838,688,50,50)
clearRect=Rect(778,688,50,50)
fillRect=Rect(718,688,50,50)
#sound rects
soundoffRect=Rect(20,40,45,45)
soundonRect=Rect(80,40,45,45)


#TOOL BUTTONS
#PaintBrush button           
draw.rect(screen,white,paintbrushRect)
draw.rect(screen,black,paintbrushRect,4)
brush=image.load("paintbrush.png")
brush=transform.smoothscale(brush,(71,66))
screen.blit(brush, (993, 259))

#Spraycan button                           
draw.rect(screen,white,spraycanRect)
draw.rect(screen,black,spraycanRect,4)
spraycan=image.load("spraycan.jpg")
spraycan=transform.smoothscale(spraycan,(70,67))
screen.blit(spraycan, (993, 349))

#line button
draw.rect(screen,white,lineRect)
draw.rect(screen,black,lineRect,4)
draw.line(screen,black,(1000,440),(1054,505),9)

#Square Filled button                          
draw.rect(screen,white,squarefilledRect)
draw.rect(screen,black,squarefilledRect,4)
draw.rect(screen,black,(998,533,60,60))

#Oval Filled button
draw.rect(screen,white,ovalfilledRect)
draw.rect(screen,black,ovalfilledRect,4)
ovalfilled=image.load("oval.png")
ovalfilled=transform.smoothscale(ovalfilled,(68,65))
screen.blit(ovalfilled, (994, 619))

#Eraser button
draw.rect(screen,white,eraserRect)
draw.rect(screen,black,eraserRect,4)
eraser=image.load("eraser.png")
eraser=transform.smoothscale(eraser,(65,60))
screen.blit(eraser, (1095, 263))
                            
#Pencil button                          
draw.rect(screen,white,pencilRect)
draw.rect(screen,black,pencilRect,4)
pencil=image.load("pencil.png")
pencil=transform.smoothscale(pencil,(65,60))
screen.blit(pencil, (1095, 352))

#Highlighter button
draw.rect(screen,white,highlightRect)
draw.rect(screen,black,highlightRect,4)
highlight=image.load("highlight.png")
highlight=transform.smoothscale(highlight,(65,65))
screen.blit(highlight, (1095, 441))

#Square Unfilled button                          
draw.rect(screen,white,squareunfilledRect)
draw.rect(screen,black,squareunfilledRect,4)
draw.rect(screen,black,(1098,533,60,60))
draw.rect(screen,white,(1102,537,52,52))

#Oval Unfilled button
draw.rect(screen,white,ovalunfilledRect)
draw.rect(screen,black,ovalunfilledRect,4)
ovalun=image.load("ovalunfilled.png")
ovalun=transform.smoothscale(ovalun,(68,65))
screen.blit(ovalun, (1094, 620))

#dice random colour generator button
draw.rect(screen,white,diceRect)
draw.rect(screen,black,diceRect,4)
dice=image.load("dice.png")
dice=transform.smoothscale(dice,(65,65))
screen.blit(dice,(1043,706))

#sticker Buttons
draw.rect(screen,white,cutesuccRect)
draw.rect(screen,0,cutesuccRect,4)
cutesucc=image.load("cutesucc.png")
smallcutesucc=transform.smoothscale(cutesucc,(67,62))
screen.blit(smallcutesucc, (39, 116))

draw.rect(screen,white,cactusRect)
draw.rect(screen,0,cactusRect,4)
cactus=image.load("cactus.png")
smallcactus=transform.smoothscale(cactus,(55,70))
screen.blit(smallcactus, (45, 206))

draw.rect(screen,white,smilesuccRect)
draw.rect(screen,0,smilesuccRect,4)
smilesucc=image.load("smilesucc.png")
smallsmilesucc=transform.smoothscale(smilesucc,(67,62))
screen.blit(smallsmilesucc, (39, 302))

draw.rect(screen,white,pinksuccRect)
draw.rect(screen,0,pinksuccRect,4)
pink=image.load("pinksucc.png")
pinksucc=transform.smoothscale(pink,(51,65))
screen.blit(pinksucc, (47, 394))

draw.rect(screen,white,awwsuccRect)
draw.rect(screen,0,awwsuccRect,4)
aww=image.load("awwsucc.png")
awwsucc=transform.smoothscale(aww,(83,71))
screen.blit(awwsucc, (31, 485))

draw.rect(screen,white,familyRect)
draw.rect(screen,0,familyRect,4)
family=image.load("family.png")
smallfamily=transform.smoothscale(family,(100,100))
screen.blit(smallfamily, (24, 563))

#UNDO Buttons
draw.rect(screen,white,undoRect)
draw.rect(screen,black,undoRect,4)
undo=image.load("undo.png")
undo=transform.smoothscale(undo,(50,50))
screen.blit(undo,(145,687))

#REDO Buttons
draw.rect(screen,white,redoRect)
draw.rect(screen,black,redoRect,4)
redo=image.load("redo.png")
redo=transform.smoothscale(redo,(50,50))
screen.blit(redo,(210,687))

#save Buttons
draw.rect(screen,white,saveRect)
draw.rect(screen,black,saveRect,4)
save=image.load("save.png")
save=transform.smoothscale(save,(40,40))
screen.blit(save,(903,693))

#load Buttons
draw.rect(screen,white,loadRect)
draw.rect(screen,black,loadRect,4)
load=image.load("load.png")
load=transform.smoothscale(load,(40,40))
screen.blit(load,(844,693))

#clear Tool Buttons
draw.rect(screen,white,clearRect)
draw.rect(screen,black,clearRect,4)
sweep=image.load("sweep.png")
sweep=transform.smoothscale(sweep,(40,40))
screen.blit(sweep,(784,693))

#fill Tool Buttons
draw.rect(screen,white,fillRect)
draw.rect(screen,black,fillRect,4)
fill=image.load("fill.png")
fill=transform.smoothscale(fill,(40,40))
screen.blit(fill,(724,693))

#Sound On Buttons
draw.rect(screen,white,(soundonRect))
draw.rect(screen,blue,(soundonRect),4)
Son=image.load("sound on.png")
Son=transform.smoothscale(Son,(37,37))
screen.blit(Son,(84,44))

#Sound Off Buttons
draw.rect(screen,white,(soundoffRect))
draw.rect(screen,black,(soundoffRect),4)
Soff=image.load("soundoff.png")
Soff=transform.smoothscale(Soff,(37,37))
screen.blit(Soff,(24,44))

#text
comicFont = font.SysFont("Comic Sans MS",40)
textRect=Rect(285,690,410,50)
draw.rect(screen,(220,250,245),(285,690,410,50))
draw.rect(screen,black,(285,690,410,50),4)
txt = comicFont.render("Enter Text Here:", True, (0,0,0))
comicFont2 = font.SysFont("Comic Sans MS",25)
txt2 = comicFont2.render("(limit 26 characters)", True, (0,0,0))
screen.blit(txt,(300,700))
screen.blit(txt2,(290,745))

#Undo Redo Lists
Ulist=[screen.subsurface(canvasrect).copy()]
Rlist=[]

picnames=["white.jpg","desert.jpg","backgroundpicnic.jpg","sunnybackground.jpg",
          "sunsetback.jpg","wood.jpg","cool.jpg","pibk.png"] #Loading background images
scaledpic=[]
for name in picnames: #adding backgrounds into a list
    pic=image.load(name)
    pic=transform.smoothscale(pic,(800,560))#scaling all the background images
    scaledpic.append(pic)
y = 20
text=False
message = ""
pos=0
size=10
start=0,0
tool="paintbrush"
running=True
while running:
    press=0
    click = False
    for evt in event.get():
        if evt.type== MOUSEBUTTONDOWN:
            if evt.button ==1:
                start= evt.pos
                sx,sy=mouse.get_pos()
                backcanvas= screen.copy()
                drawncanvas=False #makes sure screen only copies when something is drawn on the canvas
                press=1#so sound effects are only played when pressed once not continuesly
                if diceRect.collidepoint(mx,my):#random colour 
                    CC=((randint(0,255)),(randint(0,255)),(randint(0,255)))
                    draw.rect(screen,red,diceRect,4)#highlights when its being pressed down on
                    if press==1:#only plays sound when pressed on
                        button.play()
                        button.set_volume(0.5)
                if clearRect.collidepoint(mx,my):
                    screen.blit(scaledpic[pos],(150,115))#clears the canvas of changes by blitting the background again
                    draw.rect(screen,red,clearRect,4)
                    if press==1:
                        button.play()
                        button.set_volume(0.5)
                    drawncanvas=True
                if fillRect.collidepoint(mx,my):
                    draw.rect(screen,CC,canvasrect)
                    draw.rect(screen,red,fillRect,4)
                    if press==1:
                        button.play()
                        button.set_volume(0.5)
                    drawncanvas=True
                
            #controls size change of tools
            if evt.button == 5:
               size += 1
            if evt.button == 4:
               size -= 1
        #changes background of canvas when up and down arrow keys are pressed
        if evt.type==KEYDOWN:
            if evt.key==K_DOWN:
                n=len(scaledpic)
                pos=(pos+1)%n
                screen.blit(scaledpic[pos],(150,115))#blits the background on the list 
                drawncanvas=True
            if evt.key==K_UP:
                n=len(scaledpic)
                pos=(pos-1+n)%n
                screen.blit(scaledpic[pos],(150,115))
                drawncanvas=True
                
                
        if evt.type == MOUSEBUTTONUP or evt.type == KEYDOWN:
            pic=screen.subsurface(canvasrect).copy()#copies only subsurface canvas when mouse is up
            if drawncanvas==True:
                Ulist.append(pic)#adds the copied screen to undo list

        if evt.type == MOUSEBUTTONUP:
            click=True
            if undoRect.collidepoint(mx,my):
                if len(Ulist)>1:#if an action is done on canvas it will continue
                    undopic=Ulist[-1]
                    Ulist=Ulist[:-1]#gets rid of recent copied screen
                    Rlist.append(undopic)#adds recent copied screen to redo list
                screen.blit(Ulist[-1],(150,115))
            if redoRect.collidepoint(mx,my):
                if len(Rlist)>0:
                    redoCopy=Rlist.pop()#takes last value of Redo list
                    Ulist.append(redoCopy)#copies it to Undo list
                    screen.blit(redoCopy,(150,115))#blits last value of redo list to screen
            
            #unhighlights 
            draw.rect(screen,black,diceRect,4)
            draw.rect(screen,black,clearRect,4)
            draw.rect(screen,black,fillRect,4)
                
        #sets a limit to the size change of tools
        if size<1:
            size=1
        elif size>55:
            size=55     
            
        if evt.type==QUIT:
            running=False
#-----------------------------------------------------------------------

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    comicFont = font.SysFont("Comic Sans MS", size*2)
    
    if soundoffRect.collidepoint(mx,my) and mb[0]==1:
        mixer.music.set_volume(0.0) #mutes the music when pressed
        draw.rect(screen,blue,soundoffRect,4)
        draw.rect(screen,black,soundonRect,4)
        if press==1:
                    button.play()
                    button.set_volume(0.5)
        
        
    if soundonRect.collidepoint(mx,my) and mb[0]==1:
        mixer.music.set_volume(1.0)#music continues 
        draw.rect(screen,black,soundoffRect,4)
        draw.rect(screen,blue,soundonRect,4)
        if press==1:
                    button.play()
                    button.set_volume(0.5)
        

    #show size of tools
    draw.rect(screen,white,(14,661,117,117))
    draw.rect(screen,black,(14,661,117,117),4)
    draw.circle(screen,CC,(73,720),size)

    #unhighlight
    draw.rect(screen,black,pencilRect,4)
    draw.rect(screen,black,paintbrushRect,4)
    draw.rect(screen,black,eraserRect,4)
    draw.rect(screen,black,lineRect,4)
    draw.rect(screen,black,spraycanRect,4)
    draw.rect(screen,black,squarefilledRect,4)
    draw.rect(screen,black,ovalfilledRect,4)
    draw.rect(screen,black,squareunfilledRect,4)
    draw.rect(screen,black,ovalunfilledRect,4)
    draw.rect(screen,black,highlightRect,4)
    draw.rect(screen,black,cutesuccRect,4)
    draw.rect(screen,black,cactusRect,4)
    draw.rect(screen,black,smilesuccRect,4)
    draw.rect(screen,black,pinksuccRect,4)
    draw.rect(screen,black,awwsuccRect,4)
    draw.rect(screen,black,familyRect,4)
    draw.rect(screen,black,undoRect,4)
    draw.rect(screen,black,redoRect,4)
    draw.rect(screen,black,fillRect,4)
    draw.rect(screen,black,clearRect,4)
    draw.rect(screen,black,diceRect,4)
    draw.rect(screen,black,loadRect,4)
    draw.rect(screen,black,saveRect,4)
    draw.rect(screen,white,blackRect,4)
    

    #colour box shows what colour is in use
    draw.rect(screen,CC,(1133,15,50,50))
    draw.rect(screen,black,(1133,15,50,50),4)

    #colour wheel
    if mb[0]==1 and hypot(mx-1076,my-140)<=88:
        CC=screen.get_at((mx,my))
    elif mb[0]==1 and blackRect.collidepoint(mx,my):
        CC=black
        
        
        if press==1:
            button.play()
            button.set_volume(0.5)
            
    
#HIGHLIGHT
    if blackRect.collidepoint(mx,my):
        draw.rect(screen,red,blackRect,4)
        
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,red,loadRect,4)
         
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,red,saveRect,4)
        
    if fillRect.collidepoint(mx,my):
        draw.rect(screen,red,fillRect,4)
        
    if clearRect.collidepoint(mx,my):
        draw.rect(screen,red,clearRect,4)
        
    if diceRect.collidepoint(mx,my):
        draw.rect(screen,red,diceRect,4)
        
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,red,redoRect,4)

    if undoRect.collidepoint(mx,my):
        draw.rect(screen,red,undoRect,4)
        
    if tool=="pencil":
        draw.rect(screen,red,pencilRect,4)
        
    if tool=="paintbrush":
        draw.rect(screen,red,paintbrushRect,4)

    if tool=="eraser":
        draw.rect(screen,red,eraserRect,4)
        
    if tool=="spraycan":
        draw.rect(screen,red,spraycanRect,4)
        
    if tool=="line":
        draw.rect(screen,red,lineRect,4)

    if tool=="squarefilled":
        draw.rect(screen,red,squarefilledRect,4)
        
    if tool=="ovalfilled":
        draw.rect(screen,red,ovalfilledRect,4)

    if tool=="squareunfilled":
        draw.rect(screen,red,squareunfilledRect,4)
        
    if tool=="ovalunfilled":
        draw.rect(screen,red,ovalunfilledRect,4)

    if tool=="highlight":
        draw.rect(screen,red,highlightRect,4)
        
    if tool=="cutesucc":
        draw.rect(screen,red,cutesuccRect,4)
        
    if tool=="cactus":
        draw.rect(screen,red,cactusRect,4)
        
    if tool=="smilesucc":
        draw.rect(screen,red,smilesuccRect,4)

    if tool=="pinksucc":
        draw.rect(screen,red,pinksuccRect,4)
        
    if tool=="awwsucc":
        draw.rect(screen,red,awwsuccRect,4)
        
    if tool=="family":
        draw.rect(screen,red,familyRect,4)
    

#CHANGING TOOLS
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,red,pencilRect,4)#hover highlights 
        if mb[0]==1:
            tool="pencil"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif eraserRect.collidepoint(mx,my):
        draw.rect(screen,red,eraserRect,4)
        if mb[0]==1:
            tool="eraser"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif paintbrushRect.collidepoint(mx,my):
        draw.rect(screen,red,paintbrushRect,4)
        if mb[0]==1:
            tool="paintbrush"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif spraycanRect.collidepoint(mx,my):
        draw.rect(screen,red,spraycanRect,4)
        if mb[0]==1:
            tool="spraycan"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif lineRect.collidepoint(mx,my):
        draw.rect(screen,red,lineRect,4)
        if mb[0]==1:
            tool="line"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif squarefilledRect.collidepoint(mx,my):
        draw.rect(screen,red,squarefilledRect,4)
        if mb[0]==1:
            tool="squarefilled"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif ovalfilledRect.collidepoint(mx,my):
        draw.rect(screen,red,ovalfilledRect,4)
        if mb[0]==1:
            if press==1:
                    button.play()
                    button.set_volume(0.5)
            tool="ovalfilled"
    elif squareunfilledRect.collidepoint(mx,my):
        draw.rect(screen,red,squareunfilledRect,4)
        if mb[0]==1:
            tool="squareunfilled"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif ovalunfilledRect.collidepoint(mx,my):
        draw.rect(screen,red,ovalunfilledRect,4)
        if mb[0]==1:
            tool="ovalunfilled"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
    elif highlightRect.collidepoint(mx,my):
        draw.rect(screen,red,highlightRect,4)
        if mb[0]==1:
            tool="highlight"
            if press==1:
                    button.play()
                    button.set_volume(0.5)
                    
                  
    elif cutesuccRect.collidepoint(mx,my):
        draw.rect(screen,red,cutesuccRect,4)
        if mb[0]==1:
            tool="cutesucc"
    elif cactusRect.collidepoint(mx,my):
        draw.rect(screen,red,cactusRect,4)
        if mb[0]==1:
            tool="cactus"
    elif smilesuccRect.collidepoint(mx,my):
        draw.rect(screen,red,smilesuccRect,4)
        if mb[0]==1:
            tool="smilesucc"
    elif pinksuccRect.collidepoint(mx,my):
        draw.rect(screen,red,pinksuccRect,4)
        if mb[0]==1:
            tool="pinksucc"
    elif awwsuccRect.collidepoint(mx,my):
        draw.rect(screen,red,awwsuccRect,4)
        if mb[0]==1:
            tool="awwsucc"
    elif familyRect.collidepoint(mx,my):
        draw.rect(screen,red,familyRect,4)
        if mb[0]==1:
            tool="family"

    if textRect.collidepoint((mx,my)) and mb[0]==1:
        screen.set_clip(textRect)#makes sure text doesnt go out of text Rect
        if textRect.collidepoint(mx,my):
            if press==1:#makes sound when text Rect is pressed
                button.play()
                button.set_volume(0.5)
            if mb[0]==1:
                tool="text"
                txt = getName(screen,False)
                text=True
            if press==1:#makes sound when text is finished and is ready to be blit
                button.play()
                button.set_volume(0.5)     
        screen.set_clip(textRect)
        screen.set_clip(None)
        
                
    #make sure stays in the canvas
    if canvasrect.collidepoint((mx,my)) and mb[0]==1:
        screen.set_clip(canvasrect) 

        #USING TOOLS
        if tool=="pencil":
            draw.line(screen,CC,(omx,omy),(mx,my)) 
            drawncanvas=True
        
            
        elif tool=="eraser":
            dist=hypot(mx-omx,my-omy)
            dx=mx-omx
            dy=my-omy
            for i in range (int(dist)):
                cx=omx+i/dist*dx
                cy=omy+i/dist*dy
                draw.rect(screen,white,((cx-(size//2),cy-(size//2),size*2,size*2)))
            drawncanvas=True
            
        elif tool=="spraycan":
            for i in range(10):
                x=randint(mx-size,mx+size)
                y=randint(my-size,my+size)
                if hypot(mx-x,my-y)<size:
                    draw.circle(screen,CC,(x,y),0)
            drawncanvas=True
       
        elif tool=="paintbrush":
            dist=hypot(mx-omx,my-omy)
            dx=mx-omx
            dy=my-omy
            for i in range (int(dist)):
                cx=omx+i/dist*dx
                cy=omy+i/dist*dy
                draw.circle(screen,CC,(int(cx),int(cy)),size)
            drawncanvas=True
                
        elif tool=="line":
            screen.blit(backcanvas,(0,0))
            draw.line(screen,CC,start,(mx,my),size)
            drawncanvas=True

        elif tool=="squarefilled":
            screen.blit(backcanvas,(0,0))
            draw.rect(screen,CC,[sx,sy,(mx-sx),(my-sy)])
            drawncanvas=True

        elif tool=="ovalfilled":
            screen.blit(backcanvas,(0,0))
            r=Rect(sx,sy,(mx-sx),(my-sy))
            r.normalize() 
            draw.ellipse(screen,CC,(r))
            drawncanvas=True
            
        elif tool=="squareunfilled":
            screen.blit(backcanvas,(0,0))#have to blit the background so the rect can go on top
            for i in range (1,size+1): #emilinates the holes in the corner of the rectangle
                r1=Rect(sx,(sy+i),(mx-sx),(my-sy))
                r2=Rect((sx+i),sy,(mx-sx),(my-sy))
                r3=Rect(sx,sy,(mx-sx+i),(my-sy+i))
                r1.normalize()#makes sure its positive
                r2.normalize()
                r3.normalize()
                draw.rect(screen,CC,(r1),1)
                draw.rect(screen,CC,(r2),1)
                draw.rect(screen,CC,(r3),1)
                draw.rect(screen,CC,(sx,sy,size,size))
                draw.rect(screen,CC,(mx,my,size,size))
                draw.rect(screen,CC,(mx,sy,size,size))
                draw.rect(screen,CC,(sx,my,size,size))
            drawncanvas=True
                
        elif tool=="ovalunfilled":
            screen.blit(backcanvas,(0,0))#have to blit the background so the ellipse can go on top
            dx= (mx-sx)
            dy = (my-sy)
            for i in range(4):     #eliminates holes, using four ellipses (similar to rectangle)
                eRect = Rect(sx-i,sy,dx,dy) #defining the ellipse demensions in terms of a rectangle 
                eRect = Rect(sx+i,sy,dx,dy)
                eRect = Rect(sx,sy+i,dx,dy)
                eRect = Rect(sx,sy-i,dx,dy)
                eRect.normalize()      #normalize makes sure eRect is positive
                if eRect.height<size*2 or eRect.width<size*2:#if the height or the width of the rectangle is less than the diameter, it doesn't need a thickness
                    draw.ellipse(screen,CC,eRect)
                else:
                    draw.ellipse(screen,CC,eRect,size)
            drawncanvas=True

        elif tool=="highlight":
            hbrush = Surface((size*2,size*2))
            if size<25:
                hbrush.set_alpha(4)#sets transparancy
            if size>=25:#so its not too opaque
                hbrush.set_alpha(3)
            hbrush.fill(CC)
            if mx!=omx or my!=omy:
                dist=hypot(mx-omx,my-omy)
                dx=mx-omx
                dy=my-omy
                for i in range (int(dist)):
                    cx=omx+i/dist*dx
                    cy=omy+i/dist*dy
                    screen.blit(hbrush,((cx-(size//2),cy-(size//2))))
            drawncanvas=True
            
                    
        elif tool == "cutesucc":
            screen.blit(backcanvas,(0,0))
            bigcutesucc=transform.smoothscale(cutesucc,(size+70,size+65))
            screen.blit(bigcutesucc,((mx-((size+70)/2)),my-((size+65)/2)))
            if press==1:
                wahooS.play()
                wahooS.set_volume(0.5)
            drawncanvas=True
                
                
        elif tool == "cactus":
            screen.blit(backcanvas,(0,0))
            bigcactus=transform.smoothscale(cactus,(size+65,size+85))
            screen.blit(bigcactus,((mx-((size+65)/2)),my-((size+85)/2)))
            if press==1:
                woohooS.play()
                woohooS.set_volume(0.5)
            drawncanvas=True
                
        elif tool == "smilesucc":
            screen.blit(backcanvas,(0,0))
            bigsmilesucc=transform.smoothscale(smilesucc,(size+70,size+65))
            screen.blit(bigsmilesucc,((mx-((size+70)/2)),my-((size+65)/2)))
            if press==1:
                yohoS.play()
                yohoS.set_volume(0.5)
            drawncanvas=True
                
        elif tool == "pinksucc":
            screen.blit(backcanvas,(0,0))
            bigpinksucc=transform.smoothscale(pinksucc,(size+50,size+70))
            screen.blit(bigpinksucc,((mx-((size+50)/2)),my-((size+70)/2)))
            if press==1:
                fartS.play()
                fartS.set_volume(0.5)
            drawncanvas=True
                
        elif tool == "awwsucc":
            screen.blit(backcanvas,(0,0))
            bigawwsucc=transform.smoothscale(awwsucc,(size+90,size+78))
            screen.blit(bigawwsucc,((mx-((size+90)/2)),my-((size+78)/2)))
            if press==1:
                mhmS.play()
                mhmS.set_volume(0.5)
            drawncanvas=True

        elif tool == "family":
            screen.blit(backcanvas,(0,0))
            bigfamily=transform.smoothscale(family,(size+140,size+135))
            screen.blit(bigfamily,((mx-((size+140)/2)),my-((size+135)/2)))
            if press==1:
                mamaS.play()
                mamaS.set_volume(0.5)
            drawncanvas=True

        elif tool == "text":
            if text==True:
                if mb[0]==1:
                    screen.blit(backcanvas,(0,0))
                    txtPic = comicFont.render(txt, True, (CC))
                    screen.blit(txtPic,(mx-txtPic.get_width()/2, my-txtPic.get_height()/2))#blits text where mouse is 
                    drawncanvas=True
                    

    if click:
        if loadRect.collidepoint(mx,my):
            fname = askopenfilename(filetypes=[("Picture files","*.png;*.bmp;*.jpg;*.jpeg")])
            if fname!="":
                img=image.load(fname)
                img=transform.smoothscale(img,(800,560))
                screen.blit(img,canvasrect)
            
        elif saveRect.collidepoint(mx,my):
            fname = asksaveasfilename(defaultextension=".png")
            if fname!="":
                image.save(screen.subsurface(canvasrect),fname)
            
                
        screen.set_clip(canvasrect)

        

        screen.set_clip(None)

        
   
#------------------------------------------------------------------------
    omx,omy=mx,my
    display.flip()
    
font.quit()
del comicFont
                     
quit()
