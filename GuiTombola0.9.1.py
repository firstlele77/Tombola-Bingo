from tkinter import *
from tkinter import messagebox # per attivare i messagebox
from tkinter import filedialog # per attivare il modulo filedialog
import random, sys, os


class Menub(object):
    """ # Gestione menu """
    def __init__(self, window):

        def mquit():
            mexit = messagebox.askyesno(title="Quit",message='Are you sure?')
            if mexit > 0:
                window.destroy()
        def maboutinfo():
            minfo = messagebox.showinfo(title="About", message="Gioco della Tombola\n\nCreated by\n\nClaudio Francini")

        """ Creazione menu per la finestra di configurazione """
        menubar = Menu(window)
        filemenu = Menu(menubar)
        filemenu.add_command(label='Quit', command = mquit)
        menubar.add_cascade(label='File',menu=filemenu)
        helpmenu=Menu(menubar)
        helpmenu.add_command(label='About', command = maboutinfo)
        menubar.add_cascade(label='About',menu=helpmenu)
        window.config(menu=menubar)

class Board():
    """Creazione del tabellone."""
    win = 0
    def __init__(self):
        """Generazione del tabellone"""
        players_cards = []
        name_players = []
        card = []


    def show_board(self):
        """ Apertura della finestra di configurazione gioco """

        def configu():
            """ Assegnazione valori in uscita dal bottone 'cominciamo' """
            config = []
            names = []
            num_player = nplayer.get()
            num_cards = ncards.get()
            #print(num_player, num_cards)
            if num_player == 1:
                config += num_player,
                config += num_cards,
                names += gio1.get(),
            if num_player == 2:
                config += num_player,
                config += num_cards,
                names += gio1.get(),
                names += gio2.get(),
            if num_player == 3:
                config += num_player,
                config += num_cards,
                names += gio1.get(),
                names += gio2.get(),
                names += gio3.get(),
            if num_player == 4:
                config += num_player,
                config += num_cards,
                names += gio1.get(),
                names += gio2.get(),
                names += gio3.get(),
                names += gio4.get(),
            Board.players_cards = config
            Board.name_players = names
            tconf.destroy() #Premuto il bottone, la finestra di configurazione viene distrutta
            game = Game()
            game

        """ Generazione finestra di configurazione"""
        tconf = Tk()
        tconf.geometry()
        tconf.title('Tombola')
        Menub(tconf)
        radio_player = Frame(tconf)
        radio_card = Frame(tconf)
        name_players = Frame(tconf)
        nplayer = IntVar(None, 2)
        ncards = IntVar(None, 2)
        gio1 = StringVar()
        gio2 = StringVar()
        gio3 = StringVar()
        gio4 = StringVar()
        Label(text='Benvenuti nel gioco della Tombola!', fg='black', font = "Helvetica 10 bold").pack(pady=30)
        Label(text='Scegliete il numero di giocatori ed il numero cartella', fg='black', font = "Helvetica 10 bold").pack(padx=30,pady=10)
        button1 = Button(tconf, text='COMINCIAMO!!', command=configu).pack(side=BOTTOM, pady=30) #Richiama la funzione configu del bottone
        Label(radio_player,text='Numero giocatori').pack()
        radio_1 = Radiobutton(radio_player, text='1 Giocatore', value = 1, variable = nplayer).pack()
        radio_2 = Radiobutton(radio_player, text='2 Giocatore', value = 2, variable = nplayer).pack()
        radio_3 = Radiobutton(radio_player, text='3 Giocatore', value = 3, variable = nplayer).pack()
        radio_4 = Radiobutton(radio_player, text='4 Giocatore', value = 4, variable = nplayer).pack()
        radio_player.pack(side=LEFT, padx=30, pady=10)
        Label(name_players,text='Nome giocatori').pack()
        gioca1 = Entry(name_players,textvariable=gio1)
        gioca1.insert(END, 'Pippo')
        gioca1.pack()
        gioca2 = Entry(name_players,textvariable=gio2)
        gioca2.insert(END, 'Pluto')
        gioca2.pack()
        gioca3 = Entry(name_players,textvariable=gio3)
        gioca3.insert(END, 'Paperino')
        gioca3.pack()
        gioca4 = Entry(name_players,textvariable=gio4)
        gioca4.insert(END, 'Topolino')
        gioca4.pack()
        name_players.pack(side=LEFT, padx=20)
        Label(radio_card,text='Numero cartelle').pack()
        radio_5 = Radiobutton(radio_card, text='1 Cartelle', value = 1, variable = ncards).pack()
        radio_6 = Radiobutton(radio_card, text='2 Cartelle', value = 2, variable = ncards).pack()
        radio_7 = Radiobutton(radio_card, text='3 Cartelle', value = 3, variable = ncards).pack()
        radio_8 = Radiobutton(radio_card, text='4 Cartelle', value = 4, variable = ncards).pack()
        radio_card.pack(side=RIGHT, padx=30, pady=10)
        tconf.mainloop()

