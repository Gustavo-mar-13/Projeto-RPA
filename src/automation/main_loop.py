import sys
import os
import time
from datetime import datetime

# --- CONFIGURAÇÃO DE CAMINHOS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
SRC_DIR = os.path.dirname(BASE_DIR) 

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
# -------------------------------

# Importando as funções com os nomes corretos do seu arquivo
from data_collection.weather_api import pegar_clima, salvar_csv
from analysis.analyze_data import analisar_clima_real

def monitoramento_completo():
    print("\n" + "="*40)
    print("🌙 [SISTEMA IFAM] MODO NOTURNO ATIVADO")
    print("="*40)

    while True:
        try:
            agora = datetime.now().strftime('%H:%M:%S')
            print(f"\n🔔 [CICLO] Iniciando coleta das {agora}...")

            # 1. PEGA OS DADOS DA API
            dados_novos = pegar_clima()
            
            # 2. SALVA NO CSV
            salvar_csv(dados_novos)
            print(f"📊 Dados salvos no CSV: {dados_novos}")
            
            # 3. ANALISA (Gera o Log)
            analisar_clima_real()

            print(f"✅ Ciclo concluído com sucesso às {agora}.")
            
            # TESTE: 10 | PRODUÇÃO: 3600
            time.sleep(10) 

        except KeyboardInterrupt:
            print("\n🛑 Robô parado pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro no loop: {e}")
            time.sleep(300)

if __name__ == "__main__":
    monitoramento_completo()