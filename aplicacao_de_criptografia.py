import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLabel, QFileDialog
from cryptography.fernet import Fernet

# Definição da classe da aplicação
class CryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("Aplicação de Criptografia")
        self.setGeometry(100, 100, 600, 400)

        # Configuração do widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout vertical para organizar os elementos na janela
        self.layout = QVBoxLayout()

        # Rótulo para a entrada de texto
        self.label = QLabel("Digite sua mensagem:")
        self.layout.addWidget(self.label)

        # Caixa de texto para entrada da mensagem
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        # Botão para criptografar a mensagem
        self.encrypt_button = QPushButton("Criptografar")
        self.encrypt_button.clicked.connect(self.encrypt_message)
        self.layout.addWidget(self.encrypt_button)

        # Botão para descriptografar a mensagem
        self.decrypt_button = QPushButton("Descriptografar")
        self.decrypt_button.clicked.connect(self.decrypt_message)
        self.layout.addWidget(self.decrypt_button)

        # Botão para selecionar um arquivo
        self.select_file_button = QPushButton("Selecionar Arquivo")
        self.select_file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_file_button)

        # Rótulo para exibir o resultado
        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        # Aplicação do layout ao widget central
        self.central_widget.setLayout(self.layout)

        # Geração de uma chave de criptografia
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.selected_file = None

    # Método para criptografar a mensagem
    def encrypt_message(self):
        message = self.text_edit.toPlainText().encode()
        encrypted_message = self.fernet.encrypt(message).decode()
        self.result_label.setText(f"Mensagem Criptografada: {encrypted_message}")

        # Salva a mensagem criptografada em um arquivo de texto na raiz
        with open("mensagem_criptografada.txt", "w") as file:
            file.write(encrypted_message)

    # Método para descriptografar a mensagem
    def decrypt_message(self):
        if self.selected_file is None:
            self.result_label.setText("Por favor, selecione um arquivo primeiro.")
            return

        with open(self.selected_file, "r") as file:
            encrypted_message = file.read()
        
        try:
            decrypted_message = self.fernet.decrypt(encrypted_message.encode()).decode()
            self.result_label.setText(f"Mensagem Descriptografada: {decrypted_message}")

            # Substitui o arquivo com a informação descriptografada
            with open(self.selected_file, "w") as file:
                file.write(decrypted_message)
        except Exception as e:
            self.result_label.setText("Erro ao descriptografar o arquivo.")

    # Método para selecionar um arquivo
    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        selected_file, _ = file_dialog.getOpenFileName(self, "Selecionar Arquivo", "", "Arquivos de Texto (*.txt)")

        if selected_file:
            self.selected_file = selected_file
            self.result_label.setText(f"Arquivo selecionado: {selected_file}")

# Bloco de inicialização da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoApp()
    window.show()
    sys.exit(app.exec())
