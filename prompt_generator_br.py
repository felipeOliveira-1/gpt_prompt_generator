import openai
import sys

# Set the OpenAI API key
openai.api_key = ""

def get_user_input():
    """Obtenha entrada do usuário para a opção desejada, prompt, função e informações adicionais."""
    option = input("Escolha uma opção:\n1. Simule um especialista\n2. Desafie a narrativa convencional\n3. Use prompts não convencionais\n4. Ultra-Brainstormer\n5. Adicione técnicas de escrita humana\n6. Escreva de diferentes perspectivas\n7. Escreva em estilos ou tons diferentes, como sátira ou ironia\nDigite um número: ")

    if option == '1':
        desired_prompt = input("\nPor favor, digite o prompt que você deseja que o GPT-3 responda: ")
        role_choice = input("\nPor favor, escolha um modelo para GPT-3 para atuação dele no prompt:\n1. Um professor\n2. Um cientista\n3. Um artista\n4. Um empresário\n5. Um jornalista\n6. Insira sua própria função\n Digite um número: ")
    
        while role_choice not in ['1', '2', '3', '4', '5', '6']:
            role_choice = input("Escolha de função inválida. Insira um número válido ou digite sua própria função: ")
    
        if role_choice == '1':
            role = "um professor"
        elif role_choice == '2':
            role = "um cientista"
        elif role_choice == '3':
            role = "um artista"
        elif role_choice == '4':
            role = "um empreendedor"
        elif role_choice == '5':
            role = "um jornalista"
        elif role_choice == '6':
            role = input("Insira a função que deseja que o GPT-3 utilize no prompt: ")
        
        additional_info = input("\nAlguma informação ou contexto adicional para adicionar ao prompt?\n")

    

    elif option == '2':
        topic = input("\nDigite um tópico: ")
        dominant_narrative = input("\nQual é a narrativa dominante?")
        desired_prompt = f"Em relação ao tópico {topic}, forneça exemplos que refute a narrativa dominante que diz {dominant_narrative}."
        role = "um escritor instigante"
        additional_info = ""

    elif option == '3':
        prompt_type = input("\nPor favor escolha um tipo não convencional de prompt:\n1. Escrita criativa\n2. Filosófica\n3. Detetive/misterioso\nDigite um número: ")
        desired_prompt = input("\nPor favor, digite o prompt que você deseja que o GPT-3 responda: ")
        if prompt_type == '1':
            role = "um escritor criativo"
        elif prompt_type == '2':
            role = "um filósofo"
        elif prompt_type == '3':
            role = "Sherlock Holmes"
        additional_info = input("\nAlguma informação ou contexto adicional para adicionar ao prompt?")

    elif option == '4':
        desired_prompt = input("\nPor favor, digite o prompt que você deseja que o GPT-3 responda: ")
        role = "um gerador de ideias"
        additional_info = input("\nAlguma informação ou contexto adicional para adicionar ao prompt? ")

    elif option == '5':
        desired_prompt = input("\nPor favor, digite o prompt que você deseja que o GPT-3 responda: ")
        role = "um escritor persuasivo"
        additional_info = input("\nAlguma informação ou contexto adicional para adicionar ao prompt? ")

    elif option == '6':
        desired_prompt = input("\nPor favor, digite o prompt que você deseja que o GPT-3 responda: ")
        role = "um grupo de personagens com origens ou pontos de vista diferentes"
        additional_info = input("\nPor favor, forneça informações sobre as diferentes perspectivas que você deseja incluir: ")

    elif option == '7':
        desired_prompt = input("\nPor favor, digite o prompt que você deseja que o GPT-3 responda: ")
        style_choice = input("\nEscolha um estilo ou tom:\n1. Sátira\n2. Ironia\n3. Digite seu próprio estilo ou tom\nDigite um número: ")
        
        while style_choice not in ['1', '2', '3']:
            style_choice = input("Escolha inválida. Insira um número válido ou digite seu próprio estilo ou tom: ")
        
        if style_choice == '1':
            style = "satira"
        elif style_choice == '2':
            style = "ironia"
        elif style_choice == '3':
            style = input("Digite o estilo ou tom que deseja que o GPT-3 use no prompt: ")
        
        role = f"de forma {style}"
        additional_info = ""

    else:
        print("Opção inválida selecionada.")
        return None

    return option, desired_prompt, role, additional_info



def generate_response(prompt):
    """Generate a response from the GPT-3 API given a prompt."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n", ".", "!", "?"]
        )
        generated_prompt = response.choices[0].text.strip()
    except Exception as e:
        print("Error:", e)
        generated_prompt = ""
    return generated_prompt


def generate_prompt():
    option, desired_prompt, role, additional_info = get_user_input()

    prompt = f"Aja como {role}. {desired_prompt}. {additional_info}."
    print("Aqui está um exemplo de prompt que você pode usar:\n")
    print(prompt)

    generated_prompt = generate_response(prompt)
    return generated_prompt


# Call the generate_prompt() function and print the generated prompt
print(generate_prompt())
