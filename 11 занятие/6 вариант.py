# -- coding: utf-8 --
import json
import requests
import tkinter
def buttonF():
    with open("C:\\Users\\penki\\Documents\\GitHub\\op\\11 занятие\\файл для записи.json","w") as g:
        username="firehol"
        url=f"https://api.github.com/users/{username}"
        user_data=requests.get(url).json()
        data=user_data.keys()
        elem=['company','created_at','email','id','name','url']
        for i in data:
            for i in elem:
                g.write(f"{i}:{user_data[i]}" + '\n')
            return()
window = tkinter.Tk()
window.title('GET request on GitHub')
window.geometry('700x350')

lbl=tkinter.Label(window, text='ВВЕДИТЕ ИМЯ РЕПОЗИТОРИЯ', font=("Arial Bold", 20))
lbl.grid(column=0, row=2)

txt=tkinter.Entry(window, width=30)
txt.grid(column=0, row=3)

btn=tkinter.Button(window, text="Click", command=buttonF)
btn.grid(column=0,row=4)

window.mainloop()