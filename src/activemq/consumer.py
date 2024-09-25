import stomp
import base64
import os
from datetime import datetime

# Classe para o consumidor
class ImageListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    # Callback que é chamado quando uma mensagem é recebida
    def on_message(self, frame):
        # Recebendo a imagem codificada em Base64
        encoded_image = frame.body

        # Decodificando a imagem
        image_bytes = base64.b64decode(encoded_image)
        
        # Gerando um nome único para o arquivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"received_image_{timestamp}.png"
        
        # Salvando a imagem
        with open(file_name, "wb") as image_file:
            image_file.write(image_bytes)

        print(f"Imagem recebida e salva como {file_name}.")

# Função para receber a imagem
def receive_image():
    conn = stomp.Connection([('localhost', 61613)])
    listener = ImageListener(conn)
    conn.set_listener('', listener)
    conn.connect(wait=True)

    # Inscrevendo-se na fila
    conn.subscribe(destination='/queue/imageQueue', id=1, ack='auto')

    print("Consumidor ativo, aguardando novas imagens...")

    # Mantém o consumidor ativo para processar mensagens continuamente
    while True:
        try:
            # O cliente deve aguardar por mensagens
            pass
        except KeyboardInterrupt:
            print("Desconectando...")
            conn.disconnect()
            break

receive_image()

