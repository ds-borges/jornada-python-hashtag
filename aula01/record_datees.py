import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

#Abrindo o site que iremos trabalhar
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Fazendo Login
time.sleep(5)
pyautogui.click(x=768, y=509)
pyautogui.write("teste")
pyautogui.press("tab")
pyautogui.write("teste@1221")
pyautogui.press("enter")

#Cadastrando os proddutos
time.sleep(1)


file= "produtos.csv"
tabela = pandas.read_csv(file)
for linha in range(len(tabela)):
    pyautogui.click(x=670, y=368)
    codigo=tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca=tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo=tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria=str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco=str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo=str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs=str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(10000)

#print(tabela)

