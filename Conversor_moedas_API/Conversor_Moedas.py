import PySimpleGUI as sg
import requests


sg.theme('Dark gray 1')
def pegar_cotacao(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print("Código de moeda Invalido")
        return None

#importa - cria layout - cria janela - wile true - fechar janela
layout = [
    [sg.Text("Pegar cotação da Moeda")],
    [sg.InputText(key="nome_cotacao", size=(13,1))], #tem que passar o parametro chave, para poder chamar esse input em outra função
    [sg.Button("Pegar Cotacao", mouseover_colors='#16F25C'), sg.Button("Cancelar", mouseover_colors='#E4080A')],
    [sg.Text("", key="texto_cotacao")],# texto, botao, input, devem ter o parametro key para poder usar ou chamar em outra função
]

# depois de definir a janela, tem que passar o Window, 2 parametros titulo e o nome do layout
janela = sg.Window("Sistema de Cotações", layout)

while True: 
    evento, valores = janela.read() #sempre dois paramentros
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar Cotacao":
       codigo_cotacao = valores["nome_cotacao"]
       cotacao = pegar_cotacao(codigo_cotacao)
       cotacao = float(cotacao)
       janela["texto_cotacao"].update(f"Cotação do {codigo_cotacao} é de R${cotacao:.2f}")
       
janela.close()