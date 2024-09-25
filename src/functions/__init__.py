import qrcode
from PIL import Image
import base64
from io import BytesIO
import stomp  # Certifique-se de ter a biblioteca stomp instalada

def send_image(image_bytes):
    # Conectando ao ActiveMQ (localhost na porta 61613, padrão para STOMP)
    conn = stomp.Connection([('localhost', 61613)])
    conn.connect(wait=True)

    # Enviando a mensagem (imagem em Base64)
    conn.send(body=image_bytes, destination='/queue/imageQueue')
    
    print("Imagem enviada para a fila.")
    conn.disconnect()

def genQRCode(link):
    imagem_central = "../imgs/pd-logo.png"
    
    # Cria um QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(link)
    qr.make(fit=True)

    # Gera a imagem do QR Code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Abre e converte a imagem que será colocada no centro
    central_img = Image.open(imagem_central).convert("RGBA")
    
    # Calcula as dimensões para centralizar a imagem
    qr_width, qr_height = qr_img.size
    central_img = central_img.resize((int(qr_width / 4), int(qr_height / 4)))  # Ajusta o tamanho da imagem central
    central_x = (qr_width - central_img.width) // 2
    central_y = (qr_height - central_img.height) // 2

    # Coloca a imagem central no QR Code
    qr_img.paste(central_img, (central_x, central_y), central_img)  # Certifique-se de que a máscara de transparência está correta

    # Usando BytesIO para manter a imagem em memória
    buffer = BytesIO()
    qr_img.save(buffer, format="PNG")  # Salva a imagem no buffer
    buffer.seek(0)  # Move o cursor para o início do buffer
    image_bytes = base64.b64encode(buffer.getvalue()).decode('utf-8')  # Codifica a imagem em Base64

    # Chama a função send_image e passa a imagem codificada
    send_image(image_bytes)