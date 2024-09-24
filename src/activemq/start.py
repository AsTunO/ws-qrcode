import subprocess

def start_activemq():
    try:
        command = '/home/recepcao/Documents/WS/ws-qrcode/src/activemq/apache-activemq-6.1.3/bin/activemq start'
        subprocess.run(command, shell=True, check=True)
        print("ActiveMQ foi iniciado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar o ActiveMQ: {e}")

if __name__ == "__main__":
    start_activemq()
