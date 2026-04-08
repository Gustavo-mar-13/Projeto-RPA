# Este script tem duas funções principais:
# 1. Gerar um relatório consolidado em PDF a partir dos dados coletados e salvos em CSV.
# 2. Enviar esse relatório por e-mail usando o Gmail SMTP.

import pandas as pd
from fpdf import FPDF
import os

def gerar_relatorio_consolidado():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Caminhos dos seus arquivos
    csv_clima = "data/processed/monitoramento_clima.csv"
   
    
    arquivos = [
        {"nome": "Monitoramento de Clima (Tempo Real)", "path": csv_clima},
       
    ]

    for item in arquivos:
        if os.path.exists(item["path"]):
            df = pd.read_csv(item["path"])
            
            pdf.add_page()
            # Título da Seção
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, item["nome"], ln=True, align='C')
            pdf.ln(5)
            
            # Cabeçalho da Tabela
            pdf.set_font("Arial", 'B', 10)
            pdf.set_fill_color(200, 220, 255)
            
            # Ajustando largura das colunas
            col_width = pdf.epw / 3
            pdf.cell(col_width, 10, "Data/Hora", 1, 0, 'C', True)
            pdf.cell(col_width, 10, "Temperatura (°C)", 1, 0, 'C', True)
            pdf.cell(col_width, 10, "Condição/Status", 1, 1, 'C', True)
            
            # Dados (pegando os últimos 48 registros = 24 horas)
            pdf.set_font("Arial", size=9)
            for i, linha in df.tail(48).iterrows():
                # Juntamos Data e Hora que estão separadas no seu CSV
                data_formatada = f"{linha.get('Data', 'N/A')} {linha.get('Hora', '')}"
                
                # Pegamos a Temperatura e a Condição (ou Status)
                temp = f"{linha.get('Temperatura', '0')}°C"
                info_extra = f"{linha.get('Condicao', linha.get('Status', 'N/A'))}"

                # Criando as células com os nomes exatos das suas colunas
                pdf.cell(col_width, 8, data_formatada, 1)
                pdf.cell(col_width, 8, temp, 1, 0, 'C')
                pdf.cell(col_width, 8, info_extra, 1, 1, 'C')
        else:
            print(f"⚠️ Aviso: Arquivo {item['path']} não encontrado.")

    # Garante que a pasta existe antes de salvar
    os.makedirs("data/processed", exist_ok=True)
    
    output_path = "data/processed/Relatorio_Final_RPA.pdf"
    pdf.output(output_path)
    print(f"✅ Relatório PDF gerado com sucesso em: {output_path}")
    return output_path

if __name__ == "__main__":
    gerar_relatorio_consolidado()




# --- CONFIGURAÇÕES DE ENVIO PELO EMAIL ---


import smtplib
from email.message import EmailMessage
import os

# --- CONFIGURAÇÕES DE ENVIO ---
#bem alto explicativo 

MEU_EMAIL = "gustavomarluz@gmail.com"
MINHA_KEY = "altz iswt hrfw kars"  # 


# Esta função é responsável por enviar o relatório PDF gerado para o seu e-mail 
def enviar_por_email(caminho_arquivo):
    print(f"📧 Iniciando envio do e-mail para {MEU_EMAIL}...")
    
    if not os.path.exists(caminho_arquivo):
        print("❌ Erro: O arquivo PDF não foi encontrado para envio.")
        return

    # Criando a estrutura do e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Relatório de Monitoramento de Clima - RPA'
    msg['From'] = MEU_EMAIL
    msg['To'] = MEU_EMAIL # Enviando para você mesmo
    msg.set_content("Olá Gustavo,\n\nO robô RPA finalizou a coleta e gerou o relatório de clima em tempo real.\n\nSegue o arquivo em anexo.")

    # Anexando o PDF
    try:
        with open(caminho_arquivo, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(
                file_data, 
                maintype='application', 
                subtype='pdf', 
                filename='Relatorio_Clima_RPA.pdf'
            )

        # Conectando ao servidor do Gmail (SMTP)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MEU_EMAIL, MINHA_KEY)
            smtp.send_message(msg)
            
        print("🚀 Relatório enviado com sucesso para o seu e-mail!")
        
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

# --- INTEGRANDO NO MAIN ---
if __name__ == "__main__":
    # 1. Gera o PDF e guarda o caminho onde ele foi salvo
    caminho_do_pdf = gerar_relatorio_consolidado()
    
    # 2. Se o PDF foi gerado com sucesso, envia por e-mail
    if caminho_do_pdf:
        enviar_por_email(caminho_do_pdf)


