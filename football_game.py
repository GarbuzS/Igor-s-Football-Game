from tkinter import *
import random
canvas = Tk()
canvas.title("Football Career Simulator v 1.0")
canvas.geometry("600x600")
respect = 1
money = 0
goals = 0
seasons = 0
position = 0
lucky = 0
redirect = 0

#ENGLAND PART

def england():
    text_box.configure(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You are searching for a club in England...''')
    button1['text'] = 'Premier League'
    button2['text'] = 'Championship'
    button3['text'] = 'EFL League 1'
    button4['text']=''
    button4.configure(command=nothing)
    button1.configure(command=premier)
    button2.configure(command=championship)
    button3.configure(command=EFL_League_1)
    button5['text']=''
    button5.configure(command=nothing)
    button6['text']=''
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/england.png')

    

def premier():
    if respect < 15:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early to
be searching for a club in the Premier League...''')
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''You are searching for
a club in the Premier League...''')
        button1['text']='Manchester United'
        button2['text']='Arsenal'
        button3['text']='Manchester City'
        button1.configure(command=united)
        button2.configure(command=arsenal)
        button3.configure(command=chelsea)
        button4['text']=''
        button4.configure(command=nothing)
        img.configure(file='/home/stan/PycharmProjects/footballgame/premier.png')


def united():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Manchester United! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/united.png')

def arsenal():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Arsenal FC! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/arsenal.png')

def chelsea():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Manchester City! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/city.png')



def championship():
    if respect < 5:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early to
be searching for a club in the Championship...''')    
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''You are searching
for a club in the Championship...''')
        button1['text']='Birmingham City'
        button2['text']='Stoke City'
        button3['text']='Burnley'
        button1.configure(command=birmingham)
        button2.configure(command=stoke)
        button3.configure(command=burnley)
        img.configure(file='/home/stan/PycharmProjects/footballgame/championship.png')

def birmingham():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Birmingham! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/birmingham.png') 

def stoke():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Stoke City! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/stoke.png') 


def burnley():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Burnley FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/burnley.png') 



def EFL_League_1():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''What club do
you want to play for?''')
    button1['text'] = 'Wigan Athletic'
    button2['text'] = 'Charlton'
    button3['text'] = 'Portsmouth'
    button1.configure(command=wigan)
    button2.configure(command=charlton)
    button3.configure(command=portsmouth)
    img.configure(file='/home/stan/PycharmProjects/footballgame/eflone.png')

def wigan():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Wigan Athletic! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/wigan.png')

def charlton():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Charlton! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/charlton.png')

def portsmouth():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Portsmouth! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/port.png')


#SPAIN PART

def spain():
    text_box.configure(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You are searching for a club in Spain...''')
    button1['text']='La Liga'
    button2['text']='Segunda Division'
    button3['text']='Tercera Division'
    button1.configure(command=la_liga)
    button2.configure(command=segunda)
    button3.configure(command=tercera)
    button4['text']=''
    button4.configure(command=nothing)
    button5['text']=''
    button5.configure(command=nothing)
    button6['text']=''
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/spain.png')

def la_liga():
    text_box.configure(state='normal')
    text_box.delete(1.0, 'end')
    if respect < 15:
        text_box.insert('end', '''Seems a bit too
early to be searching for a club in the La Liga...''')
        
    else:
        text_box.configure(state='normal')
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a
a club in the La Liga...''')
        button1['text']='Real Madrid'
        button2['text']='Barcelona FC'
        button3['text']='Villareal'
        button1.configure(command=madrid)
        button2.configure(command=barca)
        button3.configure(command=villareal)
        img.configure(file='/home/stan/PycharmProjects/footballgame/laliga.png')

def madrid():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Real Madrid! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/madrid.png')

def barca():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Barcelona FC! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/barca.png')

def villareal():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Villareal FC! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/villa.png')
        
