import pyautogui
import time
from mouseinfo import mouseInfo
#pyautogui.click() => Clica na tela aonde o mouse estiver posicionado
#pyautogui.press() => Pressiona uma tecla do teclado
#pyautogui.write() => Escreve o que está entre aspas
#pyautogui.hotkey() => Pressiona as teclas que estão entre aspas ao mesmo tempo

#PASSO A PASSO
pyautogui.PAUSE = 0.5 # Pausa de 1 segundo entre cada ação

# 1. Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# espera 3s
time.sleep(3) # Espera 3 segundos para a página carregar

# 2. Fazer login com o usuário e senha

pyautogui.click(x=787, y=402) # Clica no campo de login
pyautogui.write('hashtag') # Digita o usuário

pyautogui.press('tab') # Clica no campo de senha
pyautogui.write('djkawldskldjahwilduasidjhaikwudALKJWHDAKLJHSDLAIWD') # Digita a senha

pyautogui.press('tab') # Clica no botão de entrar
pyautogui.press('enter') # Clica no botão de entrar

time.sleep(3) # Espera 3 segundos para a página carregar

# 3. Importar a base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv') # Lê o arquivo CSV
# 4. Cadastrar 1 produto


for linha in tabela.index:
    pyautogui.click(x=772, y=293)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if(obs == 'nan'):
        pyautogui.press('tab')
    else:
        pyautogui.write(obs)
        pyautogui.press('tab')
    
    pyautogui.press('enter')

# 5. Repetir para todos os produtos
