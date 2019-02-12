from tkinter import *
from PIL import ImageTk,Image
from front_2 import *
from back_algo import *
from helper_tools import score as scoreExpr

counterJenisKartu=[0,0,0,0,0,0,0,0,0,0,0,0,0]#####[counterjeniskartu(1,2,3...13)]
#makai list karena imuttable int
counterJumlahKartu=[52]

def fungsiImgKartu(intcard,countJenis):
    countJenis[intcard-1]=countJenis[intcard-1]+1
    if(countJenis[intcard-1]==1):
        return imgClist[intcard-1]
    elif(countJenis[intcard-1]==2):
        return imgDlist[intcard-1]
    elif(countJenis[intcard-1]==3):
        return imgHlist[intcard-1]
    elif(countJenis[intcard-1]==4):
        return imgSlist[intcard-1]

def buttonCallBack(countJenis, countJumlah):
    listCard=input_from_file()
    intcard1=listCard[0]
    intcard2=listCard[1]
    intcard3=listCard[2]
    intcard4=listCard[3]
    ekspresiHasil=solve_greedy(listCard,24)
    score=scoreExpr(ekspresiHasil,24)
    hasil= eval(ekspresiHasil)
    Kartu1.configure(image=fungsiImgKartu(intcard1,countJenis))
    #Kartu1.image = fungsiImgKartu(intcard1,countJenis)
    Kartu2.configure(image=fungsiImgKartu(intcard2,countJenis))
    #Kartu2.image = fungsiImgKartu(intcard2,countJenis)
    Kartu3.configure(image=fungsiImgKartu(intcard3,countJenis))
    #Kartu3.image = fungsiImgKartu(intcard3,countJenis)
    Kartu4.configure(image=fungsiImgKartu(intcard4,countJenis))
    #Kartu4.image = fungsiImgKartu(intcard4,countJenis)
    ekspresi.configure(text="Solusi : " + ekspresiHasil  + " = " + str(hasil))
    #ekspresi.text="Solusi : " + ekspresiHasil
    countJumlah[0] = countJumlah[0]-4
    labeljumlah.configure(text="Sisa Kartu : " + str(countJumlah[0]))
    scorelabel.configure(text="Score : " + str(score))

root = Tk()
root.title('Belum Jadi Org')

