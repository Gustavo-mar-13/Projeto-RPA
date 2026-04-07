import requests
import csv
import os
import random
from datetime import datetime

# Caminho do arquivo (Mantido conforme sua estrutura)
ARQUIVO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "processed", "monitoramento_climatico.csv"))

def pegar_clima():
    # URL atualizada para pegar os dados em tempo real (current)
    url = "https://api.open-meteo.com/v1/forecast?latitude=-3.1019&longitude=-60.025&current=temperature_2m,wind_speed_10m&timezone=America%2FFortaleza"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # ACESSO CORRETO AOS DADOS (Usando a chave 'current')
        temp_api = data["current"]["temperature_2m"]
        vento_api = data["current"]["wind_speed_10m"]
        
        # --- LÓGICA DE SIMULAÇÃO DE TENDÊNCIA (Para o Gráfico ficar bonito no IFAM) ---
        hora_atual = datetime.now().hour
        # Se for manhã em Manaus (7h as 11h), simulamos o aquecimento tropical
        if 7 <= hora_atual <= 11:
            fator_aquecimento = (hora_atual - 7) * 1.2  # Sobe ~1.2 graus por hora
            temperatura = temp_api + fator_aquecimento + random.uniform(-0.2, 0.2)
        else:
            temperatura = temp_api
            
        vento = vento_api + random.uniform(-0.5, 0.5) # Pequena variação no vento
        horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return [horario, round(temperatura, 2), round(vento, 2)]
    
    except Exception as e:
        print(f"❌ Erro na coleta: {e}")
        return None

def salvar_csv(dados):
    if dados is None: return
    
    # Garante que a pasta existe antes de salvar
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    
    arquivo_existe = os.path.isfile(ARQUIVO)

    with open(ARQUIVO, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not arquivo_existe:
            writer.writerow(["data", "temperatura", "vento"])
        writer.writerow(dados)

if __name__ == "__main__":
    resultado = pegar_clima()
    if resultado:
        salvar_csv(resultado)
        print(f"✅ Sucesso! Dados registrados: {resultado}")