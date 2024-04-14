from PySimpleGUI import PySimpleGUI as sg

sg.theme = 'Reddit'

layout = [
    [sg.InputText(key='display', size=(18,5), disabled=True, text_color='black', background_color='white')],
    [sg.Button('C', expand_x=True, enable_events=True, size=(2,1)), sg.Button('/', enable_events=True, size=(2,1), )],
    [sg.Button('7', expand_x=True, enable_events=True, size=(2,1)), sg.Button('8', expand_x=True, enable_events=True, size=(2,1)), sg.Button('9', expand_x=True, enable_events=True, size=(2,1)), sg.Button('*', expand_x=True, enable_events=True, size=(2,1))],
    [sg.Button('4', expand_x=True, enable_events=True, size=(2,1)), sg.Button('5', expand_x=True, enable_events=True, size=(2,1)), sg.Button('6', expand_x=True, enable_events=True, size=(2,1)), sg.Button('-', expand_x=True, enable_events=True, size=(2,1))],
    [sg.Button('1', expand_x=True, enable_events=True, size=(2,1)), sg.Button('2', expand_x=True, enable_events=True, size=(2,1)), sg.Button('3', expand_x=True, enable_events=True, size=(2,1)), sg.Button('+', expand_x=True, enable_events=True, size=(2,1))],
    [ sg.Button('0', enable_events=True, size=(9,1), expand_x=True), sg.Button('=', enable_events=True, size=(2,1), expand_x=True)]
]

janela = sg.Window('Calculadora', layout,)

# Mapeamento de botões para seus valores
button_values = {
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '=': '=', '/': '/', '*': '*', '-': '-', '+': '+',
}
expression = '' #conteudo do display

while True: 
    calcular, valores = janela.read()
    if calcular == sg.WINDOW_CLOSED:
        break
    if calcular == 'C':  # Se o botão 'C' foi pressionado
        expression = ''
        janela['display'].update(expression) 
    elif calcular in button_values:  # Se um botão numérico ou de operação foi pressionado
        if calcular == '=':
            try:
                # Avalia a expressão e atualiza o campo de entrada com o resultado
                result = str(eval(expression))
                janela['display'].update(result)
                expression = result  # Atualiza a expressão com o resultado para permitir cálculos contínuos
            except Exception as e:
                # Em caso de erro na expressão, exibe uma mensagem de erro
                janela['display'].update('Error')
                expression = ''
        else:
            # Concatena o valor do botão pressionado na expressão
            expression += button_values[calcular]
            janela['display'].update(expression)

janela.close()