# Planilhador Apostas Bet365

Este projeto utiliza a Google Cloud Vision API para extrair texto de imagens e processá-lo para obter informações específicas. Os dados extraídos são então armazenados em um arquivo Excel.

## Requisitos

- Python 3.6 ou superior
- Conta no Google Cloud com a Vision API habilitada
- Credenciais da Google Cloud salvas em um arquivo JSON (por exemplo, `credenciais_gcp.json`)

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/poliziinhaa/planilhador_apostas.git
    cd planilhador_apostas
    ```

2. Crie um ambiente virtual e ative-o:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install google-cloud-vision pandas openpyxl
    ```

4. Configure a variável de ambiente para as credenciais da Google Cloud:

    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="credenciais_gcp.json"
    ```

## Uso

1. Certifique-se de que a imagem de entrada está no diretório do projeto e ajuste o caminho da imagem no código se necessário:

    ```python
    image_path = 'caminho_imagem.png'
    ```

2. Execute o script:

    ```sh
    python planilhador_bet365.py
    ```

3. O script irá extrair o texto da imagem, processá-lo e salvar os dados em um arquivo Excel chamado `output.xlsx`. Se o arquivo já existir, os dados serão adicionados ao arquivo existente.


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
