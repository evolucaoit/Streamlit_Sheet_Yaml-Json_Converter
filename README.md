# 📊 Streamlit Sheet YAML/JSON Converter

Bem-vindo ao **Streamlit Sheet YAML/JSON Converter**! Este projeto é uma ferramenta poderosa desenvolvida para **converter planilhas Excel em arquivos JSON e YAML** utilizando **Python** e **Streamlit**. É uma demonstração do meu conhecimento técnico e habilidades em manipulação de dados, programação e desenvolvimento de interfaces interativas. 🚀

## 📜 Sobre o Projeto

O objetivo deste projeto é fornecer uma solução eficiente para a conversão de dados armazenados em planilhas Excel para formatos de arquivo JSON e YAML. Utilizando bibliotecas robustas como `pandas`, `yaml`, e `json`, junto com uma interface interativa criada com `Streamlit`, este projeto exemplifica minha capacidade de transformar dados de forma prática e visual. 🌟
### 📸 Exemplos Visuais

- **Interface do Aplicativo**:
  ![Interface do Aplicativo](https://github.com/evolucaoit/Streamlit_Sheet_Yaml-Json_Converter/blob/main/xczvL1dVg9.png?raw=true)

- **Exemplo de Planilhas**:
  - [Planilha de Estoque - Transportadora](https://github.com/evolucaoit/Streamlit_Sheet_Yaml-Json_Converter/blob/main/estoque_transportadora.xlsx)
  - [Planilha de Estoque - Empresas](https://github.com/evolucaoit/Streamlit_Sheet_Yaml-Json_Converter/blob/main/estoque_empresas.xlsx)

- **Código do Projeto**:
  - [Código do Conversor](https://github.com/evolucaoit/Streamlit_Sheet_Yaml-Json_Converter/blob/main/analisa-planilha-gera-yaml.py)


### 🎯 Propósito do Projeto

Este conversor é ideal para:

- **💡 Transformar Dados**: Converter dados de planilhas para JSON e YAML, facilitando a integração com diferentes sistemas e a manipulação de dados.
- **🔍 Análise e Visualização**: Visualizar dados de forma interativa através de uma interface gráfica intuitiva, tornando o processo mais acessível e eficiente.
- **🚀 Aplicações Práticas**: Utilizar em projetos onde é necessário converter e gerenciar dados de maneira estruturada e organizada.

## 🛠️ Funcionalidades

- **📂 Upload de Arquivo**: Interface para upload de planilhas Excel (.xlsx).
- **🔍 Processamento de Dados**: Leitura de abas da planilha e conversão de colunas de datas para strings.
- **💾 Exportação**: Salva dados em arquivos JSON e YAML.
- **🎈 Interface Interativa**: Interface gráfica com Streamlit para visualização dos arquivos gerados.

## 🗂️ Como Usar

### 🔧 Requisitos

Certifique-se de ter o seguinte instalado:

- Python 3.x
- Streamlit
- pandas
- PyYAML

Você pode instalar as dependências necessárias usando:

```bash
pip install streamlit pandas pyyaml

📄 Exemplos de Dados

```
Exemplo de Dados YAML

```yaml
- Categoria: Peças
  Data de Validade: '2026-11-06'
  Descrição: per
  Filial: Filial 10
  ID: 131758fd-1ab8-4186-99a8-ab8a03ff6809
  Preço Unitário: 158.78
  Quantidade: 150
- Categoria: Peças
  Data de Validade: '2029-02-20'
  Descrição: open
  Filial: Filial 10
  ID: acd51b0b-bd26-4b84-b04d-3096c18347f1
  Preço Unitário: 1477.2
  Quantidade: 92

```

```json
[
    {
        "ID": "131758fd-1ab8-4186-99a8-ab8a03ff6809",
        "Descrição": "per",
        "Categoria": "Peças",
        "Quantidade": 150,
        "Preço Unitário": 158.78,
        "Data de Validade": "2026-11-06",
        "Filial": "Filial 10"
    },
    {
        "ID": "acd51b0b-bd26-4b84-b04d-3096c18347f1",
        "Descrição": "open",
        "Categoria": "Peças",
        "Quantidade": 92,
        "Preço Unitário": 1477.2,
        "Data de Validade": "2029-02-20",
        "Filial": "Filial 10"
    }
]


```
🚀 Sobre o Autor
Olá, sou Elias Andrade! Sou um profissional com mais de 14 anos de experiência em infraestrutura de TI, automação e análise de dados. Este projeto é uma demonstração da minha capacidade de criar soluções técnicas inovadoras e práticas. 🔧💻

🌟 Minha Jornada
🔍 Conhecimento Técnico: Aprofundamento em Python, manipulação de dados e desenvolvimento de interfaces.
📚 Aprendizado Contínuo: Comprometido com a melhoria constante e a aplicação de novas técnicas.
💡 Soluções Práticas: Criação de ferramentas que facilitam a transformação e análise de dados complexos.
Para mais detalhes sobre meu trabalho e experiências, visite meu GitHub e conecte-se comigo no LinkedIn. 🌟
