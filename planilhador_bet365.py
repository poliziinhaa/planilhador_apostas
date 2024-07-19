import os
import io
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'arquivo_json_credenciais_GCP'

def extract_text_from_image(image_path):
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if response.error.message:
        raise Exception(f'API Error: {response.error.message}')
    return texts[0].description if texts else ""

def parse_extracted_text(text):
    lines = text.split('\n')
    jogo = next((line for line in lines if 'v' in line), "Jogo Desconhecido")
    valor_apostado = next((line for line in lines if 'R$' in line and 'R$' in line.split()[0]), "R$0,00").split()[0]
    odd = lines[-1] if lines[-1].replace('.', '', 1).isdigit() else "1.00"
    retorno_obtido = lines[lines.index("Retorno Líquido") + 1] if "Retorno Líquido" in lines else "R$0,00"
    
    return {
        "Jogo": jogo,
        "Aposta": lines[1],
        "Valor Apostado": valor_apostado,
        "Odd": odd,
        "Retorno Obtido": retorno_obtido
    }

def add_to_dataframe(data, df_path='output.xlsx'):
    df_new = pd.DataFrame([data])
    if os.path.exists(df_path):
        df = pd.read_excel(df_path)
        # Verifica se os dados já existem no DataFrame
        if not df[(df['Jogo'] == data['Jogo']) & (df['Aposta'] == data['Aposta']) & 
                  (df['Valor Apostado'] == data['Valor Apostado']) & (df['Odd'] == data['Odd']) & 
                  (df['Retorno Obtido'] == data['Retorno Obtido'])].empty:
            print("Dados já existentes. Não adicionando ao DataFrame.")
            return df
        df = pd.concat([df, df_new], ignore_index=True)
    else:
        df = df_new
    df['P/L'] = df.apply(lambda row: float(row['Retorno Obtido'].replace('R$', '').replace(',', '.')) -
                                         float(row['Valor Apostado'].replace('R$', '').replace(',', '.')), axis=1)
    df.to_excel(df_path, index=False)
    return df

image_path = 'Screenshot_1.png'
extracted_text = extract_text_from_image(image_path)
data = parse_extracted_text(extracted_text)
df = add_to_dataframe(data)

print(df)