import streamlit as st
import pandas as pd
import io
from openpyxl import Workbook
import base64
from PIL import Image

def download_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Controle_Finanças', index=False)
    processed_data = output.getvalue()
    return processed_data

def main():
    st.title('Controle de Finanças')

    data = {
        'Empreendimento': [],
        'Conta de Luz': [],
        'Água': [],
        'Internet': [],
        'Outras Despesas': [],
        'Entrada de Dinheiro': [],
        'Mês': []
    }

    months = ['Janeiro', 'Fevereiro', 'Março',
              'Abril', 'Maio', 'Junho', 'Julho',
              'Agosto', 'Setembro', 'Outubro',
              'Novembro', 'Dezembro']

    index = 0
    while True:
        casa = st.text_input(f'Nome do Empreendimento {index + 1}:')
        luz = st.number_input(f'Valor da Conta de Luz {index + 1}:')
        agua = st.number_input(f'Valor da Conta de Água {index + 1}:')
        internet = st.number_input(f'Valor da Conta de Internet {index + 1}:')
        
        outras_despesas = []
        despesa_index = 0
        more_expenses = True
        while more_expenses:
            despesa = st.number_input(f'Digite o valor de outra despesa {despesa_index + 1} do Empreendimento {index + 1} (ou 0 se não houver):')
            if despesa == 0:
                more_expenses = False
            else:
                outras_despesas.append(despesa)
                despesa_index += 1

        entrada = st.number_input(f'Valor da Entrada de Dinheiro {index + 1}:')
        mes = st.selectbox(f'Selecione o Mês {index + 1}:', months)

        data['Empreendimento'].append(casa)
        data['Conta de Luz'].append(luz)
        data['Água'].append(agua)
        data['Internet'].append(internet)
        data['Outras Despesas'].append(round(sum(outras_despesas), 2))
        data['Entrada de Dinheiro'].append(entrada)
        data['Mês'].append(mes)

        more_houses = st.checkbox(f'Adicionar outro Empreendimento?', key=f'checkbox_{index}')
        if not more_houses:
            break
        
        index += 1

    df = pd.DataFrame(data)

    st.write(df)

    lucro_total = round(df['Entrada de Dinheiro'].sum(), 2)
    despesas_totais = round(df[['Conta de Luz', 'Água', 'Internet', 'Outras Despesas']].sum().sum(), 2)
    lucro_liquido = round(lucro_total - despesas_totais, 2)

    st.write(f'Lucro Total: {lucro_total}')
    st.write(f'Despesas Totais: {despesas_totais}')
    st.write(f'Lucro Líquido: {lucro_liquido}')

    # Botão para download do Excel
    st.markdown("---")
    df_xlsx = download_excel(df)
    st.download_button(label='📥 Download tabela', 
                        data=df_xlsx, 
                        file_name='controle_financas.xlsx')
        
    st.markdown("---")
    st.text("Feito por Jeferson França")

if __name__ == '__main__':
    main()
