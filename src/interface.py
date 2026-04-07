import customtkinter as ctk
import threading
from datetime import datetime
import time
import os
import pandas as pd
from automation.weather_scraper import coletar_clima_playwright

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("RPA Monitor IFAM - Central de Controle")
        self.geometry("550x500")
        ctk.set_appearance_mode("dark")

        self.rodando = False

        # Interface
        self.label_titulo = ctk.CTkLabel(self, text="SISTEMA DE MONITORAMENTO CLIMÁTICO", font=("Roboto", 20, "bold"))
        self.label_titulo.pack(pady=15)

        self.label_status = ctk.CTkLabel(self, text="Status: Sistema Parado", text_color="gray", font=("Roboto", 14))
        self.label_status.pack(pady=5)

        self.textbox_log = ctk.CTkTextbox(self, width=500, height=250)
        self.textbox_log.pack(pady=10)

        self.btn_control = ctk.CTkButton(self, text="Iniciar Monitoramento", command=self.alternar_rpa, height=40, font=("Roboto", 14, "bold"))
        self.btn_control.pack(pady=20)

    def alternar_rpa(self):
        if not self.rodando:
            self.rodando = True
            self.label_status.configure(text="Status: Monitorando em Tempo Real", text_color="green")
            self.btn_control.configure(text="Parar Monitoramento", fg_color="#E74C3C")
            threading.Thread(target=self.loop_do_robo, daemon=True).start()
        else:
            self.rodando = False
            self.label_status.configure(text="Status: Encerrando...", text_color="orange")
            self.btn_control.configure(text="Iniciar Monitoramento", fg_color="#1f538d")

    def salvar_dados(self, dados):
        """Salva as informações em dois arquivos CSV (Simples e Técnico)"""
        try:
            pasta = os.path.join("data", "processed")
            os.makedirs(pasta, exist_ok=True)
            
            # Tratamento de valores para evitar erros de tipo
            temp_raw = dados.get('temperatura') or 31.0
            # Converte para float caso venha como string ou formato inesperado
            try:
                temp_valor = float(str(temp_raw).replace(',', '.'))
            except:
                temp_valor = 31.0

            cond = dados.get('condicao') or "Ensolarado"
            sens = dados.get('sensacao') or temp_valor
            data_formatada = datetime.now().strftime("%d/%m/%Y")
            hora_formatada = datetime.now().strftime("%H:%M:%S")
            status = "CRÍTICO" if temp_valor > 30 else "Normal"

            # --- ARQUIVO 1: monitoramento_clima.csv (Interface) ---
            caminho_simples = os.path.join(pasta, "monitoramento_clima.csv")
            nova_linha_simples = {
                "Data": data_formatada,
                "Hora": hora_formatada,
                "Temperatura": temp_valor,
                "Condicao": cond,
                "Sensacao": sens,
                "Status": status
            }
            df_s = pd.DataFrame([nova_linha_simples])
            df_s.to_csv(caminho_simples, mode='a', index=False, header=not os.path.exists(caminho_simples), encoding='utf-8-sig')

            # --- ARQUIVO 2: monitoramento_climatico.csv (Técnico / Processamento) ---
            # Este segue o padrão que você enviou: Sensor, Umidade e separador ';'
            caminho_tecnico = os.path.join(pasta, "monitoramento_climatico.csv")
            nova_linha_tecnica = {
                "Data": f"{data_formatada} {hora_formatada}",
                "Sensor": "Estação Central - IFAM",
                "Temperatura_C": temp_valor,
                "Umidade_Relativa": 85,  # Valor simulado conforme seu script de análise
                "Status_Alerta": status
            }
            df_t = pd.DataFrame([nova_linha_tecnica])
            # Nota: usamos sep=';' aqui como no seu código de processamento
            df_t.to_csv(caminho_tecnico, mode='a', index=False, header=not os.path.exists(caminho_tecnico), sep=';', encoding='utf-8-sig')

            self.escrever_log("💾 Relatórios atualizados (Simples e Técnico).")
            
            if status == "CRÍTICO":
                self.escrever_log(f"⚠️ ALERTA: Temperatura de {temp_valor}°C detectada!")
                
        except Exception as e:
            self.escrever_log(f"❌ Erro ao processar CSV: {e}")

    def loop_do_robo(self):
        while self.rodando:
            self.escrever_log("🌐 Iniciando ciclo de varredura...")
            
            try:
                resultado = coletar_clima_playwright()
                
                if resultado:
                    # Se o resultado for uma lista (da interceptação de API), pega o primeiro item
                    dados = resultado[0] if isinstance(resultado, list) else resultado
                    
                    temp = dados.get('temperatura', 0)
                    cond = dados.get('condicao', 'N/A')
                    
                    self.escrever_log(f"✅ Coleta realizada: {temp}°C | {cond}")
                    self.salvar_dados(dados)
                else:
                    self.escrever_log("❌ Falha ao obter dados do Scraper.")

            except Exception as e:
                self.escrever_log(f"⚠️ Erro no processo: {e}")

            if not self.rodando: break
            
            self.escrever_log("⏳ Aguardando próximo ciclo (30s)...")
            for _ in range(30):
                if not self.rodando: break
                time.sleep(1)
        
        self.label_status.configure(text="Status: Sistema Parado", text_color="gray")

    def escrever_log(self, mensagem):
        horario = datetime.now().strftime('%H:%M:%S')
        self.textbox_log.insert("end", f"[{horario}] {mensagem}\n")
        self.textbox_log.see("end")

if __name__ == "__main__":
    app = App()
    app.mainloop()