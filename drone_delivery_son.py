try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

root = tk.Tk()
root.geometry("1400x700+0+0")
root.title('BAŞLANGIÇ')
class simulasyon:
    IsPositionSelected = False
    fx = 0
    fy = 0
    baslangicX = 0
    baslangicY = 0
    HedefX = 0
    HedefY = 0
    def baslat(_m,r):
        r.destroy()

        def showxy(event):
            global IsPositionSelected
            global fx
            global fy

            fx = event.x - canvasSize[0]
            fy = event.y - canvasSize[1]
            IsPositionSelected = True
            SecilenKonum = f'Seçilen Konum -> x = {fx}, y = {fy}'
            info['text'] = SecilenKonum

        def BaslangicSecildi():
            global baslangicX
            global baslangicY
            if IsPositionSelected == True:
                baslangicX = fx
                baslangicY = fy
                SecilenKonum = f'Seçilen Konum -> x = {fx}, y = {fy}'
                infoBaslangicKonumu['text'] = SecilenKonum


        def HedefSecildi():
            global HedefX
            global HedefY
            if IsPositionSelected == True:
                HedefX = fx
                HedefY = fy
                SecilenKonum = f'Seçilen Konum -> x = {fx}, y = {fy}'
                infoHedefKonum['text'] = SecilenKonum

        window = tk.Tk()
        window.title("DRONE DELIVERY SIMULATION")
        window.geometry("1400x700+0+0")
        resim = tk.PhotoImage(file=_m)
        w = resim.width()
        h = resim.height()
        print(w,h)

        canvasSize = [0, 0, w, h]
        _map = tk.Canvas(window, width=canvasSize[2], height=canvasSize[3], bg='white')
        #_map.pack(side='bottom', fill='both')
        _map.pack()
        #_map.create_rectangle(canvasSize[0], canvasSize[1], canvasSize[2], canvasSize[3],fill="white", tag='rectangle')
        _map.create_image(canvasSize[0], canvasSize[1], image=resim, tag='image',anchor='nw')
        _map.tag_bind('image', '<Button-1>', showxy)

        info = tk.Label(window, text="Seçim Yapılmadı", height=1, width=40)
        info.place(x=800, y=595)
        infoBaslangicKonumu = tk.Label(window, text="Başlangıç Konumu Seçilmedi", height=1, width=40)
        infoBaslangicKonumu.place(x=800, y=635)
        infoHedefKonum = tk.Label(window, text="Başlangıç Konumu Seçilmedi", height=1, width=40)
        infoHedefKonum.place(x=800, y=675)

        btnBaslangicKonumuSec = tk.Button(window, text="BAŞLANGIÇ KONUMU SEÇ", command= BaslangicSecildi, height=1,width=20)
        btnBaslangicKonumuSec.place(x=50, y=600)

        btnHedefKonumuSec = tk.Button(window, text="HEDEF KONUMU SEÇ", command=HedefSecildi, height=1, width=20)
        btnHedefKonumuSec.place(x=50, y=640)
        def turtle():
            import turtle
            t = turtle.RawTurtle(_map)
            t.setx(0)
            t.sety(0)
            t.goto(100,100)
        btnturtle = tk.Button(window, text="başlat", command=turtle, height=1, width=20)
        btnturtle.place(x=50, y=680)

        window.mainloop()

def image(n,s):
    tk.Label(root, text='HARİTA SEÇİNİZ', font=(
        'Verdana', 15)).place(x=600, y=0)
    _file = f"images//harita{n}.png"
    filename = tk.PhotoImage(file=_file)

    background_label = tk.Label(root, image=filename)
    background_label.place(x=0, y=25, relwidth=1, relheight=1)

    photo = tk.PhotoImage(file="images//harita1.png")
    photoImage = photo.subsample(5, 5)
    tk.Button(root, image=photoImage, text='HARİTA 1', compound=tk.BOTTOM, command=lambda: image(1, 0)).place(x=100, y=500)
    photo2 = tk.PhotoImage(file="images//harita2.png")
    photoImage2 = photo2.subsample(5, 5)
    tk.Button(root, image=photoImage2, text='HARİTA 2', compound=tk.BOTTOM, command=lambda: image(2, 0)).place(x=500, y=500)
    photo3 = tk.PhotoImage(file="images//harita3.png")
    photoImage3 = photo3.subsample(5, 5)
    tk.Button(root, image=photoImage3, text='HARİTA 3', compound=tk.BOTTOM, command=lambda: image(3, 0)).place(x=900, y=500)
    
    tk.Button(root, text='Simulasyonu Başlat', command=lambda: simulasyon.baslat(_file, root)).place(x=900, y=650)
    tk.mainloop()

image(0,0)