CA = ImageTk.PhotoImage(Image.open("img/AC.png").resize((130, 200), Image.ANTIALIAS)) #size sudah sesuai dengan skala gambar asli
DA = ImageTk.PhotoImage(Image.open("img/AD.png").resize((130, 200), Image.ANTIALIAS))
HA = ImageTk.PhotoImage(Image.open("img/AH.png").resize((130, 200), Image.ANTIALIAS))
SA = ImageTk.PhotoImage(Image.open("img/AS.png").resize((130, 200), Image.ANTIALIAS))
C2 = ImageTk.PhotoImage(Image.open("img/2C.png").resize((130, 200), Image.ANTIALIAS))#
D2 = ImageTk.PhotoImage(Image.open("img/2D.png").resize((130, 200), Image.ANTIALIAS))
H2 = ImageTk.PhotoImage(Image.open("img/2H.png").resize((130, 200), Image.ANTIALIAS))
S2 = ImageTk.PhotoImage(Image.open("img/2S.png").resize((130, 200), Image.ANTIALIAS))
C3 = ImageTk.PhotoImage(Image.open("img/3C.png").resize((130, 200), Image.ANTIALIAS))#
D3 = ImageTk.PhotoImage(Image.open("img/3D.png").resize((130, 200), Image.ANTIALIAS))
H3 = ImageTk.PhotoImage(Image.open("img/3H.png").resize((130, 200), Image.ANTIALIAS))
S3 = ImageTk.PhotoImage(Image.open("img/3S.png").resize((130, 200), Image.ANTIALIAS))
C4 = ImageTk.PhotoImage(Image.open("img/4C.png").resize((130, 200), Image.ANTIALIAS))#
D4 = ImageTk.PhotoImage(Image.open("img/4D.png").resize((130, 200), Image.ANTIALIAS))
H4 = ImageTk.PhotoImage(Image.open("img/4H.png").resize((130, 200), Image.ANTIALIAS))
S4 = ImageTk.PhotoImage(Image.open("img/4S.png").resize((130, 200), Image.ANTIALIAS))
C5 = ImageTk.PhotoImage(Image.open("img/5C.png").resize((130, 200), Image.ANTIALIAS))#
D5 = ImageTk.PhotoImage(Image.open("img/5D.png").resize((130, 200), Image.ANTIALIAS))
H5 = ImageTk.PhotoImage(Image.open("img/5H.png").resize((130, 200), Image.ANTIALIAS))
S5 = ImageTk.PhotoImage(Image.open("img/5S.png").resize((130, 200), Image.ANTIALIAS))
C6 = ImageTk.PhotoImage(Image.open("img/6C.png").resize((130, 200), Image.ANTIALIAS))#
D6 = ImageTk.PhotoImage(Image.open("img/6D.png").resize((130, 200), Image.ANTIALIAS))
H6 = ImageTk.PhotoImage(Image.open("img/6H.png").resize((130, 200), Image.ANTIALIAS))
S6 = ImageTk.PhotoImage(Image.open("img/6S.png").resize((130, 200), Image.ANTIALIAS))
C7 = ImageTk.PhotoImage(Image.open("img/7C.png").resize((130, 200), Image.ANTIALIAS))#
D7 = ImageTk.PhotoImage(Image.open("img/7D.png").resize((130, 200), Image.ANTIALIAS))
H7 = ImageTk.PhotoImage(Image.open("img/7H.png").resize((130, 200), Image.ANTIALIAS))
S7 = ImageTk.PhotoImage(Image.open("img/7S.png").resize((130, 200), Image.ANTIALIAS))
C8 = ImageTk.PhotoImage(Image.open("img/8C.png").resize((130, 200), Image.ANTIALIAS))#
D8 = ImageTk.PhotoImage(Image.open("img/8D.png").resize((130, 200), Image.ANTIALIAS))
H8 = ImageTk.PhotoImage(Image.open("img/8H.png").resize((130, 200), Image.ANTIALIAS))
S8 = ImageTk.PhotoImage(Image.open("img/8S.png").resize((130, 200), Image.ANTIALIAS))
C9 = ImageTk.PhotoImage(Image.open("img/9C.png").resize((130, 200), Image.ANTIALIAS))#
D9 = ImageTk.PhotoImage(Image.open("img/9D.png").resize((130, 200), Image.ANTIALIAS))
H9 = ImageTk.PhotoImage(Image.open("img/9H.png").resize((130, 200), Image.ANTIALIAS))
S9 = ImageTk.PhotoImage(Image.open("img/9S.png").resize((130, 200), Image.ANTIALIAS))
C9 = ImageTk.PhotoImage(Image.open("img/9C.png").resize((130, 200), Image.ANTIALIAS))#
D9 = ImageTk.PhotoImage(Image.open("img/9D.png").resize((130, 200), Image.ANTIALIAS))
H9 = ImageTk.PhotoImage(Image.open("img/9H.png").resize((130, 200), Image.ANTIALIAS))
S9 = ImageTk.PhotoImage(Image.open("img/9S.png").resize((130, 200), Image.ANTIALIAS))
C10 = ImageTk.PhotoImage(Image.open("img/10C.png").resize((130, 200), Image.ANTIALIAS))#
D10 = ImageTk.PhotoImage(Image.open("img/10D.png").resize((130, 200), Image.ANTIALIAS))
H10 = ImageTk.PhotoImage(Image.open("img/10H.png").resize((130, 200), Image.ANTIALIAS))
S10 = ImageTk.PhotoImage(Image.open("img/10S.png").resize((130, 200), Image.ANTIALIAS))
CJ = ImageTk.PhotoImage(Image.open("img/JC.png").resize((130, 200), Image.ANTIALIAS))#
DJ = ImageTk.PhotoImage(Image.open("img/JD.png").resize((130, 200), Image.ANTIALIAS))
HJ = ImageTk.PhotoImage(Image.open("img/JH.png").resize((130, 200), Image.ANTIALIAS))
SJ = ImageTk.PhotoImage(Image.open("img/JS.png").resize((130, 200), Image.ANTIALIAS))
CQ = ImageTk.PhotoImage(Image.open("img/QC.png").resize((130, 200), Image.ANTIALIAS))#
DQ = ImageTk.PhotoImage(Image.open("img/QD.png").resize((130, 200), Image.ANTIALIAS))
HQ = ImageTk.PhotoImage(Image.open("img/QH.png").resize((130, 200), Image.ANTIALIAS))
SQ = ImageTk.PhotoImage(Image.open("img/QS.png").resize((130, 200), Image.ANTIALIAS))
CK = ImageTk.PhotoImage(Image.open("img/KC.png").resize((130, 200), Image.ANTIALIAS))#
DK = ImageTk.PhotoImage(Image.open("img/KD.png").resize((130, 200), Image.ANTIALIAS))
HK = ImageTk.PhotoImage(Image.open("img/KH.png").resize((130, 200), Image.ANTIALIAS))
SK = ImageTk.PhotoImage(Image.open("img/KS.png").resize((130, 200), Image.ANTIALIAS))
defaultimg = ImageTk.PhotoImage(Image.open("img/blue_back.png").resize((130, 200), Image.ANTIALIAS))#

