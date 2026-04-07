import pandas as pd
import os

# Caminhos ajustados para a estrutura do seu projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Note que aqui usamos o nome do CSV que o seu coletor está gerando
CSV_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "data", "processed", "monitoramento_climatico.csv"))
LOG_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "..", "data", "processed", "alertas_climaticos.log"))


def analisar_clima_real():
    if not os.path.exists(CSV_PATH):
        print(f"❌ CSV não encontrado em: {CSV_PATH}")
        return

    try:
        # 1. Lê o CSV (Ajustado para o padrão do seu coletor: vírgula e nomes minúsculos)
        df = pd.read_csv(CSV_PATH, sep=',', encoding='utf-8') # Use vírgula aqui!
        
        if df.empty:
            print("⚠️ O arquivo CSV está vazio. Aguardando primeira coleta...")
            return

        ultima_leitura = df.iloc[-1]
        
        # AJUSTE DE COLUNAS: Usando os nomes que vêm do weather_api.py
        temp = float(ultima_leitura['temperatura'])
        data_hora = ultima_leitura['data']
        
        print(f"\n🌍 [MONITORAMENTO] Estação: Open-Meteo (Manaus)")
        print(f"🌡️ [DADO ATUAL] Temperatura: {temp}°C às {data_hora}")

        # 2. Tomada de Decisão
        status_alerta = "NORMAL"
        recomendacao = "Nenhuma ação necessária"

        if temp > 31.0:
            status_alerta = "ALERTA DE ONDA DE CALOR"
            recomendacao = "Notificar órgãos de saúde e Defesa Civil"
            print(f"⚠️ {status_alerta}: Risco de estresse térmico detectado!")
        else:
            print("✅ CONDIÇÕES ESTÁVEIS: Clima dentro da média esperada.")

        # 3. Grava o Log de Eventos
        with open(LOG_PATH, "a", encoding="utf-8") as log:
            log.write(f"{data_hora} - Temp: {temp}°C - Status: {status_alerta} - Recomendação: {recomendacao}\n")
        
        print(f"📝 Histórico atualizado em: {os.path.basename(LOG_PATH)}")

    except Exception as e:
        print(f"❌ Erro na análise: {e}")

if __name__ == "__main__":
    analisar_clima_real()