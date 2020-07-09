# ENNE
Faça download de suas músicas direto pela linha de comando

O enne é um utilitário via linha de comando escrito em Python3. Sua função primordial é realizar o download de músicas a partir de vídeos do YouTube.
O programa está na sua inicial, então, muitos bugs e adaptações serão feitas no futuro. Espero contar com você, caro leitor, para contribuir com o desenvolvimento desta ferramenta.
Para contribuições(dicas, relatos de bugs, feedback, etc) deixo o link do projeto [GitHub](https://github.com/viktorsht/enne).

## INSTALAÇÃO

Para a utilização do programa é necessário ter ter instalado na sua máquina:

- [Python3](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)
- [pafy](https://pypi.org/project/pafy/)
- [youtube-dl](https://youtube-dl.org/)

Windows:
```dos
  pip install pafy youtube-dl
```
Linux / macOs
```bash
  pip3 install pafy youtube-dl
```

Agora que você instalou todas os pacotes necessários para o funcionamento do programa, clone o repositório em sua máquina [enne](https://github.com/viktorsht/enne.git).  
Pronto, agora você está com todas as ferramentas para baixar suas músicas.  


## UTILIZAÇÃO

Para utilizar o programa é bem simples.
- Vá ,usando a linha de comando, até o diretório do repositório do programa e digite:

  $ python3 enne.py UrlDaMúsica

- O programa salva o nome e o url dos downloads em um arquivo .txt a fim de não realizar repetidos downloads da mesma música.  

- Caso o url já exista no arquivo.txt o programa será fechado.  

- O usuário deve passar o path onde o arquivo deverá ser salvo. O programa identifica a sua pasta de usuário.

- O usuário pode escolher realizar outro download ou não.

### Exemplo

Digite  

  $ python3 enne.py https://www.youtube.com/watch?v=S-xb1miTjoE

Aparecerá uma mensagem na tela: 'Onde deseja salvar a música?'   

  Ex: Música  

e você baixará a Free Software Song(música do movimento do software livre) no formato .mp3 na pasta Música.

## ATUALIZAÇÕES PARA O FUTURO

- Possuir um banco de bados próprio e simples.

- Funções de busca direto do programa.

- Virar um pacote para arquiteturas mais comuns.

## Observações finais

Além de otimizar minhas tarefas e mostrar os resultados dos meus estudos em Python. , este programa é uma forma de mostrar o funcionamento prático da biblioteca Pafy, além de tentar contribuir com a comunidade do Software Livre. Não há intenção alguma de prejudicar pessoas, grupos ou empresas.
