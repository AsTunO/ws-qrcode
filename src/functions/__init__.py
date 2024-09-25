import qrcode
from PIL import Image

def genQRCode(link):
    imagem_central = "../imgs/pd-logo.png"
    caminho_saida = "qrcode.png"
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

    # Salva a imagem final
    qr_img.save(caminho_saida)
    print(f'QR Code salvo em {caminho_saida}')
