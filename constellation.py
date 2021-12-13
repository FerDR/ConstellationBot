import numpy as np
from PIL import ImageDraw, ImageFont
import BotUtils as BU
import time

def get_points():
    n = np.random.poisson(10)+1
    x = []
    y = []
    color = []
    size = []
    for i in range(n):
        x.append(np.random.rand())
        y.append(np.random.rand())
        color.append(1)#Check actual distribution
        size.append(1)#Check actual distribution
    xys = []
    for X,Y in zip(x,y):
        xys.append((X,Y))
    return xys,color,size

def get_lines(xys):
    #haha yes
    return xy1s,xy2s

def get_name():
    #haha yes
    return name

def rotate(point,angle):
    x = point[0]*np.cos(angle)+point[1]*np.sin(angle)
    y = point[0]*np.sin(-angle)+point[1]*np.cos(angle)
    return (x,y)

def move(point,center):
    return (point[0]+center[0],point[1]+center[1]

def draw_star(draw,center,r,color):
    p1 = r*(0,2.62)
    p2 = r*(0.59,0.81)
    p3 = r*(2.49,0.81)
    p4 = r*(0.95,-0.31)
    p5 = r*(1.54,-2.12)
    p6 = r*(0,-1)
    p7 = r*(-1.54,-2.12)
    p8 = r*(-0.95,-0.31)
    p9 = r*(-2.49,0.81)
    p10 = r*(-0.59,0.81)
    ps = [p1,p2,p3,p4,p5,
            p6,p7,p8,p9,p10]
    angle = np.random.rand()*2*np.pi
    for i,p in enumerate(ps):
        ps[i] = move(rotate(p,angle),center)
    draw.polygon(ps,color)

def get_image(xys,colors,sizes):
    img = Image.new("RGB",(1000,1200))
    draw = ImageDraw.Draw(img)
    for xy,color,size in zip(xys,colors,sizes):
        #size to radius conversion
        #color to color conversion
        draw_star(draw,xy,radius,color)
    lines1, lines2 = get_lines(xys)
    for l1,l2 in zip(lines1,lines2):
        draw.line([l1,l2],"white",10)
    name = get_name() 
    #Add constellation name
    #Dont forget to use BU


def main():
    xys,colors,sizes = get_points()
    img_path = get_image(xys,colors,sizes)
    gr,p_id = BU.Facebook.upload("Check out this nice constellation!",BU.getAccessToken(),img_path)
    return True
