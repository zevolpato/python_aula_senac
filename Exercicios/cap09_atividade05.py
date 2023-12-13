from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def enviar(nome):
  try:
    mensagem = driver.find_element(By.XPATH, MESSAGE_BOX)
    mensagem.click()
    mensagem.send_keys(f"Olá *{nome}*, tudo bem?")
    mensagem.send_keys(Keys.CONTROL, Keys.RETURN)
    mensagem.send_keys("Esta é uma mensagem de *Teste*.")
    sleep(3)
    botao = driver.find_element(By.XPATH, SEND)
    botao.click()
    return 'Enviado'
  except Exception as e:
    return 'Sem Whatsapp'

WP_LINK = 'https://web.whatsapp.com'
## XPATHS
SEND = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'

driver = webdriver.Chrome()
driver.get(WP_LINK)

listaTelefone = ['5512981256440', '5512999999999']
listaNome = ['Laercio', 'Teste']

contador = True
while (contador):
  sleep(3)
  try:
    driver.find_element(By.XPATH, NEW_CHAT)
    contador = False
  except:
    print("Por favor scaneie o QR Code")
    contador = True

envio = []
for nome, telefone in zip(listaNome, listaTelefone):
  try:
    sleep(3)
    url = f"https://web.whatsapp.com/send?phone={telefone}"
    driver.get(url)
    sleep(5)
    status = enviar(nome)
    print(f"Telefone: {telefone} - {nome} | {status}")
  except Exception as e:
    driver.execute_script("window.stop();")
    print(f"Telefone: {telefone} - {nome} | ERRO ao Enviar")
    status = 'Erro ao enviar'

  envio.append(status)

print(envio)
sleep(5)
driver.close()