class Game():

    def __init__(self):
        """Configurazione finestre di gioco"""
        num = Numeri()
        car = Cartelle()
        matrix = num.matrix(90)

        """ Generazione finestra del Tabellone """
        board = Tk()
        board.geometry()
        board.title('Tabellone')
        for i in range (1,11):
            for a in range (0,9):
                Label(board,text='%02d' % (i+(10*a)), fg='black', bg='white',font = "Helvetica 10 bold").grid(row=a,column=[i], padx=5, pady=5)

        """Generazione finestra delle cartelle"""
        play_cards = Board.players_cards
        name_play = Board.name_players
        elen_tuple = []
        prima_tuple = []
        coord_tuple = []
        tot_coord = []
        gen_coord = []
        cards = Tk()
        cards.geometry()
        cards.title('Cartelle')


        posx = 0
        posy = 0
        posz = 2
        for pos_gio in range(play_cards[0]):
            Label(cards, text='Nome giocatore:%s' % (name_play[pos_gio])).grid(row=0+posy,column=1+posx,columnspan=10)
            posy += 1
            for pos_card in range(play_cards[1]):
                Label(cards, text='Numero cartella:%s' % (pos_card)).grid(row=0+posy,column=1+posx,columnspan=10)
                Label(cards, text='    ').grid(row=0+posy,column=0+posx)
                tupla_card = car.genera_cartella()
                elen_tuple += tupla_card,
                tot_coord = []
                for el in range(3):
                    #print(el)
                    for elem in range(5):
                        if 0 < tupla_card[el][elem] < 11:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=1+posx)
                            coord_tuple += [el+posz,1+posx],
                            continue
                        elif 10 < tupla_card[el][elem] < 21:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=2+posx)
                            coord_tuple += [el+posz,2+posx],
                            continue
                        elif 20 < tupla_card[el][elem] < 31:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=3+posx)
                            coord_tuple += [el+posz,3+posx],
                            continue
                        elif 30 < tupla_card[el][elem] < 41:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=4+posx)
                            coord_tuple += [el+posz,4+posx],
                            continue
                        elif 40 < tupla_card[el][elem] < 51:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=5+posx)
                            coord_tuple += [el+posz,5+posx],
                            continue
                        elif 50 < tupla_card[el][elem] < 61:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=6+posx)
                            coord_tuple += [el+posz,6+posx],
                            continue
                        elif 60 < tupla_card[el][elem] < 71:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=7+posx)
                            coord_tuple += [el+posz,7+posx],
                            continue
                        elif 70 < tupla_card[el][elem] < 81:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=8+posx)
                            coord_tuple += [el+posz,8+posx],
                            continue
                        elif 80 < tupla_card[el][elem] <= 91:
                            Label(cards,text=tupla_card[el][elem], fg='black', bg='white').grid(row=el+posz,column=9+posx)
                            coord_tuple += [el+posz,9+posx],
                            continue
                    tot_coord += coord_tuple,
                posx += 13
            posx = 0
            posy += 6
            posz += 7


        def vincita(numero):
            """ Verifica di vincita """
            cartel = 0
            pnumero = numero

            for i in elen_tuple:

                tombola = 0
                for k in i:
                    n = k.count(99)
                    tombola += n
                    gi = cartel // Board.players_cards[1]
                    if Board.win == 0:
                        if n == 2:
                            tombo = messagebox.showinfo(title="AMBO!!!", message="\nIL GIOCATORE %s \nCON LA CARTELLA %s \nHA FATTO \nAMBO!!!!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            #print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO AMBO!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            Board.win  = 1
                    if Board.win  == 1:
                        if n == 3:
                            tombo = messagebox.showinfo(title="TERNA!!!", message="\nIL GIOCATORE %s \nCON LA CARTELLA %s \nHA FATTO \nTERNA!!!!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            #print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO TERNA!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            Board.win  = 2
                    if Board.win  == 2:
                        if n == 4:
                            tombo = messagebox.showinfo(title="QUATERNA!!!", message="\nIL GIOCATORE %s \nCON LA CARTELLA %s \nHA FATTO \nQUATERNA!!!!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            #print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO QUATERNA!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            Board.win  = 3
                    if Board.win  == 3:
                        if n == 5:
                            tombo = messagebox.showinfo(title="CINQUINA!!!", message="\nIL GIOCATORE %s \nCON LA CARTELLA %s \nHA FATTO \nCINQUINA!!!!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            #print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO CINQUINA!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                            Board.win  = 4
                    if tombola == 15:
                        tombo = messagebox.showinfo(title="TOMBOLA!!!", message="\nIL GIOCATORE %s \nCON LA CARTELLA %s \nHA FATTO \nTOMBOLA!!!!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                        #print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO TOMBOLA!!!!!!" % (Board.name_players[gi],cartel % Board.players_cards[1]))
                        exit()
                cartel +=1

        def verifica(pedina, players_cards):
            """ Controllo e visualizzazione del numero uscito """
            pedina = pedina
            players_cards = players_cards
            decine = pedina // 10
            unita = pedina % 10
            if unita == 0:
                decine -= 1
                unita = 10
                Label(board,text='%02d' % (pedina), fg='black', bg='red', font = "Helvetica 10 bold").grid(row=decine,column=unita, padx=5, pady=5)
            elif unita != 0:
                Label(board,text='%02d' % (pedina), fg='black', bg='red', font = "Helvetica 10 bold").grid(row=decine,column=unita, padx=5, pady=5)
            zero = 0
            tre = 0
            for czero in elen_tuple:
                uno = 0
                for cuno in czero:
                    due = 0
                    for cdue in cuno:
                        if int(pedina) == int(cdue):
                            #print('Trovato il %d in cartella%d nella linea %d posizione%d' %(pedina, zero, uno, due))
                            Label(cards, text = pedina, fg='black', bg='green').grid(row=coord_tuple[tre][0],column=coord_tuple[tre][1])
                            elen_tuple[zero][uno][due] = 99
                            vincita(pedina)
                        due += 1
                        tre += 1
                    uno += 1
                zero += 1

        def bcheck():
            """ Visualizza numero uscito """
            numero = Numeri()
            pedina = numero.pesca_num()
            verifica(pedina, Board.players_cards)
            Label(score, text='%02d' % (pedina), font = 'Helvetica 15 bold').grid(row=5,column=0)


        """Generazione finestra dello score e pulsante"""
        score = Tk()
        score.geometry()
        score.title('Risultato')
        Label(score, text='Premere il bottone per continuare').grid(row=0,column=0, pady=5)
        button2 = Button(score, text='Numero', command=bcheck).grid(row=1,column=0,padx=10, pady=10)
        Label(score, text='In numero uscito è:',font = 'Helvetica 10 bold' ).grid(row=2,column=0)

        """ Accende le finestre si score, cartelle, e tabellone """
        score.mainloop()
        cards.mainloop()
        board.mainloop()

class Cartelle():
    """Creazione Cartelle."""

    def __init__(self):
        """ Imposxtazione numero Cartelle """
        pass

    def genera_cartella(self):
        """ creazione della tupla della cartella
        elemento output = tupla cartella generata"""
        num = Numeri()
        matrix = num.matrix(90)
        numeri_cart = []
        tupla_cartella = []
        mnumeri = []
        cmatrice = []
        cmatrice = matrix
        for a in range(1,4):
            riga = []
            mnumeri = []
            mnumeri += cmatrice
            for b in range(1,6):
                pulito = []
                for h in range(0,90):
                    if mnumeri[h] != ' ':
                        puli = mnumeri[h]
                        pulito += puli,
                scelto = random.choice(pulito)
                riga += scelto,
                scelto = int(scelto)
                if scelto <= 10:
                    for g in range(0,10):
                        mnumeri[g] = ' '
                if scelto >= 11 and scelto <= 20:
                    for g in range(10,20):
                        mnumeri[g] = ' '
                if scelto >= 21 and scelto <= 30:
                    for g in range(20,30):
                        mnumeri[g] = ' '
                if scelto >= 31 and scelto <= 40:
                    for g in range(30,40):
                        mnumeri[g] = ' '
                if scelto >= 41 and scelto <= 50:
                    for g in range(40,50):
                        mnumeri[g] = ' '
                if scelto >= 51 and scelto <= 60:
                    for g in range(50,60):
                        mnumeri[g] = ' '
                if scelto >= 61 and scelto <= 70:
                    for g in range(60,70):
                        mnumeri[g] = ' '
                if scelto >= 71 and scelto <= 80:
                    for g in range(70,80):
                        mnumeri[g] = ' '
                if scelto >= 81 and scelto <= 90:
                    for g in range(80,90):
                        mnumeri[g] = ' '
                riduci = scelto -1
                cmatrice[riduci] = ' '
                riga.sort()
            tupla_cartella += ((riga),)
        return tupla_cartella

class Numeri():
    """Creazione sacchetto dei Numeri."""
    numeri = []
    pesca = []
    for i in range(1, 91):
        pesca.append(i)
    numeri = pesca

    def __init__(self):
        pass

    def matrix(self, value):
        """ Generatore di matrice.
        Valore input = grandezza matrice
        Valore output = tupla di grandezza 'matrice'
        """
        self.value = value + 1
        matrix = []
        for i in range(1, self.value):
            matrix.append(i)
        return matrix

    def pesca_num(self):
        """Pesca un numero e lo elimina dalla lista
        elemento output numero scelto"""
        self.numero = Numeri.numeri
        random.shuffle(self.numero)
        self.scelto = self.numero[0]
        self.numero.pop(0)
        return self.scelto

if __name__ == '__main__':
    play = Board()
    play.show_board()
