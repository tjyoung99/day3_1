def setup():
    size(500,500)
    background(0)
    
def draw():
    red=random(0,255)
    green=random(0,255)
    blue=random(0,255)
    fill(red,green,blue)
    size=random(10,100)
    size2=random(10,100)
    xy=random(0,500)
    hk=random(0,500)
    if mouseX <250 and mouseY <250:
        fill(255,0,0)
    elif mouseX >250 and mouseY >250:
        fill(0,255,0)
    elif mouseX >250 and mouseY <250:
        fill(0,0,255)
    else:
        fill(255,255,0)
    ellipse(xy,hk,size,size2)
