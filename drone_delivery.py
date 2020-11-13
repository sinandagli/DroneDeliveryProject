from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("1400x700+0+0")
root.title('BAŞLANGIÇ')


def baslat(fn,w,n):
    w.destroy()
    _map = Tk()
    _map.geometry("1400x700+0+0")
    _map.title('HARİTA')
    Label(_map, text=f'HARİTA {n} SEÇİLDİ', font=(
        'Verdana', 15)).place(x=550, y=0)
    filename = PhotoImage(file=fn)
    background_label = Label(_map, image=filename)
    background_label.place(x=0, y=25, relwidth=1, relheight=1)
    mainloop()


def image(n):
    Label(root, text='HARİTA SEÇİNİZ', font=(
        'Verdana', 15)).place(x=600, y=0)
    _file = f"images//harita{n}.png"
    filename = PhotoImage(file=_file)

    background_label = Label(root, image=filename)
    background_label.place(x=0, y=25, relwidth=1, relheight=1)
    photo = PhotoImage(file="images//harita1.png")
    photoImage = photo.subsample(5, 5)
    Button(root, image=photoImage, text='HARİTA 1', compound=BOTTOM, command=lambda: image(1)).place(x=100, y=500)
    photo2 = PhotoImage(file="images//harita2.png")
    photoImage2 = photo2.subsample(5, 5)
    Button(root, image=photoImage2, text='HARİTA 2', compound=BOTTOM, command=lambda: image(2)).place(x=500, y=500)
    photo3 = PhotoImage(file="images//harita3.png")
    photoImage3 = photo3.subsample(5, 5)
    Button(root, image=photoImage3, text='HARİTA 3', compound=BOTTOM, command=lambda: image(3)).place(x=900, y=500)

    Button(root, text = 'Simülasyonu Başlat', command=lambda: baslat(_file,root,n)).place(x=900, y=650)
    mainloop()


image(0)
