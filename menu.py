from tkinter.constants import TRUE
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED, Button, Prog
import sqlite3
from time import sleep

class Program:
    def __init__(self):
        None

    #database    
    def registrar(self, name, password):
        self.con = sqlite3.connect('database.db')
        self.cursor = self.con.cursor()

        try:
            self.cursor.execute("""CREATE TABLE usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL
            )


            """)
        except:
            print('Erro')
        sleep(5)
        
        self.cursor.execute(f"""INSERT INTO usuarios (nome, senha)
        VALUES ('{name}', '{password}')""")
        
        self.con.commit()
        self.con.close()
    #checking values in login
    def verificar(self,name,psw):
        self.con = sqlite3.connect('database.db')
        self.cursor = self.con.cursor()
        self.cursor.execute("""
        SELECT * FROM usuarios;""")

        for line in self.cursor.fetchall():
            if name == line[1] and psw == line[2]:
                return True
        self.con.close()
    
    #starwindow
    def start_window(self):
        #layout
        sg.theme('LightBlue')
        layout = [
            [sg.Text('Login Test', font='Bahnschrift 25')],
            [sg.Text('Usuário'), sg.InputText(key='user_login',size=(60,60))],
            [sg.Text('Senha  '), sg.InputText(key='psw_login',password_char='*',size=(30,30))],
            [sg.Button('Novo usuário?'), sg.Button(button_text='Entrar')]
        ]

        #window
        return sg.Window('Login Test', layout=layout, size=(600,600), finalize=True)

    #registration window
    def rg_window(self):
      #layout of screen 2
        layout2 = [
          [sg.Text('Novo usuário')],
          [sg.Text('Nome'), sg.InputText(key='_username_', size=(90,60))],
          [sg.Text('Senha'), sg.InputText(key='password',password_char='*',size=(30,60))],
          [sg.Button(button_text='Registrar')]]
    
        return sg.Window('Registered', layout2, size=(600,600), finalize=True, resizable=True)
    
    
    def loop(self):
        window1, window2 = self.start_window(), None
        bad_characters = ['@','#','$','!','-','%','*','(',')','&','<','>',';',':','/','^','~','=','+']
        while True:
            #reading values and events
            window, event, values = sg.read_all_windows()
            if window == window1 and event == sg.WINDOW_CLOSED:
                break
            
            if event == 'Entrar':
                if self.verificar(values['user_login'],values['psw_login']) == True:
                    sg.PopupNoTitlebar('ABRIU')
            
            if event == 'Novo usuário?':
                window2 = self.rg_window()
                window1.hide()
            
            if window == window2 and event == 'Registrar':
                #temcchar é uma variável do tipo True/False que retorne True se possuir algum caractere indesejado no nome
                temcchar= False
                for c in bad_characters:
                    if c in values['_username_']:
                        temcchar = True

                if len(values['_username_']) < 8 or len(values['password']) < 8 or temcchar > 0:
                    sg.PopupNoTitlebar('(Nome de usário/Senha) não cumprem as especificações')
                
                else:
                    self.registrar(values['_username_'], values['password'])
                    window2.close()
                    window1.un_hide()

test1 = Program()
test1.loop()





