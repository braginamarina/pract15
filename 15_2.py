from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

root = Tk()
root.title("Котики")
root.geometry("450x550")
root['bg'] = "#FFD6E7"
root.iconbitmap("cat.ico")


def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    data = requests.get(url).json()

    img_url = data[0]["url"]

    img_data = requests.get(img_url).content
    img = Image.open(BytesIO(img_data))
    img = img.resize((350, 320))

    photo = ImageTk.PhotoImage(img)

    label_img.config(image=photo)
    label_img.image = photo



title = Label(root,text="♥Cute Cats♥",font=("Arial", 24, "bold"),bg="#FFD6E7",fg="#C2185B")
title.pack(pady=25)

frame = Frame(root,bg="#FFF0F6",width=380,height=350)

frame.pack(pady=10)
frame.pack_propagate(False)

label_img = Label(frame, bg="#FFF0F6")
label_img.pack(expand=True)

btn = Button(root,text="🐾Показать котика🐾",font=("Arial", 14, "bold"),bg="#FF5C9A",fg="white",command=get_cat)
btn.pack(pady=20)

root.mainloop()