def segunda():
    text_box.configure(state='normal')
    text_box.delete(1.0, 'end')
    if respect < 5:
        text_box.insert('end', '''Seems a bit too
early to be searching for a club in the
Segunda Division...''')
        
    else:
        text_box.configure(state='normal')
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a
club in the Segunda Division...''')
        button1['text']='Levante'
        button2['text']='Real Zaragoza'
        button3['text']='Elche FC'
        button1.configure(command=levante)
        button2.configure(command=zaragoza)
        button3.configure(command=elche)
        img.configure(file='/home/stan/PycharmProjects/footballgame/segunda.png')

def levante():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Levante UD! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/levante.png')

def zaragoza():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Real Zaragoza! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/zaragoza.png')

def elche():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Elche FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/elche.png')


        
def tercera():
    text_box.configure(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a 
club in the Tercera Division...''')
    button1['text']='Murcia Imperial'
    button2['text']='Arenas Getxo'
    button3['text']='Constancia'
    button1.configure(command=murcia)
    button2.configure(command=arenas)
    button3.configure(command=constancia)
    img.configure(file='/home/stan/PycharmProjects/footballgame/tercera.png')

def murcia():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Murcia Imperial! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/murcia.png')

def arenas():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Arenas Getxo! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/arenas.png')

def constancia():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Constancia FC! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/consta.png') 


#ITALY PART

def italy():
    text_box.configure(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You are searching for a club in Italy...''')
    button1['text']='Serie A'
    button2['text']='Serie B'
    button3['text']='Serie C'
    button1.configure(command=A)
    button2.configure(command=B)
    button3.configure(command=C)
    button4['text']=''
    button4.configure(command=nothing)
    button5['text']=''
    button5.configure(command=nothing)
    button6['text']=''
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/italy.png')

def A():
    if respect < 15:
        text_box.configure(state='normal')
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early
to be searching for a club in the Serie A...''')  
    else:
        text_box.configure(state='normal')
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a
club in the Serie A...''')
        button1['text']='Napoli'
        button2['text']='Inter Milan'
        button3['text']='Juventus'
        button1.configure(command=napoli)
        button2.configure(command=inter)
        button3.configure(command=juve)
        img.configure(file='/home/stan/PycharmProjects/footballgame/seriea.png')

def napoli():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Napoli FC! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/napoli.png') 
  

def inter():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Inter Milan! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/inter.png') 


def juve():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Juventus FC! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/juve.png') 
        
def B():
    if respect < 5:
        text_box.configure(state='normal')
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early
to be searching for a club in the Serie B...''')
        
    else:
        text_box.configure(state='normal')
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a
club in the Serie B...''')
        button1['text']='Parma'
        button2['text']='Cremonese'
        button3['text']='Sampdoria'
        button1.configure(command=parma)
        button2.configure(command=cremo)
        button3.configure(command=samp)
        img.configure(file='/home/stan/PycharmProjects/footballgame/serieb.png')
        
def parma():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Parma FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/parma.png') 

def cremo():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Cremonese FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/cremo.png') 

def samp():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Sampodria FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/samp.png') 


        
def C():
    text_box.configure(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a
club in the Serie C...''')
    button1['text']='Feralpisalo'
    button2['text']='Reggiano'
    button3['text']='Catanzaro'
    button1.configure(command=feral)
    button2.configure(command=reggi)
    button3.configure(command=catan)
    img.configure(file='/home/stan/PycharmProjects/footballgame/seriec.png') 

def feral():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Feralpisalo! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/feral.png')

def reggi():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Reggiano! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/reggiano.png')

def catan():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Catanzaro! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/catanzaro.png')

#FRANCE PART

