"""
  Cap09 - Atividade 04
  Realizar um download e descompactar um arquivo
"""
import io
import sys
import os
import zipfile
import urllib.request as request

BUFF_SIZE = 1024
def download(response, output):
  total_downloaded = 0
  while True:
    data = response.read(BUFF_SIZE)
    total_downloaded += len(data)
    if not data:
      break
    output.write(data)
  print('Tamanho do arquivo {bytes}'.format(bytes=total_downloaded))

def zip(path):
  if not os.path.exists(path):
    print("Arquivo {} não existe".format(path))
    sys.exit(-1)
  else:
    zfile = zipfile.ZipFile(path)
    zfile.extractall()
    print("Arquivos extraídos")


url = 'https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_win32.zip'
response = request.urlopen(url)
pasta = os.path.abspath(os.getcwd())
out_file = io.FileIO(f"{pasta}\chromedriver_win32.zip", mode="w")
download(response, out_file)
zip(f"{pasta}\chromedriver_win32.zip")
print(f'Download realizado na pagina {url}')