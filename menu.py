from tkinter.constants import TRUE
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED, Button, Prog

class Program:
    def __init__(self):
        None
    
    #starwindow
    def start_window(self):
        #layout
        sg.theme('LightBlue')
        layout = [
            [sg.Text('Login Test', font='Bahnschrift 25')],
            [sg.Text('Usuário'), sg.InputText(size=(60,60))],
            [sg.Text('Senha  '), sg.InputText(password_char='*',size=(30,30))],
            [sg.Button('Novo usuário?'), sg.Button(button_text='Entrar')]
        ]

        #window
        return sg.Window('Login Test', layout=layout, size=(600,600), finalize=True)

    #registration window
    def rg_window(self):
      #layout of screen 2
        layout2 = [
          [sg.Text('Novo usuário')],
          [sg.Text('Nome'), sg.InputText(size=(90,60))],
          [sg.Text('Senha'), sg.InputText(password_char='*',size=(30,60))],
          [sg.Button(button_text='Registrar')]]
    
        return sg.Window('Registered', layout2, size=(600,600), finalize=True)
    
    
    def loop(self):
        window1, window2 = self.start_window(), None
        while True:
            #reading values and events
            window, event, values = sg.read_all_windows()
            if window == window1 and event == sg.WINDOW_CLOSED:
                break
            if event == 'Novo usuário?':
                window2 = self.rg_window()
                window1.hide()


test1 = Program()
test1.loop()





