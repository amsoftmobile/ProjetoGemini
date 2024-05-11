## Analisando a Produção de Produtos com Google Generative AI\n\nEste código Python utiliza a API do Google Generative AI para calcular a quantidade de produtos finais que podem ser produzidos com base em um inventário de matérias-primas.\n\n**Funcionalidades:**\n\n* Recebe um JSON com informações sobre produtos finais e suas respectivas composições de matérias-primas.\n* Utiliza o modelo de linguagem \"gemini-1.5-pro-latest\" para processar o JSON e realizar cálculos.\n* Retorna um JSON indicando a quantidade máxima de cada produto final que pode ser produzida com base nas matérias-primas disponíveis.\n\n**Como o código funciona:**\n\n1. **Importação e Configuração:**\n   ```python\n   import google.generativeai as genai\n   genai.configure(api_key=\"SUA_API_KEY\") # Substitua 'SUA_API_KEY' pela sua chave real \n   ```\n   - Importa a biblioteca `google.generativeai`.\n   - Configura a chave da API.\n\n2. **Configurações de Geração e Segurança:**\n   ```python\n   generation_config = { \n       \"temperature\": 1, \n       \"top_p\": 0.95, \n       \"top_k\": 0, \n       \"max_output_tokens\": 81920, \n   }\n   safety_settings = [\n       {\"category\": \"HARM_CATEGORY_HARASSMENT\", \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"},\n       {\"category\": \"HARM_CATEGORY_HATE_SPEECH\", \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"},\n       {\"category\": \"HARM_CATEGORY_SEXUALLY_EXPLICIT\", \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"},\n       {\"category\": \"HARM_CATEGORY_DANGEROUS_CONTENT\", \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"},\n   ]\n   ```\n   - Define parâmetros para controlar a criatividade e o tamanho da resposta do modelo.\n   - Implementa filtros de segurança para evitar conteúdo prejudicial.\n\n3. **Criação do Modelo:**\n   ```python\n   model = genai.GenerativeModel(model_name=\"gemini-1.5-pro-latest\",\n       generation_config=generation_config, \n       safety_settings=safety_settings)\n   ```\n   - Cria uma instância do modelo \"gemini-1.5-pro-latest\".\n\n4. **Comunicação com o Modelo:**\n   ```python\n   chat = model.start_chat()\n   chat.send_message(\"\"\"faça o retorno em json\\nLevando em consideração produtos finais e materias primas, informe quais produtos finais posso fazer e quantos?\\n{ \n       \"produtos\": [\n           {\"codigo\": \"001\", \"descricao\": \"Hambúrguer de Carne 200g\", \"composicao\": [\"002\", \"003\", \"004\", \"005\"]},\n           {\"codigo\": \"002\", \"descricao\": \"Pão de Hambúrguer Brioche\", \"composicao\": [], \"quantia\": 4},\n           # ... (outros produtos) ...\n       ]\n   }\"\"\")\n   print(chat.last.text)\n   ```\n   - Inicia um chat com o modelo.\n   - Envia uma mensagem com instruções em português e um JSON descrevendo produtos e suas composições.\n   - Imprime a resposta do modelo, que deve conter um JSON indicando a quantidade produzível de cada produto final.\n\n**Observação:**\n\n* Substitua `\"SUA_API_KEY\"` pela sua chave real da API do Google Generative AI.\n* Adapte o JSON de entrada de acordo com os seus produtos e matérias-primas.\n\nEste código demonstra como usar o Google Generative AI para automatizar cálculos de produção, simplificando a gestão de estoque e planejamento de produção.
