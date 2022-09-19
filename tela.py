import PySimpleGUI as sg 

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text("Login", size=(5, 0)), sg.Input(size=(20, 0), key='login')],
            [sg.Text("Senha", size=(5, 0)), sg.Input(size=(20, 0), key='senha', password_char='*')],
            [sg.Checkbox("Salvar o login ?")],
            [sg.Button("New user"), sg.Button("Log in"), sg.Button("Go out")],
            [sg.Output(size=(20, 10))]
        ]
        #janela
        self.janela = sg.Window("Janela de login").layout(layout)
        
        
    def Iniciar(self):
        while True:
            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
        
            login = self.values['login']
            senha = self.values['senha']
            print(f'login: {login}')
            print(f'senha: {senha}')
        
tela = TelaPython()
tela.Iniciar()