def france():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in France...''')
    button1['text']='Ligue 1'
    button2['text']='Ligue 2'
    button3['text']='Championnat National'
    button4['text']=''
    button1.configure(command=ligue1)
    button2.configure(command=ligue2)
    button3.configure(command=national)
    button4.configure(command=nothing)
    button5['text']=''
    button5.configure(command=nothing)
    button6['text']=''
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/france.png')
    
def ligue1():
    if respect < 15:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early
to be searching for a club in the Ligue 1...''')
        
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in the Ligue 1...''')
        button1['text']='PSG'
        button2['text']='Marseille'
        button3['text']='Monaco'
        button4['text']=''
        button1.configure(command=psg)
        button2.configure(command=marseille)
        button3.configure(command=monaco)
        button4.configure(command=nothing)
        img.configure(file='/home/stan/PycharmProjects/footballgame/ligue1.png')

def psg():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
PSG! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    button4['text']=''
    button4.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/psg.png')

def marseille():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Marseille FC! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    button4['text']=''
    button4.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/marseille.png')

def monaco():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Monaco FC! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    button4['text']=''
    button4.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/monaco.png')


def ligue2():
    if respect < 5:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early
to be searching for a club in the Ligue 2...''')
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club
in the Ligue 2...''')
        button1['text']='Paris FC'
        button2['text']='Auxerre'
        button3['text']='St Ettiene'
        button4['text']=''
        button1.configure(command=paris)
        button2.configure(command=auxe)
        button3.configure(command=etti)
        button4.configure(command=nothing)
        img.configure(file='/home/stan/PycharmProjects/footballgame/ligue2.png')

def paris():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Paris FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    button4['text']=''
    button4.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/paris.png')

def auxe():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Auxerre! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    button4['text']=''
    button4.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/auxerre.png')

def etti():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
St Ettiene! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    button4['text']=''
    button4.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/ettiene.png')

        
def national():
    button1['text']='Niort'
    button2['text']='Sochaux'
    button3['text']='Red Star'
    button4['text']=''
    button1.configure(command=niort)
    button2.configure(command=socha)
    button3.configure(command=star)
    button4.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/national.png')

def niort():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Niort FC! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/niort.png')

def socha():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Sochaux FC! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/socha.png')

def star():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Red Star FC! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/redstar.png')


#GERMANY PART
def germany():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in Germany...''')
    button1['text']='Bundesliga'
    button1.configure(command=first)
    button2['text']='2. Bundesliga'
    button2.configure(command=second)
    button3['text']='3 Liga'
    button3.configure(command=liga)
    button4['text']=''
    button4.configure(command=nothing)
    button5['text']=''
    button5.configure(command=nothing)
    button6['text']=''
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/germany.png')

def first():
    if respect < 15:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early
to be searching for a club in the Bundesliga...''')
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in
the Bundesliga...''')
        button1['text']='Bayern Munich'
        button2['text']='Borussia Dortmund'
        button3['text']='VfB Stuttgart'
        button4['text']=''
        button5['text']=''
        button1.configure(command=bayern)
        button2.configure(command=borussia)
        button3.configure(command=vfb)
        button4.configure(command=nothing)
        button5.configure(command=nothing)
        img.configure(file='/home/stan/PycharmProjects/footballgame/bundesliga.png')

def bayern():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Bayern Munich! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/bayern.png')

def borussia():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Borussia Dortmund! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/dortmund.png')

def vfb():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
VfB Stuttgart! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/vfb.png') 

    
def second():
    if respect < 5:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early
to be searching for a club in the 2. Bundesliga...''')
        
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in
the 2. Bundesliga...''')
        button1['text']='Hannover 96'
        button2['text']='Schalke 04'
        button3['text']='Hamburger SV'
        button4['text']=''
        button5['text']=''
        button1.configure(command=hannover)
        button2.configure(command=schalke)
        button3.configure(command=hamburger)
        button4.configure(command=nothing)
        button5.configure(command=nothing)
        img.configure(file='/home/stan/PycharmProjects/footballgame/2bundesliga.png') 

def hannover():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Hannover 96! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/hannover.png') 

def schalke():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Schalke 04! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/schalke.png') 

def hamburger():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Hamburger SV! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/hamburger.png')            

        
def liga():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in
the 3. Liga...''')
    button1['text']='1860 Munich'
    button2['text']='Ingolstadt'
    button3['text']='Borussia Dortmund II'
    button4['text']=''
    button5['text']=''
    button1.configure(command=munich)
    button2.configure(command=ingol)
    button3.configure(command=dortmundII)
    button4.configure(command=nothing)
    button5.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/3liga.png')

def munich():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
1860 Munich! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/munich1860.png')

def ingol():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Ingolstadt FC! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/ingolstadt.png')

def dortmundII():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Borussia Dortmund II! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/dortmund.png')

#NETHERLANDS PART

def netherlands():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in
the Netherlands...''')
    button1['text']='Eredivisie'
    button2['text']='Eerste Divisie'
    button3['text']='Tweede Divisie'
    button4['text']=''
    button5['text']=''
    button6['text']=''
    button1.configure(command=ered)
    button2.configure(command=eerste)
    button3.configure(command=tweede)
    button4.configure(command=nothing)
    button5.configure(command=nothing)
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/netherlands.png')

