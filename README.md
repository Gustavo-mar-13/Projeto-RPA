# 🤖 RPA - Monitoramento Climático Automatizado

## 📌 Sobre o Projeto

Automação (RPA) desenvolvida em Python para coletar, processar e reportar dados climáticos de Manaus em tempo real.

O sistema intercepta a API interna do MSN Clima via Playwright, processa os dados, salva em CSV e gera relatórios em PDF enviados automaticamente por e-mail.

---

## 🚀 Funcionalidades

- 🌐 Interceptação da API do MSN Clima via Playwright
- 🖥️ Interface gráfica para controle do robô (dark mode)
- 💾 Salvamento automático em CSV a cada ciclo
- ⚠️ Classificação automática de alertas (CRÍTICO / Normal)
- 📄 Geração de relatório PDF com as últimas 24h de dados
- 📧 Envio automático do relatório por e-mail via Gmail SMTP

---

## 🧠 Como o sistema funciona
Usuário clica "Iniciar"
↓
interface.py inicia loop em thread separada
↓
weather_scraper.py abre Chromium e intercepta API do MSN
↓
Retorna → { temperatura, condicao, sensacao }
↓
interface.py classifica e salva em 2 CSVs
↓
pdf_email.py gera PDF e envia pro e-mail (execução manual)


---

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Playwright
- CustomTkinter
- Pandas
- fpdf
- smtplib

---

## 📁 Estrutura do Projeto

Projeto-RPA/
├── src/
│   └── automation/
│       └── data_collection/
│           └── weather_scraper.py  # Motor de coleta via Playwright
├── interface.py                    # Interface gráfica + orquestrador
├── pdf_email.py                    # Geração de PDF + envio por e-mail
├── requirements.txt
└── README.md

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Gustavo-mar-13/Projeto-RPA.git
cd Projeto-RPA
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Execute o sistema

```bash
python interface.py
```

### 5. Para gerar e enviar o relatório

```bash
python pdf_email.py
```

---

## 📊 Possíveis aplicações

- Monitoramento climático automatizado
- Alertas de temperatura em ambientes críticos
- Base para sistemas de análise de dados em tempo real
- Automação de tarefas repetitivas (RPA)

---

## 🔮 Melhorias futuras

- Dashboard visual em tempo real
- Integração com banco de dados
- Agendamento automático via cron job
- Coleta de umidade real (atualmente simulada)
- Deploy em ambiente cloud

---

## 👨‍💻 Autor

Desenvolvido por **Gustavo Martins Luz**

---

## 📌 Observações

Projeto desenvolvido com foco em aprendizado prático de:

- Automação (RPA)
- Web scraping com interceptação de API
- Interface gráfica com Python
- Geração de relatórios e notificações automáticas

---

## 💡 Consideração final

Este projeto representa um **fluxo RPA completo e funcional** — da coleta automática de dados até a entrega do relatório no e-mail, sem intervenção humana após o início.