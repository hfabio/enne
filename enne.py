from time import sleep
import pafy
import os
import shutil
import sys
import json

with open('./config.json', 'r') as reader:
  config = json.loads(reader.read())

class Kickstart:
    def __init__(self):
      if not config['initialized']:
          print('\n'*50)
          print('Esta é a primeira vez que você está executando o Enne.')
          print('O diretório que está configurado atualmente é o {}'.format(config['download_path']))
          resp = input('Você deseja alterá-lo? (S/N)\n')
          config['initialized'] = True
          if resp.lower() == 's':
              new_directory = input('Digite o novo diretório:\n')
              while not os.path.isdir(os.path.expanduser(new_directory)):
                  new_directory = input('Desculpe, o seu diretório não é válido, tente novamente:\n')
              config['download_path'] = os.path.expanduser(new_directory)
              print('Diretório padrão setado!')
          else:
              if not os.path.isdir(config['download_path']):
                  config['download_path'] = os.path.expanduser(config['download_path'])
                  os.makedirs(config['download_path'], exist_ok=True)
          with open('./config.json' ,'w') as writer:
                  writer.write(json.dumps(config))
          resp = input('Você quer fazer um download de teste? (S/N)\n')
          if resp.lower().strip() == 's':
              print('\n' + '-'*50)
              for music in config['test_songs']:
                  download(music['url'].replace(r'\\', '\\'))
              print('-'*50 + '\n\n')
              print('Músicas baixadas!')
          print('Seu enne está configurado, aproveite!\n')


class Download:
    def __init__(self,url):
        local_url = url
        self.url = "\\".join(local_url.split('\\'))
        self.video = pafy.new(self.url)
        self.arquivomp3 = ''
        self.pasta = ''
    def GoDownload(self):
        video = self.video
        try:
            bestaudio = video.getbestaudio(preftype="webm")
            self.pasta = config['download_path']
            self.arquivomp3 = self.pasta +str(video.title)+".mp3" if self.pasta[-1] == '/' else self.pasta+"/"+str(video.title)+".mp3"
            bestaudio.download(self.arquivomp3)
            print("| baixada com sucesso -> {}".format(video.title))
            return {'title': str(self.video.title), 'url': self.url}
        except:
            print("ERRO! Download não realizado")

def download(link):
    down = Download(link)
    already_downloaded = [x['url'] for x in config['downloaded_songs']]
    if link not in already_downloaded:
        downloaded = down.GoDownload()
        with open('./config.json', 'w') as writer:
            config['downloaded_songs'].append(downloaded)
            writer.write(json.dumps(config))
            writer.close()
    else:
      print('Essa música já foi baixada, pulamos este download!')


if len(sys.argv) > 1:
    link = sys.argv[1]
else:
    link = ''

while True:
    print('\n'*50)
    Kickstart()
    if link == '':
        link = input('Por favor, digite o url da música que você deseja baixar:\n')
    download(link)
    repeticao = input("Fazer um novo download? [S/N]: ")
    if 's' != repeticao.lower():
        print('\n'*50)
        print('Esta é a lista de musicas baixadas:\n')
        for musica in config['downloaded_songs']:
          print('| - {}'.format(musica['title']))
        print('\nVocê pode encontrá-las em: {}'.format(config['download_path']))
        print('Até mais!')
        break
    else:
      link = ''