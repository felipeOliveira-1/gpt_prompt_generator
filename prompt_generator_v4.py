import openai
import sys

# Set the OpenAI API key
openai.api_key = "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"

def get_user_input():
    """Get user input for the desired option, prompt, role, and additional information."""
    option = input("Please choose an option:\n1. Simulate an expert\n2. Challenge the conventional narrative\n3. Write in different styles or tones, such as satire or irony\nEnter a number: ")

    if option == '1':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role_choice = input("\nPlease choose a role for GPT-3 to act as in the prompt:\n1. A teacher\n2. A scientist\n3. Enter your own role\nEnter a number: ")
    
        while role_choice not in ['1', '2', '3']:
            role_choice = input("Invalid role choice. Please enter a valid number or type your own role: ")
    
        if role_choice == '1':
            role = "a teacher"
        elif role_choice == '2':
            role = "a scientist"
        elif role_choice == '3':
            role = input("Please enter the role you want GPT-3 to act as in the prompt: ")
        
        additional_info = input("\nAny additional information or context to add to the prompt? ")  

    elif option == '2':
        topic = input("\nEnter a Topic: ")
        dominant_narrative = input("\nWhat is the dominant narrative? ")
        desired_prompt = f"For the topic about {topic}, give examples that contradict the dominant narrative that said {dominant_narrative}."
        role = "a thought-provoking writer"
        additional_info = ""

    elif option == '3':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        style_choice = input("\nPlease choose a style or tone:\n1. Satire\n2. Irony\n3. Enter your own style or tone\nEnter a number: ")
        
        while style_choice not in ['1', '2', '3']:
            style_choice = input("Invalid choice. Please enter a valid number or type your own style or tone: ")
        
        if style_choice == '1':
            style = "satire"
        elif style_choice == '2':
            style = "irony"
        elif style_choice == '3':
            style = input("Please enter the style or tone you want GPT-3 to use in the prompt: ")
        
        role = f"a {style} writer"
        additional_info = ""
    else:
        print("Invalid option selected.")
        return None

    prompt = f"Act as {role}. {desired_prompt}. {additional_info}."
    print("\nHere's an example of a prompt you could use:\n")
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
