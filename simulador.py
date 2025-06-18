import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Análise e Simulador de Desconto por Banco")

# 📁 Caminho do arquivo CSV (ajuste conforme necessário)
CAMINHO_ARQUIVO = "C:\\Users\\pablo paiva\\PROJETOS\\CÓDIGO\\testesimular2024 - RELATÓRIO ANUAL 2024  - Página1 (4).csv"

# 📄 Leitura do arquivo
df = pd.read_csv(CAMINHO_ARQUIVO)

# 🔧 Tratamento da coluna percentual
df['PERCENTUAL'] = df['PERCENTUAL'].str.replace('%', '').str.replace(',', '.').astype(float)

# ======= CALCULA MÉDIA (sem exibir gráfico) =======
media_por_banco = df.groupby('BANCO')['PERCENTUAL'].mean().sort_values(ascending=False)

st.divider()

# ======= SIMULADOR DE DESCONTO =======
st.subheader("✅ 📊 Simulador de Desconto")

with st.form("simulador_formulario"):
    saldo = st.number_input("Informe o saldo devedor (R$)", min_value=0.0, format="%.2f")
    bancos_disponiveis = df['BANCO'].dropna().astype(str).unique()
    banco_opcao = st.selectbox("Selecione o banco", sorted(bancos_disponiveis))
    simular = st.form_submit_button("Simular Desconto")

if simular:
    media_desconto = media_por_banco[banco_opcao]
    valor_desconto = saldo * (media_desconto / 100)
    valor_final = saldo - valor_desconto

    st.success(f"🏦 Banco selecionado: **{banco_opcao}**")
    st.info(f"📉 Desconto médio: **{media_desconto:.2f}%**")
    st.write(f"💸 Valor do desconto sugerido: `R$ {valor_desconto:,.2f}`")
    st.write(f"✅ Valor final com desconto: `R$ {valor_final:,.2f}`")
