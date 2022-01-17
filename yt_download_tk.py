from tkinter import *
import pytube

root = Tk()
root.title("Скачивание видео с YT")
root.geometry('400x350')
icon = PhotoImage(file="icons/icon.png")
root.iconphoto(False, icon)
root.resizable(False, False)

def download():
    ent_status.delete(0, END)
    ent_title.delete(0, END)
    ent_views.delete(0, END)
    ent_length.delete(0, END)

    lnk = ent_link.get()
    lnk = str(lnk)
    pth = ent_path.get()
    pth = str(pth)
        
    try:
        link = pytube.YouTube(lnk)
        stream = link.streams.get_highest_resolution()
        stream.download(pth)       #Путь установки. По дефолту - в папку проекта.

        ent_status.configure(fg="green", font=("Courier", 10, "bold"))
        ent_status.insert(0, "Видео загружено!")
    except pytube.exceptions.RegexMatchError:
        ent_status.configure(fg="red", font=("Courier", 10, "bold"))
        ent_status.insert(0, "Неправильная ссылка!")

    ent_title.insert(0, link.title)
    ent_views.insert(0, link.views)
    ent_length.insert(0, link.length)


lbl_link = Label(root, text="Введите ссылку на видео:")
lbl_link.pack()
ent_link = Entry(root, width=50, borderwidth=3, relief=SOLID)
ent_link.pack()

lbl_path = Label(root, text="Введите путь для сохранения:")
lbl_path.pack()
ent_path = Entry(root, width=50, borderwidth=3, relief=SOLID)
ent_path.pack()

# Вывод инфо о видео
lbl_info = Label(root, text="Информация о видео", fg="red")
lbl_info.configure(font=("Courier", 14, "bold"))
lbl_info.pack(pady=5)

lbl_title = Label(root, text="Название видео:")
lbl_title.pack()
ent_title = Entry(root, width=50, borderwidth=2)
ent_title.pack()

lbl_views = Label(root, text="Количество просмотров:")
lbl_views.pack()
ent_views = Entry(root, width=20, borderwidth=2)
ent_views.pack()

lbl_length = Label(root, text="Длина видео(в сек.):")
lbl_length.pack()
ent_length = Entry(root, width=20, borderwidth=2)
ent_length.pack()

lbl_status = Label(root, text="Статус:")
lbl_status.pack()
global ent_status
ent_status = Entry(root, width=25, borderwidth=2)
ent_status.pack()

but_start = Button(root, text="Скачать", width=25, height=2, activebackground="red", borderwidth=3, relief=RIDGE, bg="white", command=download)
but_start.configure(font=("Courier", 10, "bold"))
but_start.pack(pady=10)

root.mainloop()