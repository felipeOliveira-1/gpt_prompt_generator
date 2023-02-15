import os
import openai

# Set the OpenAI API key
openai.api_key = "API-key"

# Define the generate_prompt function
def generate_prompt():
    # Get input from user
    desired_prompt = input("Please enter the prompt you want GPT-3 to respond to: ")
    role = input("What role should GPT-3 act as in the prompt? (e.g. a teacher, a scientist) ")
    additional_info = input("Any additional information or context to add to the prompt? Ex. Prompt: Write an essay about the importance of exercise. Additional information/context: Your audience is a group of sedentary office workers who are looking for ways to improve their physical health and reduce stres: ")

    # Provide an example for each input
    print("Here's an example of a prompt you could use:")
    print(f"Act as a {role}. {additional_info}. {desired_prompt}\n")

    # Create the prompt using the user input
    prompt = f"Act as {role}. {additional_info}. {desired_prompt}"

    # Generate the prompt using the OpenAI API
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

    # Extract the generated prompt from the OpenAI API response
    generated_prompt = response.choices[0].text.strip()

    return generated_prompt

generate_prompt()
