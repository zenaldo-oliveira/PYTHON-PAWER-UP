# Passo a passo do Projeto
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
#   pyautogui.hotkey -> apertar um conjunto de teclado ( ctrl c, Ctrl V, ctrl tab)

# 1. abrir o sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site do sistema 
link_sistema = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")


pyautogui.write(link_sistema)
pyautogui.press("enter")

# 2. Fazer login 
time.sleep(3)
# fazer login 
pyautogui.click(x=-1455, y=521)
pyautogui.click(x=-1250, y=567)
pyautogui.write("zenaldo.221@hotmail.com")

pyautogui.press("tab")
pyautogui.write("casacasacasa")

pyautogui.press("tab") # passou para o botao de logar
pyautogui.press("enter")

time.sleep(3)
# 3. Abrir/importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.pandas.read_csv("produtos.csv")

print(tabela)

# 4. Cadastrar um produto
# str = string = texto

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do codigo do produto
    pyautogui.click(x=-1535, y=371)

    # preencher o codigo
    pyautogui.write(codigo)
    # passar para o proximo campo
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar para o proximo campo
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar para o proximo campo
    pyautogui.press("tab") 
    # custo nan 849.0
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # passar para o proximo campo
    pyautogui.press("tab")
    # apertar o botao   599.0   
    pyautogui.press("enter")
    pyautogui.scroll(5000)


