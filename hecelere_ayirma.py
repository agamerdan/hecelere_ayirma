from tkinter import *
from tkinter import font
from tkinter.colorchooser import askcolor

def cumle_yazdir():
    c="Merdan elektrik bölümünde okuyor " 
   
    
    
    root = Tk()
    root.tk_setPalette("white")
    root.attributes("-fullscreen", 1)

    a=Text(root, height=20, width=50,font=('TTKB Dik Temel Abece', 120, 'bold'),fg="red")
    a.tag_configure('color',foreground='blue')
    a.insert(END,"\n ")
    a.pack()
    
    cekimliler = {"â","ê","î","ô","û","a","e","ı","i","o","ö","u","ü","A","E","I","İ","O","Ö","U","Ü"}
    SPELL_SLICER = (('001000', 5), ('000100', 5), ('01000', 4), ('00100', 4), ('00010', 4), ('1000', 3), ('0100', 3),
                    ('0011', 3), ('0010', 3), ('011', 2),('010', 2), ('100', 2), ('10', 1), ('11', 1))

    def wordtoten(word: str):
        wtt = ''

        for ch in word:
            if ch in cekimliler:
                wtt += '1'
            else:
                wtt += '0'
        print(wtt)
        return wtt

    def spellword(word: str):
        heceler = []
        tenword = wordtoten(word)
        cekimlisayisi = tenword.count('1')
        
        for i in range(tenword.count('1')):
            for x, y in SPELL_SLICER:
                if tenword.startswith(x):
                    heceler.append(word[:y])
                    word = word[y:]
                    tenword = tenword[y:]
                    break

        if tenword == '0':
            heceler[-1] = heceler[-1] + word
        elif word:
            heceler.append(word)

        if len(heceler) != cekimlisayisi:
            return False

        return heceler
     
    for enum, kelime in enumerate(spellword(c)):
        if enum%2==0:
            a.insert(END,kelime)
 
        else:
            a.insert(END,kelime,'color')
            
    def cikis():
        root.destroy()
        
        

    def renk():
        color = askcolor()[-1]
        a.tag_add(color, a.index("sel.first"), a.index("sel.last"))
        a.tag_configure(color, foreground=color)        

    buton1 = Button(root,text="Seçili Alanın Rengini Değiştir", command=renk, height=1, width=25, fg="black", bg="white", font="Helvetica 16 bold")
    buton1.place(relx=0.05, rely=0.90)
        
    buton = Button(root,text="Çıkış", command=cikis, height=1, width=7, fg="black", bg="white", font="Helvetica 16 bold")
    buton.place(relx=0.30, rely=0.90)

    root.mainloop()

cumle_yazdir()