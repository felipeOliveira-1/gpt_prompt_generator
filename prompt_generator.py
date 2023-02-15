import os
import openai

# Set the OpenAI API key
openai.api_key = ""

def get_user_input():
    desired_prompt = input("\nPlease enter the prompt you want GPT-3 to respond to: ")
    role = input("\nWhat role should GPT-3 act as in the prompt? (e.g. a teacher, a scientist) ")
    additional_info = input("\nAny additional information or context to add to the prompt? \nExample:\nPrompt: Write an essay about the importance of exercise. \nAdditional information/context: Your audience is a group of sedentary office workers who are looking for ways to improve their physical health and reduce stres\n")

    return desired_prompt, role, additional_info

def create_prompt(desired_prompt, role, additional_info):
    example = f"Act as a {role}. {additional_info}. {desired_prompt}\n"
    print("Here's an example of a prompt you could use:")
    print(example)

    prompt = f"Act as {role}. {additional_info}. {desired_prompt}"
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
    desired_prompt, role, additional_info = get_user_input()
    prompt = create_prompt(desired_prompt, role, additional_info)
    generated_prompt = generate_response(prompt)
    return generated_prompt

generate_prompt()
