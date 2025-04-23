## Scanner de Portas em Python

Este projeto é um **Scanner de Portas** simples em Python, que possibilita a identificação de portas abertas em um endereço IP e gera um relatório com o status das portas. O relatório inclui informações adicionais sobre as portas mais relevantes e as vulnerabilidades associadas a elas, proporcionando uma visão sobre a segurança de sistemas e redes.

## 🛠 Funcionalidades

- Entrada de endereço IP ou hostname.
- Verificação de portas entre 1 e 1024 (padrão).
- Exibição de portas abertas.
- Tratamento de exceções (ex: host inválido ou inacessível).

##  Tecnologias

- Python 3.x
- Módulo `socket`
- Módulo `datetime`

## Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/brazbruna/scanner-de-portas.git
cd scanner-de-portas

2. Instale as dependências:

pip install colorama

## 3. Execute o script:

bash
Copiar
Editar
python scanner.py

### 4. Exemplo de Saída:

Digite o IP ou domínio para escanear: localhost
Digite as portas a serem escaneadas (separadas por vírgula): 80 , 20, 55
Iniciando escaneamento no IP: localhost
Escaneando as portas: 80, 20, 55
==================================================
Escaneando a porta 80...
==================================================
Escaneando a porta 20...
==================================================
Escaneando a porta 55...
==================================================
Relatório salvo com sucesso em 'relatorio_scan.txt'

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Veja o arquivo `LICENSE` para mais detalhes.