def ered():
    if respect < 15:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early to
be searching for a club in the Eredivisie...''')
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in the
Eredivisie...''')
        button1['text']='PSV Eindhoven'
        button2['text']='Ajax'
        button3['text']='Feyenoord'
        button4['text']=''
        button5['text']=''
        button6['text']=''
        button1.configure(command=psv)
        button2.configure(command=ajax)
        button3.configure(command=feyenoord)
        button4.configure(command=nothing)
        button5.configure(command=nothing)
        button6.configure(command=nothing)
        img.configure(file='/home/stan/PycharmProjects/footballgame/eredivisie.png')

def psv():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
PSV Eindhoven! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/psv.png')

def ajax():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Ajax! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/ajax.png')

def feyenoord():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Feyenoord! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/feyenoord.png')

        
def eerste():
    if respect < 5:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too early to
be searching for a club in the Eerste Divisie...''')
        
    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in the
Eerste Divisie...''')
        button1['text']='VVV Venlo'
        button2['text']='FC Eindhoven'
        button3['text']='Helmond Sport'
        button4['text']=''
        button5['text']=''
        button6['text']=''
        button1.configure(command=venlo)
        button2.configure(command=FC_eind)
        button3.configure(command=sport)
        button4.configure(command=nothing)
        button5.configure(command=nothing)
        button6.configure(command=nothing)
        img.configure(file='/home/stan/PycharmProjects/footballgame/eerste.png')

def venlo():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
VVV Venlo! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/venlo.png')

def FC_eind():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
FC Eindhoven! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/fc_eind.png')

def sport():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Helmond Sport! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/helmond.png')

        

        
def tweede():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in
the Derde Divisie...''')
    button1['text']='Spakenburg'
    button2['text']='Kozzaken Boys'
    button3['text']='FC Lisse'
    button4['text']=''
    button5['text']=''
    button6['text']=''
    button1.configure(command=spaken)
    button2.configure(command=kozzaken)
    button3.configure(command=lisse)
    button4.configure(command=nothing)
    button5.configure(command=nothing)
    button6.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/tweede.png')

def spaken():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Spakenburg! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/spakenburg.png')

def kozzaken():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Kozzaken Boys! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/kozzaken.png')

def lisse():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
FC Lisse! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/lisse.png')


def portugal():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in
Portugal...''')
    button1['text']='Liga Portugal'
    button2['text']='Liga Portugal 2'
    button3['text']='Liga Portugal 3'
    button4['text']=''
    button5['text']=''
    button6['text']=''
    button1.configure(command=port1)
    button2.configure(command=port2)
    button3.configure(command=port3)
    button4.configure(command=nothing)
    button5.configure(command=nothing)
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/portugal.png')

def port1():
    if respect < 15:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too
early to be searching for a club in the Portugal
Liga 1...''')

    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in
    the Portugal Liga 1...''')
        button1['text']='FC Porto'
        button2['text']='Sporting CP'
        button3['text']='Benfica'
        button1.configure(command=porto)
        button2.configure(command=sporting)
        button3.configure(command=benfica)
        img.configure(file='/home/stan/PycharmProjects/footballgame/port1.png')

def porto():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
FC Porto! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/porto.png')

def sporting():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Sporting CP! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/sporting.png')

def benfica():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Benfica! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/benfica.png')



def port2():
    if respect < 5:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too
early to be searching for a club in the Portugal
Liga 2...''')

    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in
    the Portugal Liga 2...''')
        button1['text']='Santa Clara'
        button2['text']='Nacional'
        button3['text']='Pacos Ferreira'
        button1.configure(command=santa)
        button2.configure(command=nacional)
        button3.configure(command=pacos)
        img.configure(file='/home/stan/PycharmProjects/footballgame/liga2.png')

def santa():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Santa Clara FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/santa.png')

def nacional():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Nacional! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/nacional.png')

def pacos():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Pacos Ferreira! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/pacos.png')


