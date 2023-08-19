import PySimpleGUI as sg

def create_window(theme):
    sg.theme('DarkBlue',)
    sg.set_options(font = 'Franklin 14', button_element_size = (10, 2))
    button_size = (6, 2)

    layout = [
    # [sg.Text('Resultado', justification = 'center', expand_x = True)],
    [sg.Push(), sg.Text('Resultado', pad = (10, 24))],
    [sg.Button('Clear', expand_x = True),sg.Button('Enter', expand_x = True)],
    [sg.Button('1/x', size = button_size), sg.Button('x²', size = button_size), sg.Button('²√x', size = button_size), sg.Button('÷', size = button_size)],
    [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('×', size = button_size)],
    [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('-', size = button_size)],
    [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('+', size = button_size)],
    [sg.Button('+/-', size = button_size), sg.Button(0, size = button_size), sg.Button(',', size = button_size), sg.Button('=', size = button_size)],
    ]

    return sg.Window('calculadora', layout)

window = create_window('DarkBlue')

current_num = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
     break

if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
    current_num.append(event)

window.close()