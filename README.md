# Análise de Produção de Produtos com Google Generative AI

Este código Python utiliza a API do Google Generative AI para calcular a quantidade de produtos finais que podem ser produzidos com base em um inventário de matérias-primas.

## Funcionalidades

- Recebe um JSON com informações sobre produtos finais e suas respectivas composições de matérias-primas.
- Utiliza o modelo de linguagem "gemini-1.5-pro-latest" para processar o JSON e realizar cálculos.
- Retorna um JSON indicando a quantidade máxima de cada produto final que pode ser produzida com base nas matérias-primas disponíveis.

## Como o Código Funciona

### Importação e Configuração

```python
import google.generativeai as genai
genai.configure(api_key="SUA_API_KEY")  # Substitua 'SUA_API_KEY' pela sua chave real
