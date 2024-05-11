## Analisando a Produção de Produtos com Google Generative AI
Este código Python utiliza a API do Google Generative AI para calcular a quantidade de produtos finais que podem ser produzidos com base 
em um inventário de matérias-primas.
\*\*Funcionalidades:\*\*
\* Recebe um JSON com informações sobre produtos finais e suas respectivas composições de matérias-primas.
\* Utiliza o modelo de linguagem \"gemini-1.5-pro-latest\" para processar o JSON e realizar cálculos.
\* Retorna um JSON indicando a quantidade máxima de cada produto final que pode ser produzida com base nas matérias-primas disponíveis.

\*\*Como o código funciona:\*\*
1. \*\*Importação e Configuração:\*\*
```python   
   import google.generativeai as genai
   genai.configure(api\_key=\"SUA\_API\_KEY\") 
   # Substitua 'SUA\_API\_KEY' pela sua chave real \n   ```
- Importa a biblioteca `google.generativeai`.   
- Configura a chave da API.\n\n2. 

\*\*Configurações de Geração e Segurança:\*\*
```python\n   generation\_config = { 
       \"temperature\": 1, 
       \"top\_p\": 0.95, 
       \"top\_k\": 0, 
       \"max\_output\_tokens\": 81920, 
	   }\n   safety\_settings = [       {\"category\": \"HARM\_CATEGORY\_HARASSMENT\", \"threshold\": \"BLOCK\_MEDIUM\_AND\_ABOVE\"},
       {\"category\": \"HARM\_CATEGORY\_HATE\_SPEECH\", \"threshold\": \"BLOCK\_MEDIUM\_AND\_ABOVE\"},
	   {\"category\": \"HARM\_CATEGORY\_SEXUALLY\_EXPLICIT\", \"threshold\": \"BLOCK\_MEDIUM\_AND\_ABOVE\"},\n       {\"category\": \"HARM\_CATEGORY\_DANGEROUS\_CONTENT\", \"threshold\": \"BLOCK\_MEDIUM\_AND\_ABOVE\"},\n   ]\n   ```\n   - Define parâmetros para controlar a criatividade e o tamanho da resposta do modelo.\n   - Implementa filtros de segurança para evitar conteúdo prejudicial.\n\n3. \*\*Criação do Modelo:\*\*\n   ```python\n   model = genai.GenerativeModel(model\_name=\"gemini-1.5-pro-latest\",\n       generation\_config=generation\_config, \n       safety\_settings=safety\_settings)\n   ```\n   - Cria uma instância do modelo \"gemini-1.5-pro-latest\".\n\n4. \*\*Comunicação com o Modelo:\*\*\n   ```python\n   chat = model.start\_chat()\n   chat.send\_message(\"\"\"faça o retorno em json\\nLevando em consideração produtos finais e materias primas, informe quais produtos finais posso fazer e quantos?\\n{ \n       \"produtos\": [\n           {\"codigo\": \"001\", \"descricao\": \"Hambúrguer de Carne 200g\", \"composicao\": [\"002\", \"003\", \"004\", \"005\"]},\n           {\"codigo\": \"002\", \"descricao\": \"Pão de Hambúrguer Brioche\", \"composicao\": [], \"quantia\": 4},\n           # ... (outros produtos) ...\n       ]\n   }\"\"\")\n   print(chat.last.text)\n   ```\n   - Inicia um chat com o modelo.\n   - Envia uma mensagem com instruções em português e um JSON descrevendo produtos e suas composições.\n   - Imprime a resposta do modelo, que deve conter um JSON indicando a quantidade produzível de cada produto final.\n\n\*\*Observação:\*\*\n\n\* Substitua `\"SUA\_API\_KEY\"` pela sua chave real da API do Google Generative AI.\n\* Adapte o JSON de entrada de acordo com os seus produtos e matérias-primas.\n\nEste código demonstra como usar o Google Generative AI para automatizar cálculos de produção, simplificando a gestão de estoque e planejamento de produção.