imgClist=[CA,C2,C3,C4,C5,C6,C7,C8,C9,C10,CJ,CQ,CK]
imgDlist=[DA,D2,D3,D4,D5,D6,D7,D8,D9,D10,DJ,DQ,DK]
imgHlist=[HA,H2,H3,H4,H5,H6,H7,H8,H9,H10,HJ,HQ,HK]
imgSlist=[SA,S2,S3,S4,S5,S6,S7,S8,S9,S10,SJ,SQ,SK]

frameJudul = Frame(root)
frameJudul.place(relwidth=1, relheight=0.2, relx=0.5, rely=0, anchor=N)
frameKartu = Frame(root)
frameKartu.place(relwidth=1, relheight=0.4, relx=0.5, rely=0.2, anchor=N)
frameExp = Frame(root)
frameExp.place(relwidth=1, relheight=0.2, relx=0.5, rely=0.8, anchor=S)
frameOther = Frame(root)
frameOther.place(relwidth=1, relheight=0.2, relx=0.5, rely=1, anchor=S)

Judul = Label(frameJudul, text="Permainan Kartu 24", font =('bold',30))
Judul.place(relx=0.5, rely=0.1, anchor=N)

Kartu1 = Label(frameKartu, image=defaultimg)
Kartu1.place(relx=0.0625, rely=0.5, anchor=W)#, bordermode=OUTSIDE)

Kartu2 = Label(frameKartu, image=defaultimg)
Kartu2.place(relx=0.3125, rely=0.5, anchor=W)

Kartu3 = Label(frameKartu, image=defaultimg)
Kartu3.image = H2
Kartu3.place(relx=0.6875, rely=0.5, anchor=E)

Kartu4 = Label(frameKartu, image=defaultimg)
Kartu4.image = S2
Kartu4.place(relx=0.9375, rely=0.5, anchor=E)

ekspresi = Label(frameExp, text="Solusi : ", relief="groove", font =(20) )
ekspresi.place(relx=0.5, rely=0.2, anchor=N)

start = Button(frameExp,text="Start", font =(20), command =lambda: buttonCallBack(counterJenisKartu,counterJumlahKartu))
start.place(relx=0.5, rely=0.4, anchor=N)

labeljumlah = Label(frameOther,text="Sisa Kartu : 52", font=(30))
labeljumlah.place(relx=0, rely=0.5, anchor=W)

scorelabel = Label(frameOther,text="Score : ", font=(30))
scorelabel.place(relx=1, rely=0.5, anchor=E)

root.mainloop()
