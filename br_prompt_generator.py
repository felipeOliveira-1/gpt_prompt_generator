import openai
import sys

# Set the OpenAI API key
openai.api_key = ""

def get_user_input():
    """Obtenha entrada do usuário para a opção desejada, prompt, função e informações adicionais."""
    option = input("Escolha uma opção:\n1. Simule um especialista\n2. Desafie a narrativa convencional\n3. Escreva em estilos ou tons diferentes, como sátira ou ironia\nDigite um número: ")

    if option == '1':
        desired_prompt = input("\nPor favor, digite o prompt que você deseja que o GPT-3 responda: ")
        role_choice = input("\Por favor, escolha uma função para GPT-3 para atuar como no prompt:\n1. Um professor\n2. Um cientista\n3. Digite sua própria função\nDigite um número: ")
    
        while role_choice not in ['1', '2', '3']:
            role_choice = input("Escolha de função inválida. Insira um número válido ou digite sua própria função: ")
    
        if role_choice == '1':
            role = "um professor"
        elif role_choice == '2':
            role = "um cientista"
        elif role_choice == '3':
            role = input("Insira a função que você deseja que o GPT-3 aja no prompt: ")
        
        additional_info = input("\nAlguma informação ou contexto adicional para adicionar ao prompt?")  

    elif option == '2':
        topic = input("\nDigite um tópico: ")
        dominant_narrative = input("\Qual é a narrativa dominante?")
        desired_prompt = f"Para o tópico sobre {topic}, dê exemplos que contradizem a narrativa dominante que diz {dominant_narrative}."
        role = "um escritor instigante"
        additional_info = ""

    elif option == '3':
        desired_prompt = input("\nPor favor, digite o prompt que deseja que o GPT-3 responda:")
        style_choice = input("\nPor favor, escolha um estilo ou tom:\n1. Sátira\n2. Ironia\n3. Digite seu próprio estilo ou tom\Digite um número: ")
        
        while style_choice not in ['1', '2', '3']:
            style_choice = input("Escolha inválida. Digite um número válido ou digite seu próprio estilo ou tom: ")
        
        if style_choice == '1':
            style = "satirico"
        elif style_choice == '2':
            style = "ironico"
        elif style_choice == '3':
            style = input("Insira o estilo ou tom que deseja que o GPT-3 use no prompt: ")
        
        role = f"um escritor {style}"
        additional_info = ""
    else:
        print("Opção inválida selecionada.")
        return None

    prompt = f"Aja como {role}. {desired_prompt}. {additional_info}."
    print("\nAqui está um exemplo de prompt que você pode usar:\n")
    print(prompt)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
)

    print(response.choices[0].text)
       
get_user_input()
