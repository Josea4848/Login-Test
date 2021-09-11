import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED, Prog

class Program:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Login Test', font='Bahnschrift 25')],
            [sg.InputText(size=(60,60))]
        ]

        #window
        self.window = sg.Window('Login Test', layout, size=(600,600))

    def start(self):
        while True:
            #reading values and events
            events, values = self.window.read()
            if events == sg.WINDOW_CLOSED or events == 'Sair':
                break


test1 = Program()
test1.start()