def port3():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in
the Portugal Liga 3...''')
    button1['text']='Oliveirense'
    button2['text']='Belenenses'
    button3['text']='Torreense'
    button1.configure(command=olive)
    button2.configure(command=bele)
    button3.configure(command=torree)
    img.configure(file='/home/stan/PycharmProjects/footballgame/port3.png')

def olive():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Oliveirense! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/oliver.png')

def bele():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Belenenses! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/bele.png')

def torree():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Torreense! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/torree.png')


def argentina():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in
Argentina...''')
    button1['text']='Argentine Primera'
    button2['text']='Primera Nacional'
    button3['text']='Primera B'
    button4['text']=''
    button5['text']=''
    button6['text']=''
    button1.configure(command=primera)
    button2.configure(command=primera2)
    button3.configure(command=primerab)
    button4.configure(command=nothing)
    button5.configure(command=nothing)
    button6.configure(command=nothing)
    button8['text']=''
    button8.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/argentina.png')

def primera():
    if respect < 15:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too
early to be searching for a club in the Argentine
Primera Division...''')

    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in
the Argentine Primera Division...''')
        button1['text']='Boca Juniors'
        button2['text']='River Plate'
        button3['text']='Newells Old Boys'
        button1.configure(command=boca)
        button2.configure(command=river)
        button3.configure(command=newell)
        img.configure(file='/home/stan/PycharmProjects/footballgame/argentine.png')

def boca():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Boca Juniors! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/boca.png')

def river():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
River Plate! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/river.png')

def newell():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Newells Old Boys! Plus 25,000 money!''')
    money += 25000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/newell.png')

def primera2():
    if respect < 5:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Seems a bit too
early to be searching for a club in the Primera
Nacional...''')

    else:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''Searching for a club in
    the Primera Nacional...''')
        button1['text']='Patronato'
        button2['text']='Quilmes'
        button3['text']='Aldosivi'
        button1.configure(command=patro)
        button2.configure(command=quilmes)
        button3.configure(command=aldo)
        img.configure(file='/home/stan/PycharmProjects/footballgame/primera2.png')

def patro():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Patronato FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/patro.png')

def quilmes():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Quilmes FC! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/quilmes.png')

def aldo():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Aldosivi! Plus 15,000 money!''')
    money += 15000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/aldo.png')

def primerab():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a club in
the Portugal Liga 3...''')
    button1['text']='Los Andes'
    button2['text']='Sasachispas'
    button3['text']='Villa San Carlos'
    button1.configure(command=andes)
    button2.configure(command=sasa)
    button3.configure(command=carlos)
    img.configure(file='/home/stan/PycharmProjects/footballgame/primerab.png')

def andes():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Los Andes! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/andes.png')

def sasa():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Sasachispas FC! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/sasa.png')

def carlos():
    global money
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have signed for
Villa San Carlos! Plus 10,000 money!''')
    money += 10000
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    button1['text']='Play the season'
    button2['text']=''
    button3['text']=''
    button1.configure(command=season)
    button2.configure(command=nothing)
    button3.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/carlos.png')












#STUFF

text_box = Text(canvas, height=10, width=50)
text_box.pack(padx=0, pady = 32)


respect_text = Text(canvas, height=1, width=10, fg="black", borderwidth=0, highlightthickness=0)
respect_text.configure(font=("Courier", 11, "bold"))
respect_text.place(x=30, y=8)
respect_text.insert('end', respect)

starimg=PhotoImage(file="/home/stan/PycharmProjects/footballgame/star.png")
starimage=Label(canvas, image=starimg)
starimage.place(x=7, y=7)



money_text = Text(canvas, height=1, width=10, fg="black", borderwidth=0, highlightthickness=0)
money_text.configure(font=("Courier", 11, "bold"))
money_text.place(x=170, y=8)
money_text.insert('end', money)

moneyimg=PhotoImage(file="/home/stan/PycharmProjects/footballgame/money.png")
moneyimage=Label(canvas, image=moneyimg)
moneyimage.place(x=140, y=7)



goal_text = Text(canvas, height=1, width=10, fg="black", borderwidth=0, highlightthickness=0)
goal_text.configure(font=("Courier", 11, "bold"))
goal_text.place(x=310, y=8)
goal_text.insert('end', goals)

goalimg=PhotoImage(file="/home/stan/PycharmProjects/footballgame/soccer.png")
goalimage=Label(canvas, image=goalimg)
goalimage.place(x=280, y=7)



