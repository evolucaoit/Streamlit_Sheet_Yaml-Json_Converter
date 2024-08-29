import streamlit as st
import pandas as pd
import yaml
import json
import io

# Função para processar o arquivo Excel
def process_excel(file):
    # Ler as abas do arquivo
    xls = pd.ExcelFile(file)
    sheet_names = xls.sheet_names
    
    # Criar um dicionário para armazenar os dados
    data = {}
    
    # Processar cada aba
    for sheet_name in sheet_names:
        df = pd.read_excel(file, sheet_name=sheet_name)
        # Converter colunas de datas para string
        for col in df.select_dtypes(include=['datetime64']).columns:
            df[col] = df[col].astype(str)
        data[sheet_name] = df.to_dict(orient='records')
    
    return data

# Função para salvar os dados em JSON e YAML
def save_files(data):
    json_files = []
    yaml_files = []
    
    for sheet_name, records in data.items():
        # Salvar JSON
        json_file = f"{sheet_name}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=4)
        json_files.append(json_file)
        
        # Salvar YAML
        yaml_file = f"{sheet_name}.yaml"
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.dump(records, f, allow_unicode=True)
        yaml_files.append(yaml_file)
    
    return json_files, yaml_files

# Interface do usuário com Streamlit
st.title("📊 Planilha para JSON/YAML Converter")

uploaded_file = st.file_uploader("📂 Arraste e solte sua planilha aqui", type=['xlsx'])

if uploaded_file:
    st.write("🔍 Processando a planilha...")
    
    data = process_excel(uploaded_file)
    json_files, yaml_files = save_files(data)
    
    st.write("✅ Arquivos gerados com sucesso!")
    
    st.write("📄 Arquivos JSON:")
    for json_file in json_files:
        st.markdown(f"- [{json_file}](./{json_file})")

    st.write("📄 Arquivos YAML:")
    for yaml_file in yaml_files:
        st.markdown(f"- [{yaml_file}](./{yaml_file})")

    st.balloons()
