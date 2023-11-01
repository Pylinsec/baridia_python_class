from turtle import *


# make most function 
def most():
    penup()
    goto(-100,50)
    pendown()
    pensize(3)
    pencolor('red')
    for i in range(2):
        fd(200)
        rt(90)
        fd(100)
        rt(90)
    done()


# make mosslas 
def moss():
    pensize(3)
    pencolor('red')
    for i in range(3):
        fd(300)
        rt(120)
    done()


# sakht deyreh 
def dayerh(shoa):
    pensize(3)
    pencolor('red')
    shoa = int(input('andaz shae ra vared konid: '))
    circle(shoa)
    done()

def moraba():
    pensize(3)
    pencolor('red')
    for i in range(4):
        fd(200)
        rt(90)
    done()

def setarh():
    print('setareh')


text= ''' lotfan adad monaseb vared kondid:
1--> sakht mostatil
2--> sakht mosals
3--> sakht dayerh ba shoa maloom
4--> sakht moraba
5--> sakht setareh 
: '''
voroodi = int(input(text))
if voroodi == 1:
    most()
elif voroodi == 2:
    moss()  
elif voroodi == 3:
    dayerh()
elif voroodi == 4:
    moraba()         
elif voroodi == 5:
    setarh()