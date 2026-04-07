import pandas as pd
import os
from datetime import datetime

# 1. Configuração de Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Onde os dados processados devem morar
CAMINHO_PROCESSED = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "processed"))
os.makedirs(CAMINHO_PROCESSED, exist_ok=True)

def gerar_csv_climatico():
    print("📊 Iniciando processamento de dados para CSV...")
    
    # 2. Simulação de dados extraídos do seu PDF/Monitoramento
    # No futuro, aqui entrará a lógica do pdfplumber
    dados_climaticos = {
        "Data": [datetime.now().strftime("%d/%m/%Y %H:%M")],
        "Sensor": ["Estação Central - IFAM"],
        "Temperatura_C": [28.5],
        "Umidade_Relativa": [85],
        "Status_Alerta": ["Normal"]
    }

    # 3. Criando o DataFrame (Tabela do Pandas)
    df = pd.DataFrame(dados_climaticos)

    # 4. Caminho do arquivo final
    arquivo_csv = os.path.join(CAMINHO_PROCESSED, "monitoramento_climatico.csv")

    # 5. Salvando em CSV
    # 'mode=a' permite que o robô adicione novas linhas sem apagar as antigas
    # 'header' só é escrito se o arquivo ainda não existir
    file_exists = os.path.isfile(arquivo_csv)
    df.to_csv(arquivo_csv, mode='a', index=False, header=not file_exists, sep=';', encoding='utf-8-sig')

    print(f"✅ Dados armazenados com sucesso em: {arquivo_csv}")

if __name__ == "__main__":
    gerar_csv_climatico()