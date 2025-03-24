import socket
from datetime import datetime
from colorama import Fore, init

# Inicializa o colorama
init(autoreset=True)

# Dicionário de portas relevantes com descrição e vulnerabilidade (se houver)
portas_relevantes = {
    20: {"serviço": "FTP (File Transfer Protocol)", "vulnerabilidade": "FTP não criptografado."},
    21: {"serviço": "FTP (File Transfer Protocol)", "vulnerabilidade": "FTP não criptografado."},
    22: {"serviço": "SSH (Secure Shell)", "vulnerabilidade": "Força bruta e falhas na configuração."},
    23: {"serviço": "Telnet", "vulnerabilidade": "Comunicacão sem criptografia, vulnerável a MITM."},
    25: {"serviço": "SMTP (Simple Mail Transfer Protocol)", "vulnerabilidade": "Risco de spammers."},
    53: {"serviço": "DNS (Domain Name System)", "vulnerabilidade": "Ataques DDoS, envenenamento de cache DNS."},
    80: {"serviço": "HTTP (HyperText Transfer Protocol)", "vulnerabilidade": "XSS, SQL Injection, CSRF."},
    443: {"serviço": "HTTPS (HTTP Secure)", "vulnerabilidade": "Ataques a SSL/TLS, falhas de configuração."},
    3306: {"serviço": "MySQL", "vulnerabilidade": "SQL Injection, configuração insegura."},
    3389: {"serviço": "RDP (Remote Desktop Protocol)", "vulnerabilidade": "Falhas no protocolo, ataques de força bruta."},
    445: {"serviço": "SMB (Server Message Block)", "vulnerabilidade": "Vulnerabilidade explorada pelo WannaCry."},
}

# Função para escanear as portas
def scan_port(ip, port):
    """Tenta conectar ao IP e verificar se a porta está aberta e fornece informações sobre o serviço"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP
        s.settimeout(1)  # Define um tempo limite para evitar travamento
        result = s.connect_ex((ip, port))  # Tenta conectar à porta
        s.close()  # Fecha a conexão após o teste
        
        if result == 0:  # Se a porta estiver aberta
            # Adicionar informações sobre a porta, se disponível
            if port in portas_relevantes:
                servico = portas_relevantes[port]["serviço"]
                vulnerabilidade = portas_relevantes[port]["vulnerabilidade"]
                print(Fore.GREEN + f"Porta {port} está aberta. Serviço: {servico}. Vulnerabilidade: {vulnerabilidade}")
            else:
                print(Fore.GREEN + f"Porta {port} está aberta, mas sem informações específicas.")
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao escanear {port}: {e}")
        return False

# Função para salvar os resultados em um arquivo
def save_results_to_file(ip, portas, resultados):
    with open("relatorio_scan.txt", "w") as file:
        file.write(f"Relatório de Escaneamento de Portas - IP: {ip}\n")
        file.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("="*50 + "\n")
        
        for port, status in resultados.items():
            if status:  # Se a porta está aberta
                file.write(f"Porta {port} está aberta.\n")
                # Adicionar descrição sobre a porta, se disponível
                if port in portas_relevantes:
                    servico = portas_relevantes[port]["serviço"]
                    vulnerabilidade = portas_relevantes[port]["vulnerabilidade"]
                    file.write(f"  Serviço: {servico}\n  Vulnerabilidade: {vulnerabilidade}\n")
                else:
                    file.write(f"  Serviço desconhecido.\n")
            else:  # Se a porta está fechada
                file.write(f"Porta {port} está fechada.\n")
        
        file.write("="*50 + "\n")
        file.write("Escaneamento finalizado.\n")

# Função principal para escanear portas e gerar relatório
def scanner_de_portas(ip, portas):
    print(f"Iniciando escaneamento no IP: {ip}")
    print(f"Escaneando as portas: {', '.join(map(str, portas))}")
    print("="*50)
    
    resultados = {}
    
    for port in portas:
        print(f"Escaneando a porta {port}...")
        resultado = scan_port(ip, port)
        resultados[port] = resultado
        print("="*50)

    # Salvar os resultados em um arquivo
    save_results_to_file(ip, portas, resultados)
    print(Fore.GREEN + "Relatório salvo com sucesso em 'relatorio_scan.txt'")

# Exemplo de uso
if __name__ == "__main__":
    ip_alvo = input("Digite o IP ou domínio para escanear: ")
    portas = list(map(int, input("Digite as portas a serem escaneadas (separadas por vírgula): ").split(",")))
    
    scanner_de_portas(ip_alvo, portas)
