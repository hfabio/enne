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
- Usando a linha de comando, vá até a pasta do enne e digite:

```bash
  $ python3 enne.py
```
ou
```bash
  $ python3 enne.py UrlDaMúsica
```
**Nota: na primeira vez que você utilizar o programa irá configurar a pasta onde salvará as músicas baixadas**

- O programa salva o nome e o url dos downloads no arquivo de configuração `config.json` a fim de não realizar repetidos downloads da mesma música.

- Caso o url já exista no arquivo o programa avisará e te dará a opção de baixar mais uma música.

- O usuário pode escolher realizar outro download ou não.

### Exemplo

```bash
 hfabio ~/Projetos/enne: python3 enne.py https://www.youtube.com/watch\?v\=0dl9vM7sj50


Esta é a primeira vez que você está executando o Enne.
O diretório que está configurado atualmente é o /home/hfabio/Música/enne/
Você deseja alterá-lo? (S/N)
n
Você quer fazer um download de teste? (S/N)
n
Seu enne está configurado, aproveite!


| baixada com sucesso -> Best Part (Reigh Lofi Remix)
Fazer um novo download? [S/N]: n


Esta é a lista de musicas baixadas:

| - Best Part (Reigh Lofi Remix)

Você pode encontrá-las em: /home/hfabio/Música/enne/
Até mais!
```