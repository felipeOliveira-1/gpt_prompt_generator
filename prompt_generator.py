import openai
import sys

# Set the OpenAI API key
openai.api_key = ""

def get_user_input():
    """Get user input for the desired option, prompt, role, and additional information."""
    option = input("Please choose an option:\n1. Simulate an expert\n2. Challenge the conventional narrative\n3. Use unconventional prompts\n4. Ultra-Brainstormer\n5. Add in human-written techniques\n6. Write from different perspectives\n7. Write in different styles or tones, such as satire or irony\nEnter a number: ")

    if option == '1':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role_choice = input("\nPlease choose a role for GPT-3 to act as in the prompt:\n1. A teacher\n2. A scientist\n3. An artist\n4. An entrepreneur\n5. A journalist\n6. Enter your own role\nEnter a number: ")
    
        while role_choice not in ['1', '2', '3', '4', '5', '6']:
            role_choice = input("Invalid role choice. Please enter a valid number or type your own role: ")
    
        if role_choice == '1':
            role = "a teacher"
        elif role_choice == '2':
            role = "a scientist"
        elif role_choice == '3':
            role = "an artist"
        elif role_choice == '4':
            role = "an entrepreneur"
        elif role_choice == '5':
            role = "a journalist"
        elif role_choice == '6':
            role = input("Please enter the role you want GPT-3 to act as in the prompt: ")
        
        additional_info = input("\nAny additional information or context to add to the prompt? ")

    

    elif option == '2':
        topic = input("\nEnter a Topic: ")
        dominant_narrative = input("\nWhat is the dominant narrative? ")
        desired_prompt = f"For the topic about {topic}, give examples that contradict the dominant narrative that said {dominant_narrative}."
        role = "a thought-provoking writer"
        additional_info = ""

    elif option == '3':
        prompt_type = input("\nPlease choose a type of unconventional prompt:\n1. Creative writing\n2. Philosophical\n3. Detective/mystery\nEnter a number: ")
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        if prompt_type == '1':
            role = "a creative writer"
        elif prompt_type == '2':
            role = "a philosopher"
        elif prompt_type == '3':
            role = "Sherlock Holmes"
        additional_info = ""

    elif option == '4':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role = "an idea generator"
        additional_info = input("\nAny additional information or context to add to the prompt? ")

    elif option == '5':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role = "a persuasive writer"
        additional_info = input("\nAny additional information or context to add to the prompt? ")

    elif option == '6':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role = "a group of characters with different backgrounds or viewpoints"
        additional_info = input("\nPlease provide information about the different perspectives you want to include: ")

    elif option == '7':
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

    prompt = f"Act as {role}. {desired_prompt}. {additional_info}."
    print("\nHere's an example of a prompt you could use:\n")
    print(prompt)

    generated_prompt = generate_response(prompt)
    return generated_prompt


# Call the generate_prompt() function and print the generated prompt
print(generate_prompt())
