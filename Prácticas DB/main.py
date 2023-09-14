import sqlite3 as sql
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


conn = sql.connect('passmg.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    ID_User ROWID INT PRIMARY KEY,
                    User VARCHAR(50),
                    Password VARCHAR(255)
                )
              ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS entity_types (
                    ID_Entity_Type ROWID INT PRIMARY KEY,
                    Entity VARCHAR(50)
                )
              ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Entities (
                    ID_Entity ROWID INT PRIMARY KEY,
                    ID_User TINYINT,
                    ID_Entity_Type TINYINT,
                    
                    Pass_Title VARCHAR(100),
                    Pass_URL VARCHAR(2000),
                    Pass_ID_User VARCHAR(50),
                    Pass_Password VARCHAR(255),
                    Pass_Notes VARCHAR(5000),
                    
                    Bm_Title VARCHAR(100),
                    Bm_URL VARCHAR(2000),
                    Bm_Notes VARCHAR(5000),

                    App_Title VARCHAR(100),
                    App_dir VARCHAR(260),
                    App_ID_User VARCHAR(50),
                    App_Password VARCHAR(255),
                    App_Notes VARCHAR(5000),

                    Contact_Title VARCHAR(100),
                    Contact_Surnames VARCHAR(200),
                    Contact_First_Name VARCHAR(50),
                    Contact_Date DATE,
                    Contact_Phone VARCHAR(20),
                    Contact_Mail VARCHAR(100),
                    Contact_Country VARCHAR(100),
                    Contact_City VARCHAR(100),
                    Contact_Notes VARCHAR(5000),

                    Notes_Title VARCHAR(100),
                    Notes_Notes VARCHAR(5000)                    
                )
              ''')
conn.commit()
conn.close()


app = tk.Tk()
app.title('patata')
window_width = 1440
window_height = 1080

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/ 2 - window_height/ 2)

app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
app.resizable(True, True)

Nombre = Entry(app, background='#202020')
Nombre.place(x=50,y=50)
app.mainloop()