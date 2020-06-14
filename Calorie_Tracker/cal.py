import tkinter as tk
import sqlite3 as s
import datetime

root = tk.Tk()
root.title('Calorie Tracker')
root.geometry('800x800')
title = tk.Label(root,text='Calorie Intake(Carbs, Protien, Fats)', font=('times new roman', 35, 'bold'), fg='black', bg='yellow')
title.pack()

con = s.connect('calorie.db') 
c = con.cursor() 

Label1 = tk.Label(root, text='Day(dd)', font=('times new roman', 20)).place(relx=0.0, rely=0.1)
Label2 = tk.Label(root, text='month(mm)', font=('times new roman', 20)).place(relx=0.0, rely=0.25)
Label3 = tk.Label(root, text='year(yy)', font=('times new roman', 20)).place(relx=0.0, rely=0.4)
Label4 = tk.Label(root, text='Carbohydrate', font=('times new roman', 20)).place(relx=0.6, rely=0.1)
Label5 = tk.Label(root, text='Protein', font=('times new roman', 20)).place(relx=0.6, rely=0.3)
Label6 = tk.Label(root, text='Fats', font=('times new roman', 20)).place(relx=0.6, rely=0.5)
Label7 = tk.Label(root, text='Total', font=('times new roman', 20)).place(relx=0.0, rely=0.55)

cal = tk.StringVar(root)
cal.set('----') 

caldb = tk.StringVar(root)
caldb.set('----')

day = tk.StringVar(root)
month = tk.StringVar(root)
year = tk.StringVar(root)
carb = tk.StringVar(root)
pro = tk.StringVar(root)
fat = tk.StringVar(root)
total = tk.StringVar(root)

diet = {'ketogenic', 'Intermittent', 'carb-cycle','custom_diet'}

diett = tk.Label(root, text='diet - ', font=('times new roman', 20)).place(relx=0.0, rely=0.175)
cald = tk.OptionMenu(root, cal, *diet)  
cald.place(relx=0.1,rely=0.175)


diett = tk.Label(root, text='Table - ', font=('times new roman', 20)).place(relx=0.0, rely=0.9)
caldd = tk.OptionMenu(root, caldb, *diet) 
caldd.place(relx=0.1,rely=0.9)


dayT = tk.Entry(root, textvariable=day)
dayT.place(relx=0.2, rely=0.1)

monthT = tk.Entry(root, textvariable=month)
monthT.place(relx=0.2, rely=0.25)

yearT = tk.Entry(root, textvariable=year)
yearT.place(relx=0.2, rely=0.4)

totalT = tk.Entry(root, textvariable=total)
totalT.place(relx=0.2, rely=0.55)

carbT = tk.Entry(root, textvariable=carb)
carbT.place(relx=0.8, rely=0.1)

proT = tk.Entry(root, textvariable=pro)
proT.place(relx=0.8, rely=0.3)

fatT = tk.Entry(root, textvariable=fat)
fatT.place(relx=0.8, rely=0.5)
def receive():
        print("You have submitted a record")
        
        c.execute('CREATE TABLE IF NOT EXISTS ' +cal.get()+ ' (Datestamp TEXT, Carbs INTEGER, Protiens INTEGER, Fats INTEGER, Total INTEGER)') #SQL syntax
        
        date = datetime.date(int(year.get()),int(month.get()), int(day.get())) 

        c.execute('INSERT INTO ' +cal.get()+ ' (Datestamp, Carbs, Protiens, Fats, Total) VALUES (?, ?, ?, ?, ?)',
                  (date, carb.get(), pro.get(), fat.get(), total.get())) 
        con.commit()


        cal.set('----')
        caldb.set('----')
        day.set('')
        month.set('')
        year.set('')
        carb.set('')
        pro.set('')
        fat.set('')
        total.set('')


def clear():
        cal.set('----')
        caldb.set('----')
        month.set('')
        year.set('')
        carb.set('')
        pro.set('')
        fat.set('')
        total.set('')
def note():
    c.execute('SELECT * FROM ' +caldb.get())

    frame = tk.Frame(root)
    frame.place(relx= 0.4, rely = 0.6)
    
    Lb = tk.Listbox(frame, height = 8, width = 25,font=("arial", 12)) 
    Lb.pack(side = 'left')
    
    scroll = tk.Scrollbar(frame, orient = 'vertical') 
    scroll.config(command = Lb.yview)
    scroll.pack(side = 'right')
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'Date, carbs, protein, fats, total')
    
    data = c.fetchall() 
    
    for row in data:
        Lb.insert(1,row) 

    L7 = tk.Label(root, text = caldb.get()+ '      ', 
               font=("arial", 16)).place(relx=0.4,rely=0.55) 

    L8 = tk.Label(root, text = "They are ordered from most recent", 
               font=("arial", 16)).place(relx=0.4,rely=0.85)
    con.commit()

button_1 = tk.Button(root, text="Submit",command=receive)
button_1.place(relx=0.2,rely=0.7)

button_2 = tk.Button(root,text= "Clear",command=clear)
button_2.place(relx=0.8,rely=0.7)

button_3 = tk.Button(root,text="Open DB",command=note)
button_3.place(relx=0.5,rely=0.9)
root.mainloop()