import pygame as pg
#By adamsonacho on github!
dis = None
class sprite:
    """input -> size / optional: color"""

    def __init__(self,size,screen,color = None):
        sf = pg.Surface(size)
        rect = sf.get_rect()
        if color != None:
            sf.fill(color)
        self.screen = screen
        self.size = size
        self.rect = rect
        self.sf = sf
        self.sp = (self.sf,self.rect)
    def Disp(self):
        self.screen.blit(self.sf, self.rect)
class spritefi:
    def __init__(self,zoom,path,angle,screen):
        """input -> size, zoom, imagePath, rotationAngle"""
        sf_raw = pg.image.load(path).convert_alpha()
        sf = pg.transform.rotozoom(sf_raw,angle,zoom)
        rect = sf.get_rect(topleft = (0,0))
        self.screen = screen
        self.sf = sf
        self.rect = rect
        self.sp = (self.sf,self.rect)
    def Disp(self):
        self.screen.blit(self.sf, self.rect)
class text:
    def __init__(self,text,fontpath,Color,screen):
        """input -> text, pathOfFont,Color"""
        self.screen = screen
        self.fontpath = fontpath
        font = pg.font.Font(fontpath, 50)
        textsf = font.render(text,False,Color)
        textrect = textsf.get_rect()
        self.sf = textsf
        self.rect = textrect
        self.sp = (self.sf,self.rect)
    def Disp(self):
        self.screen.blit(self.sf, self.rect)
    def setText(self,text,color):
        font = pg.font.Font(self.fontpath, 50)
        self.sf = font.render(text,False,color)
        self.rect = self.sf
        self.sp = (self.sf,self.rect)
def Init(screenSize,bckColor):
    """input -> screen size, Color -> set background color / Returns Screen and background"""
    pg.init()
    dis = pg.display.set_mode(screenSize)
    if bckColor != None:
        Back = sprite(screenSize,dis,color=bckColor)
    return dis,Back
