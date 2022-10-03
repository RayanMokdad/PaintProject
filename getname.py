from pygame import *
from glob import *

''' -------------------------------------------------------------
    getName
    -------------------------------------------------------------
    Because pygame likes to crash you can copy and paste my getName
    function into your program and use it, free of charge.  You
    may want to change the size of the rectange, it's location, the
    font, and the colour so that it matches your program.
    ------------------------------------------------------------- '''
def getName(screen,showFiles):
    ans = ""                    # final answer will be built one letter at a time.
    comicFont = font.SysFont("Comic Sans MS", 40)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(285,690,410,50) # make changes here.

    if showFiles:
        pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
        n = len(pics)
        choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
        draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
        for i in range(n):
            txtPic = arialFont.render(pics[i], True, (0,111,0))   #
            screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))

    cursorShow = 0
    myclock = time.Clock()
    typing = True
    while typing:
        cursorShow += 1
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                
                    
        txtPic = comicFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,250,245),textArea)        # draw the text window and the text.
        draw.rect(screen,(127,210,250),textArea,4)            
        screen.blit(txtPic,(textArea.x+7,textArea.y+10))
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x+txtPic.get_width()+10
            cy = textArea.y+4
            draw.rect(screen,(255,0,0),(cx,cy,2,textArea.height-6))
        if len(ans)>25:
            typing=False
        
        myclock.tick(100)
        display.flip()
    if len(ans)<5:
        typing = False
    screen.blit(back,(0,0))
    return ans
       
