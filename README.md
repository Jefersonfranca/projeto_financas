# Controle de Finanças com Streamlit

Este é um aplicativo simples desenvolvido em Python usando Streamlit para controle de finanças domésticas. O aplicativo permite que o usuário registre diversas despesas e entradas de dinheiro associadas a diferentes casas ao longo dos meses do ano.

## Funcionalidades

- Registro de despesas como Conta de Luz, Água, Internet e outras despesas diversas.
- Registro de entradas de dinheiro para cada casa.
- Seleção do mês associado aos registros.
- Visualização do lucro total, despesas totais e lucro líquido.

## Como Executar

1. **Instalação das Dependências:**
   - Certifique-se de ter o Python instalado no seu sistema. Recomenda-se utilizar um ambiente virtual para instalação das dependências.
   - Instale as dependências listadas no arquivo `requirements.txt` executando o comando:
     ```
     pip install -r requirements.txt
     ```

2. **Execução do Aplicativo:**
   - Execute o aplicativo usando o Streamlit. No terminal, navegue até o diretório onde está o código e execute o seguinte comando:
     ```
     streamlit run projeto_financa_streamlit.py
     ```
   - O aplicativo será iniciado e abrirá no navegador padrão.

3. **Utilização:**
   - Preencha os campos para cada casa com os valores de despesas e entradas de dinheiro correspondentes.
   - Selecione o mês associado aos registros de cada casa.
   - Clique em "Adicionar outra casa?" se precisar incluir mais de uma casa.
   - Os resultados de lucro total, despesas totais e lucro líquido serão calculados automaticamente e exibidos na interface.
   - Você pode fazer o download dos dados em formato Excel clicando no link fornecido.

4. **Contribuição:**
   - Sinta-se à vontade para enviar sugestões, relatar problemas ou contribuir com melhorias através de issues e pull requests neste repositório.

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Openpyxl

---

Esse projeto foi desenvolvido como um exemplo educacional para demonstrar a criação de uma aplicação simples de controle financeiro usando Streamlit. Sinta-se à vontade para adaptá-lo e expandi-lo conforme suas necessidades.