season_text = Text(canvas, height=1, width=10, fg="black", borderwidth=0, highlightthickness=0)
season_text.configure(font=("Courier", 11, "bold"))
season_text.place(x=450, y=8)
season_text.insert('end', seasons)

seasonimg=PhotoImage(file="/home/stan/PycharmProjects/footballgame/clock.png")
seasonimage=Label(canvas, image=seasonimg)
seasonimage.place(x=420, y=7)

img= PhotoImage(file="/home/stan/PycharmProjects/footballgame/football.png")
picture=Label(canvas, image=img)
picture.place(x=200, y=250)








def season():
    global money
    global respect
    global goals
    global seasons
    global position
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You have played for
a season. Check how much goals you scored!''')
    respect += 1
    seasons += 1
    money += 1000
    
    if position == 1:
        lucky = random.randint(1,100)
        if lucky == 100:
            goals += 1

    if position == 2:
        goals += random.randint(0,10)

    if position == 3:
        goals += random.randint(10,20)

    if position == 4:
        goals += random.randint(20,30)

    if seasons >= 25:
        text_box.delete(1.0, 'end')
        text_box.insert('end', '''You will retire soon...''')

    if seasons == 30:
        exit()

    respect_text.delete("1.0", 'end')
    respect_text.insert('end', respect)
    money_text.delete("1.0", 'end')
    money_text.insert('end', money)
    goal_text.delete("1.0", 'end')
    goal_text.insert('end', goals)
    season_text.delete("1.0", 'end')
    season_text.insert('end', seasons)
    button2['text']='Sign for a new club'
    button2.configure(command=new_club)
    button1.configure(command=season)
    button1['text']='Play another season'
    button4['text']=''
    button4.configure(command=nothing)
    button5['text']=''
    button5.configure(command=nothing)
    if seasons >= 1:
        button7['text']='Retire'
        button7.configure(cursor= "hand2",bg='red2', 
        activebackground="red3", command=retire)


def nothing():
    global redirect
    redirect = random.randint(100,100000)
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''This button does nothing. Try another
button!''')
    print("Redirecting to file", redirect, "...")
    print("Error in file,", redirect, "moving to: pycharmproject/footballgame/canvas$.py X550CL mnk@mnk-lop09")

def retire():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Are you sure you want to retire?''')
    button1['text']='Yes'
    button2['text']='No'
    button1.configure(command=yes)
    button2.configure(command=new_club)
    button3['text']=''
    button3.configure(command=nothing)
    button4['text']=''
    button4.configure(command=nothing)
    button5['text']=''
    button5.configure(command=nothing)
    button6['text']=''
    button6.configure(command=nothing)
    button9['text']=''
    button9.configure(command=nothing)
    img.configure(file='/home/stan/PycharmProjects/footballgame/retire.png')

def yes():
    exit()

def new_club():
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''Searching for a new club...''')

    button1['text']='England'
    button1.configure(command=england)

    button2['text']='Spain'
    button2.configure(command=spain)

    button3['text']='Italy'
    button3.configure(command=italy)

    button4['text']='France'
    button4.configure(command=france)

    button5['text']='Germany'
    button5.configure(command=germany)

    button6['text']='Netherlands'
    button6.configure(command=netherlands)

    button8['text']='Portugal'
    button8.configure(command=portugal)

    button9['text']='Argentina'
    button9.configure(command=argentina)

    img.configure(file='/home/stan/PycharmProjects/footballgame/football.png')

def one():
    global position
    position=1
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You are a goalkeeper!
Don't expect to score much goals... you do
have a small chance to do so though... 
Anyway, what country's clubs do you
want to play for?''')
    
    button1['text']='England'
    button1.configure(command=england)
    button2['text']='Spain'
    button2.configure(command=spain)
    button3['text']='Italy'
    button3.configure(command=italy)
    button4['text']='France'
    button4.configure(command=france)
    button5['text']='Germany'
    button5.configure(command=germany)
    button6['text']='Netherlands'
    button6.configure(command=netherlands)
    button8['text']='Portugal'
    button8.configure(command=portugal)
    button9['text']='Argentina'
    button9.configure(command=argentina)
    img.configure(file='/home/stan/PycharmProjects/footballgame/goalkeeper.png')


def two():
    global position
    position=2
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You are a defender!
Could you become the next Maldini?! What country's
clubs do you want to play for?''')
    
    button1['text']='England'
    button1.configure(command=england)
    button2['text']='Spain'
    button2.configure(command=spain)
    button3['text']='Italy'
    button3.configure(command=italy)
    button4['text']='France'
    button4.configure(command=france)
    button5['text']='Germany'
    button5.configure(command=germany)
    button6['text']='Netherlands'
    button6.configure(command=netherlands)
    button8['text']='Portugal'
    button8.configure(command=portugal)
    button9['text']='Argentina'
    button9.configure(command=argentina)
    img.configure(file='/home/stan/PycharmProjects/footballgame/defender.png')


