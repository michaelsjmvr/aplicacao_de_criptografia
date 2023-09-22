### Hi, I'm Michael D.🤙

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michael-douglas-640a11180/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/michael.douglaspdl/)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/MikeeD.Cloud9/)

# Aplicação de Criptografia

Esta é uma aplicação de criptografia simples que permite criptografar e descriptografar mensagens usando o algoritmo AES (Advanced Encryption Standard) Fernet e também permite selecionar um arquivo para descriptografar e substituir com a informação descriptografada.

## Funcionalidades

- Criptografar mensagens de texto digitadas.
- Descriptografar mensagens previamente criptografadas.
- Selecionar um arquivo de texto para descriptografar e substituir.

## Requisitos

- Python 3.x
- Bibliotecas Python: PySide6 e cryptography

## Instalação

Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

Instale as bibliotecas Python necessárias executando o seguinte comando:

pip install PySide6 cryptography


## Como Usar

1. Execute o aplicativo usando o seguinte comando:

python nome_do_arquivo.py


2. A interface da aplicação será exibida.

3. Digite sua mensagem no campo de texto.

4. Clique no botão "Criptografar" para criptografar a mensagem e um arquivo chamado "mensagem_criptografada.txt" será criado na raiz do diretório com a mensagem criptografada.

5. Para descriptografar uma mensagem, clique no botão "Selecionar Arquivo" para escolher um arquivo de texto previamente criptografado.

6. Após selecionar o arquivo, clique no botão "Descriptografar". O arquivo será descriptografado e seu conteúdo será substituído pela mensagem descriptografada.

## Nota de Segurança

Este projeto é apenas um exemplo simples para fins educacionais e de demonstração. A chave de criptografia é gerada automaticamente e armazenada na memória da aplicação, o que não é seguro para fins de produção. Em um cenário de produção real, você deve implementar uma maneira segura de gerenciar as chaves de criptografia.

