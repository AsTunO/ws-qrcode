from functions import genQRCode

def show():
    print("Interface temporária")
    print("1 - Gerar QR Code")
    option = int(input("Digite a sua opção: "))

    match option:
        case 1:
            link = str(input("Digite o link que deve ser gerado o QR Code: "))
            genQRCode(link)
        case _:
            print("Opção inválida")
