import google.generativeai as genai

genai.configure(api_key="AIzaSyA16mT84EdvEnvAADJfKSDJIyna_31oReQ")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat()

convo.send_message("""faça o retorno em json\nLevando em consideração produtos finais e materias primas, informe quais produtos finais posso fazer e quantos?\n{
    "produtos": [
        {"codigo": "001", "descricao": "Hambúrguer de Carne 200g", "composicao": ["002", "003", "004", "005"]},
        {"codigo": "002", "descricao": "Pão de Hambúrguer Brioche", "composicao": [], "quantia": 4},
        {"codigo": "003", "descricao": "Fatia de Queijo Cheddar", "composicao": [], "quantia": 4},
        {"codigo": "004", "descricao": "Fatias de Bacon", "composicao": [], "quantia": 4},
        {"codigo": "005", "descricao": "Molho Especial", "composicao": ["006", "007"]},
        {"codigo": "006", "descricao": "Maionese Caseira", "composicao": [], "quantia": 3},
        {"codigo": "007", "descricao": "Ketchup Artesanal", "composicao": [], "quantia": 3},
        {"codigo": "008", "descricao": "Porção de Batatas Fritas", "composicao": [], "quantia": 1},
        {"codigo": "009", "descricao": "Anéis de Cebola", "composicao": [], "quantia": 1},
        {"codigo": "010", "descricao": "Refrigerante Lata 350ml", "composicao": [], "quantia": 1},
        {"codigo": "011", "descricao": "Milkshake de Chocolate 500ml", "composicao": [], "quantia": 1},
        {"codigo": "012", "descricao": "Salada para Hambúrguer (Alface, Tomate)", "composicao": [], "quantia": 1},
        {"codigo": "013", "descricao": "Picles em Conserva", "composicao": [], "quantia": 1},
        {"codigo": "014", "descricao": "Cebola Caramelizada", "composicao": [], "quantia": 1},
        {"codigo": "015", "descricao": "Molho Barbecue", "composicao": [], "quantia": 1},
        {"codigo": "016", "descricao": "Hambúrguer Vegetariano", "composicao": ["002", "003", "012"]},
        {"codigo": "017", "descricao": "Cerveja Artesanal 300ml", "composicao": [], "quantia": 1},
        {"codigo": "018", "descricao": "Sobremesa - Brownie de Chocolate", "composicao": [], "quantia": 1},
        {"codigo": "019", "descricao": "Café Expresso", "composicao": [], "quantia": 1},
        {"codigo": "020", "descricao": "Água Mineral Sem Gás 500ml", "composicao": [], "quantia": 1}
    ]
}, Note que o produto 5 e composto por 6 e 7 e só tem 3""")
print(convo.last.text)