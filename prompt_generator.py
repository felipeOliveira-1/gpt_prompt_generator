import os
import openai
import sys

# Set the OpenAI API key
openai.api_key = ""

def get_user_input():
    option = input("Please choose an option:\n1. Simulate an expert\n2. Challenge the conventional narrative\n3. Use unconventional prompts\n4. Ultra-Brainstormer\n5. Add in human-written techniques\n6. Write from different perspectives\n7. Write in different styles or tones, such as satire or irony\n\n")
    desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
    role = input("\nWhat role should GPT-3 act as in the prompt? (e.g. a teacher, a scientist) ")
    additional_info = input("\nAny additional information or context to add to the prompt? ")

    return option, desired_prompt, role, additional_info

def get_user_input():
    option = input("Please choose an option:\n1. Simulate an expert\n2. Challenge the conventional narrative\n3. Use unconventional prompts\n4. Ultra-Brainstormer\n5. Add in human-written techniques\n6. Write from different perspectives\n7. Write in different styles or tones, such as satire or irony\n")

    if option == '1':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role =  input("\nWhat role should GPT-3 act as in the prompt? (e.g. a teacher, a scientist) ")
        additional_info = input("\nAny additional information or context to add to the prompt? ")

    elif option == '2':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role = input("\nWhat role should GPT-3 act as in the prompt? (e.g. a teacher, a scientist) ")
        additional_info = input("\nAny additional information or context to add to the prompt? ")

    elif option == '3':
        desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
        role = "a creative writer"
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
        role = "a satirical or ironic writer"
        additional_info = ""

    else:
        print("Invalid option selected.")
        return None

    return option, desired_prompt, role, additional_info


    print(prompt)
    sys.stdout.flush() # add this line to flush the output buffer
    return prompt

def generate_response(prompt):
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
    return generated_prompt

def generate_prompt():
    option, desired_prompt, role, additional_info = get_user_input()

    prompt = f"Act as {role}. {desired_prompt}, {additional_info}. "
    print("Here's an example of a prompt you could use:")
    print(prompt)

    generated_prompt = generate_response(prompt)
    return generated_prompt


# Call the generate_prompt() function and print the generated prompt
print(generate_prompt())
