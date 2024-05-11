
# Análise de Produção de Produtos com Google Generative AI

## Funcionalidades
- Recebe um JSON com informações sobre produtos finais e suas respectivas composições de matérias-primas.
- Utiliza o modelo "gemini-1.5-pro-latest" para processar o JSON e realizar cálculos.
- Retorna um JSON indicando a quantidade máxima de cada produto final que pode ser produzida.

## Código

### Importação e Configuração
```python
import google.generativeai as genai
genai.configure(api_key="SUA_API_KEY")  # Substitua 'SUA_API_KEY' pela sua chave real
```

### Configurações de Geração e Segurança
```python
generation_config = { 
    "temperature": 1, 
    "top_p": 0.95, 
    "top_k": 0, 
    "max_output_tokens": 81920, 
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
```

### Criação do Modelo
```python
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
    generation_config=generation_config, 
    safety_settings=safety_settings)
```

### Comunicação com o Modelo
```python
chat = model.start_chat()
chat.send_message("faça o retorno em json\nLevando em consideração produtos finais e materias primas, informe quais produtos finais posso fazer e quantos?\n{ 'produtos': [{'codigo': '001', 'descricao': 'Hambúrguer de Carne 200g', 'composicao': ['002', '003', '004', '005']},{'codigo': '002', 'descricao': 'Pão de Hambúrguer Brioche', 'composicao': [], 'quantia': 4}]}")
print(chat.last.text)
```

## Observação
- Substitua "SUA_API_KEY" pela sua chave real da API do Google Generative AI.
- Adapte o JSON de entrada de acordo com os seus produtos e matérias-primas.
