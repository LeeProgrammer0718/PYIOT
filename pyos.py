import pygame
#import pygame_textinput #text input
import datetime
import os
import pygame_textinput #text input module

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode([width, height],pygame.RESIZABLE)
pygame.display.set_caption("PYOS")
#textinput = pygame_textinput.TextInput()
#Color
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (103,153,255)
GREY = (166,166,166)
BLACK_A = (0,0,0,50) #반투명 black

class button:
    def __init__(self,screen,size): # size -->(width,height)
        self.width = size[0]
        self.height = size[1]
        self.screen = screen
    def Buttongenerate(self,TEXT,POS,COLOR):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        font = pygame.font.Font(None,self.height//2)
        text = font.render(TEXT,True,(0,0,0))
        textsize = font.size(TEXT)
        TEXTPOS = [POS[0]+(self.width-textsize[0])/2,POS[1]+(self.height-textsize[1])/2]
        self.screen.blit(text,TEXTPOS)
        pygame.draw.polygon(self.screen, COLOR, [[POS[0],POS[1]],[POS[0]+self.width,POS[1]],[POS[0]+self.width,POS[1]+self.height],[POS[0],POS[1]+self.height]], 5)
        if POS[0]+self.width> mouse[0] > POS[0] and  POS[1]+self.height> mouse[1] > POS[1]:
            if click[0]==1:
                return True #버튼 클릭했는지 확인
        else :
            return False #ok
    def imagebutton(self,image,POS,appname): #POS --> (width,height) #appname-->popupnotification , if appname=None is not work
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        image = pygame.transform.scale(image,(self.width,self.height))
        slef.screen.blit(image,POS)
        if POS[0]+self.width> mouse[0] > POS[0] and  POS[1]+self.height> mouse[1] > POS[1]:
            if appname != 'None':
                return 0
            if click[0]==1:
                return True #버튼 클릭했는지 확인


def TEXT(TEXTSIZE,TEXT,TEXTCOLOR,TEXTPOS,FONT):
    font = pygame.font.SysFont(FONT,TEXTSIZE)
    text = font.render(TEXT,True,TEXTCOLOR)
    screen.blit(text,TEXTPOS)

def TEXTSIZE(TEXTSIZE,TEXT,FONT):
    font = pygame.font.SysFont(FONT,TEXTSIZE)
    textsize = font.size(TEXT)
    return textsize

def BOX(SIZE,COLOR,POS,WIT): #SIZE --> (width,height) #CODE --> 박스안 내용 추가
    #POS --> (w,h)
    # WIT ==>테두리, None이면 fill
    if WIT == 'None':
        WIT = 0
    pygame.draw.polygon(screen,COLOR,((POS[0],POS[1]),(POS[0]+SIZE[0],POS[1]),(POS[0]+SIZE[0],POS[1]+SIZE[1]),(POS[0],POS[1]+SIZE[1])),WIT)


def popupnotification(POS,text): #POPUPMENU
    textsize = TEXTSIZE(screen.get_width()//45,text,'NotoSansCJKkr-Light')
    BOX((textsize[0]+6,screen.get_width()//45+6),BLACK_A,POS,'None')
    TEXT(screen.get_width()//45,text,WHITE,(POS[0]+3,POS[1]+3),'NotoSansCJKkr-Light')

def imagebutton(size,image,POS,appname): #POS --> (width,height) #appname-->popupnotification , if appname=None is not work
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    image = pygame.transform.scale(image,size)
    screen.blit(image,POS)
    if POS[0]+size[0]> mouse[0] > POS[0] and  POS[1]+size[1]> mouse[1] > POS[1]:
        if appname != 'None':
            popupnotification(mouse,appname)
        if click[0]==1:
            return True #버튼 클릭했는지 확인

def Timewidget(SIZE,TEXTCOLOR,BGCOLOR,POS,WIT): # SIZE --> (width,height)
    dt = datetime.datetime.now()
    hour = dt.hour
    min = dt.minute
    sec = dt.second
    day = dt.strftime("%A %d. %B %Y")
    timetextsize = TEXTSIZE(SIZE[1]//3,"{}:{}".format(hour,min),"NotoSansCJKkr-Light")
    daytextsize = TEXTSIZE(SIZE[1]//10,"{}".format(day),"NotoSansCJKkr-Light")
    BOX(SIZE,BGCOLOR,POS,WIT)
    textpos = (POS[0]+(SIZE[0]-timetextsize[0])//2,POS[1]+timetextsize[1]//2)
    TEXT(SIZE[1]//3,"{}:{}".format(hour,min),TEXTCOLOR,textpos,"NotoSansCJKkr-Light")
    TEXT(SIZE[1]//10,"{}".format(day),TEXTCOLOR,(POS[0]+(SIZE[0]-daytextsize[0])//2,textpos[1]+daytextsize[1]*4),"NotoSansCJKkr-Light")

def APPS(TEXTCOLOR,BGCOLOR,POS,WIT):
    appiconimage = [] #앱아이콘 저장 확장자는 무조건 png 아이콘 이름은 앱이름으로
    BOX((screen.get_width()//2,screen.get_height()//20),BGCOLOR,POS,WIT)
    TEXT(screen.get_height()//30,'APPS',TEXTCOLOR,(POS[0]+10,POS[1]),'NotoSansCJKkr-Regular')
    apppath = 'apps'
    try:
        applist = os.listdir(apppath)
        for filename in applist:
            iconpath ='apps/'+filename+'/'+filename+'.png'
            appiconimage.append(iconpath)
            #print(iconpath)
    except:
        print("apps 폴더가 없음")

    try:
        x = POS[0]+screen.get_height()//9 #이미지 배치 시작 x좌표
        i = 0 #앱이름 인덱스
        for icon in appiconimage:
            loadicon = pygame.image.load(icon)
            if imagebutton((screen.get_height()//30,screen.get_height()//30),loadicon,(x,POS[1]+6),applist[i]): #앱버튼 배열
                print('buttonpush')
            i+=1
            x += screen.get_height()//25
    except:
        print("이미지 불러오기 실패")


def musicapp(SIZE,TEXTCOLOR,BGCOLOR,POS,WIT):
    return 0

def start(bool,screen):
    but = button(screen,(screen.get_width()//4,screen.get_height()//7))
    startlevel = 0 #시작 진행단계
    textinput = pygame_textinput.TextInput()
    clock = pygame.time.Clock()
    while bool:
        screen.fill(WHITE)
        events = pygame.event.get()
        if startlevel == 0:
            textsize = TEXTSIZE(screen.get_height()//6,"HELLO","NotoSansCJKkr-Light")
            TEXT(screen.get_height()//6,"HELLO",BLACK,((screen.get_width()-textsize[0])//2,(screen.get_height()-textsize[1])//3),"NotoSansCJKkr-Light")
            if but.Buttongenerate("LET's START", ((screen.get_width()-screen.get_width()//4)//2,
            (screen.get_height()-screen.get_height()//7)//5) ,BLACK):
                startlevel = 1
        elif startlevel == 1 :
            textsize = TEXTSIZE(screen.get_height()//6,"What Your name?","NotoSansCJKkr-Light")
            TEXT(screen.get_height()//6,"What Your name?",BLACK,((screen.get_width()-textsize[0])//2,(screen.get_height()-textsize[1])//3),"NotoSansCJKkr-Light")
            textinput.update(events)
            screen.blit(textinput.get_surface(), (50, 10))

        pygame.display.update()
        clock.tick(30)
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
                screen = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)

def main(bool,screen,bg):
    wallpaper = ['bg1.jpg','bg2.jpg','bg3.jpg','bg4.jpg','bg5.jpg']
    imagenum = 0
    menu = pygame.image.load("menu.png")
    backgroundchange = pygame.image.load("background.png")
    background = pygame.image.load(wallpaper[4])
    apps = 0 #if 앱스 버튼 클릭-->1
    while bool:
        #background = pygame.image.load(wallpaper[4])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.fill(BLACK)
        bac = pygame.transform.scale(background, (screen.get_width(),screen.get_height()))
        men = pygame.transform.scale(menu,(screen.get_width()//40,screen.get_width()//40))
        bacchange = pygame.transform.scale(backgroundchange,(screen.get_width()//40,screen.get_width()//40))#배경바꾸기 버튼이미지
        screen.blit(bac,(0,0)) #배경이미지 설정

        screen.blit(men,(screen.get_width()//18,screen.get_height()-screen.get_width()//16))
        screen.blit(bacchange,(screen.get_width()//18*2,screen.get_height()-screen.get_width()//16))

        Timewidget((screen.get_width()//2,screen.get_height()//2),BLACK,WHITE,
        ((screen.get_width()-screen.get_width()//2)//2,(screen.get_height()-screen.get_height()//2)//2),'None')

        if screen.get_width()//18+screen.get_width()//40> mouse[0] > screen.get_width()//18 \
        and  screen.get_height()-screen.get_width()//16+screen.get_width()//40> mouse[1] > screen.get_height()-screen.get_width()//16:
            popupnotification((mouse[0],mouse[1]),'APPS')
            if click[0]==1:
                if apps == 0:
                    apps = 1
                #print(True) #앱스버튼 눌릴 시 실행

        elif screen.get_width()//18*2+screen.get_width()//40> mouse[0] > screen.get_width()//18*2 \
        and  screen.get_height()-screen.get_width()//16+screen.get_width()//40> mouse[1] > screen.get_height()-screen.get_width()//16:
            popupnotification((mouse[0],mouse[1]),'WALLPAPER')
            if click[0]==1:
                print(True) #웰페이퍼변경버튼 눌릴 시 실행

        elif (screen.get_width()-screen.get_width()//2)//2+screen.get_width()//2> mouse[0] > (screen.get_width()-screen.get_width()//2)//2 \
        and  screen.get_height()-screen.get_height()//4+screen.get_height()//20 > mouse[1] > (screen.get_height()-screen.get_height()//2)//2:

            print(False)

        else:
            if click[0]==1:
                apps = 0
                #print(True)

        if apps != 0:
            APPS(BLACK,WHITE,((screen.get_width()-screen.get_width()//2)//2,(screen.get_height()-screen.get_height()//4)),'None')


        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
                screen = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
if __name__ == '__main__':
    #start(True,screen)
    main(True,screen,"None")
