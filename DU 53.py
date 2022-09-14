import tkinter #použije knižnicu tkinter
canvas=tkinter.Canvas(width=1000,height= 250) #spravý platno s hrubkou 1000 a dlžkov 250
canvas.pack() #spravý platno

def budovy(): #definicia 
    subor=open('zastavba_na_ulici.txt') #otvorí textovy subor zastavba_na_ulici
    a=int(entry1.get()) #premena a do ktorej sa uloži niečo čo niekto zada
    x=10  #premena x ktora predstavuje osu x
    y=150 #premena y ktora predstavuje y osu
    vyska2=0 #vyska2 sa nastavy na 0 

    for riadok in subor: #for ciklus ktory sa vykona tolko krat kolko je riadkov v subore
        cislo=riadok.split() #premena čislo ktora rozdelý retazed za každou medzerou
        vyska=int(cislo[1]) #premena vyska ktora je vyčita čislo za prvou medzerou
        sirka=int(cislo[0]) #premena sirka ktora vyčita prvu premenu

    if vyska >0: #podmienka nato aby ked je vyska budovy večšia ako 0 tak spravila budovu
        canvas.create_rectangle(x,y-vyska,x+sirka,y,fill='grey') #nakreslenie budovy

    else: #ak sa nespravi prva podmienka tak sa spusiti podmiena else
        canvas.create_line(x,y,x+sirka,y,width=3,fill='green') #spravenie zelenej čiary teda či je tam miesto na stavanie
    if vyska !=0 and vyska2 !=0 and abs(vyska-vyska2)>a: #podmienka ak sa vyska a vyska 2 nerovnaju 0 a absolutna hodnota po ich odčitaný je večšia ako premena a
        canvas.create_line(x,y-vyska,x,y-vyska2,width=3,fill='red') #tak sa nakresli červena čiara 
    x+=sirka #premna x sa zvačši o sirka
    vyska2=vyska #vyska2 sa nastavy na vyska
    subor.close() #zatvori sa subor

entry1=tkinter.Entry() #spravi sa pole do ktoreho sa niečo vklada
entry1.pack()
entry1.insert(0,'60') #do pola entry sa da 60 
button1=tkinter.Button(text='Vykresli ulicu', command=budovy) #spravi sa tlačidlo
button1.pack()
canvas.mainloop() #všetko sa to zopakuje 


        