def three():
    global position
    position=3
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You are a midfielder!
Could you become the world's best playmaker?! What country's 
clubs do you want to play for?''')
    
    button1['text']='England'
    button1.configure(command=england)
    button2['text']='Spain'
    button2.configure(command=spain)
    button3['text']='Italy'
    button3.configure(command=italy)
    button4['text']='France'
    button4.configure(command=france)
    button5['text']='Germany'
    button5.configure(command=germany)
    button6['text']='Netherlands'
    button6.configure(command=netherlands)
    button8['text']='Portugal'
    button8.configure(command=portugal)
    button9['text']='Argentina'
    button9.configure(command=argentina)
    img.configure(file='/home/stan/PycharmProjects/footballgame/midfielder.png')


def four():
    global position
    position=4
    text_box.delete(1.0, 'end')
    text_box.insert('end', '''You are a striker!
I see you like scoring lots of goals and being
the star of the show! Choose which country's
clubs you want to play for down below!''')
    
    button1['text']='England'
    button1.configure(command=england)
    button2['text']='Spain'
    button2.configure(command=spain)
    button3['text']='Italy'
    button3.configure(command=italy)
    button4['text']='France'
    button4.configure(command=france)
    button5['text']='Germany'
    button5.configure(command=germany)
    button6['text']='Netherlands'
    button6.configure(command=netherlands)
    button8['text']='Portugal'
    button8.configure(command=portugal)
    button9['text']='Argentina'
    button9.configure(command=argentina)
    img.configure(file='/home/stan/PycharmProjects/footballgame/striker.png')




message = '''Welcome to Football Career Simulator! 
Take a look at the statistics on the top of the
screen. The star means your fame. The higher
your fame, the better the clubs that you can
sign for are. The cash icon is your money. 
You can't really do anything with money in this 
game, but it's just a thing I decided to add. 
The ball is the amount of goals you have scored,
and clock is the amount of seasons you have 
played.Scroll down to read more.

After 30 seasons you will automatically 
retire. If you think that doesn't make sense,
look at it this way: even if you started your 
career at 18, after thirty seasons you'd be 
48! Even Ibrahimovic and Buffon didn't play for
that long!

Anyway, to start, choose your  position 
(goalkeeper, defender, midfielder, striker)
by clicking one of the buttons below!'''
text_box.insert('end', message)

scroll_bar = Scrollbar(canvas, orient="vertical")
scroll_bar.pack(side=RIGHT, fill='y')
text_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=text_box.yview)



button1=Button(canvas, text="Goalkeeper", cursor= "hand2", command=one)
button1.place(x=25, y=210)

button2=Button(canvas, text="Defender", cursor= "hand2", command=two)
button2.place(x=25, y=260)

button3=Button(canvas, text="Midfielder",cursor= "hand2", command=three)
button3.place(x=25, y=310)

button4=Button(canvas, text="Striker",cursor= "hand2", command=four)
button4.place(x=25, y=360)

button5=Button(canvas, text="",cursor= "hand2", command=nothing)
button5.place(x=25, y=410)

button6=Button(canvas, text="",cursor= "hand2", command=nothing)
button6.place(x=25, y=460)

button7=Button(canvas, text="",cursor= "hand2", command=nothing)
button7.place(x=500, y=550)

button8=Button(canvas, text="",cursor= "hand2", command=nothing)
button8.place(x=25, y=510)

button9=Button(canvas, text="",cursor= "hand2", command=nothing)
button9.place(x=25, y=560)





canvas.mainloop()