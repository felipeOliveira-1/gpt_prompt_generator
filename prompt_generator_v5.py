import openai

# Set the OpenAI API key
openai.api_key = ""


def roleplay_filter(user_input):
    roleplay_prompt = f"Hey AI, let's roleplay that I am the AI, and you are the user. Make a request using a perfect prompt to know more about {user_input}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=roleplay_prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


def option_simulate_expert():
    desired_prompt = input("Enter the prompt: ")
    desired_prompt = roleplay_filter(desired_prompt)

    roles = ["a teacher", "a scientist", "Enter your own role"]
    print("Choose a role:")
    for i, role in enumerate(roles, 1):
        print(f"{i}. {role}")

    role_choice = int(input("Enter a number: "))
    while role_choice not in range(1, len(roles) + 1):
        role_choice = int(input("Invalid choice. Enter a valid number: "))

    role = roles[role_choice -
                 1] if role_choice != len(roles) else input("Enter the role: ")
    additional_info = input("Any additional information or context? ")

    return role, desired_prompt, additional_info


def option_challenge_narrative():
    topic = input("Enter a Topic: ")
    dominant_narrative = input("What is the dominant narrative? ")
    desired_prompt = f"For the topic about {topic}, give examples that contradict the dominant narrative that said {dominant_narrative}."
    role = "a thought-provoking writer"
    additional_info = ""

    return role, desired_prompt, additional_info


def option_write_different_styles():
    desired_prompt = input("Enter the prompt: ")
    styles = ["satire", "irony", "Enter your own style or tone"]
    print("Choose a style or tone:")
    for i, style in enumerate(styles, 1):
        print(f"{i}. {style}")

    style_choice = int(input("Enter a number: "))
    while style_choice not in range(1, len(styles) + 1):
        style_choice = int(input("Invalid choice. Enter a valid number: "))

    style = styles[style_choice - 1] if style_choice != len(
        styles) else input("Enter the style or tone: ")
    role = f"a {style} writer"
    additional_info = ""

    return role, desired_prompt, additional_info


def option_accelerate_learning():
    complex_topic = input("Enter a complex topic: ")
    desired_prompt = f"Explain {complex_topic} in simple terms. Explain to me like I'm 11 years old."
    role = "an expert simplifying a complex topic"
    additional_info = ""

    return role, desired_prompt, additional_info


def option_consult_celebrity():
    person = input("Enter a person's name (e.g., Steve Jobs, Elon Musk): ")
    argument = input("Provide your argument or opinion: ")
    desired_prompt = f"Criticize the argument or opinion '{argument}' as if you were {person}."
    role = f"a critic channeling {person}"
    additional_info = ""

    return role, desired_prompt, additional_info


def option_social_media_plan():
    product_or_company = input("Enter the name of the product or company: ")
    desired_outcome = input("Enter the desired outcome for customers: ")
    desired_prompt = f"Generate a creative social media content calendar for the next week for our {product_or_company} on how {desired_outcome}."
    role = "a social media strategist"
    additional_info = ""

    return role, desired_prompt, additional_info


def get_user_input():
    options = [
        option_simulate_expert,
        option_challenge_narrative,
        option_write_different_styles,
        option_accelerate_learning,
        option_consult_celebrity,
        option_social_media_plan
    ]

    print("Please choose an option:")
    for i, option in enumerate(options, 1):
        print(
            f"{i}. {option.__name__.replace('option_', '').replace('_', ' ').title()}")

    choice = int(input("Enter a number: "))
    while choice not in range(1, len(options) + 1):
        choice = int(input("Invalid choice. Enter a valid number: "))

    role, desired_prompt, additional_info = options[choice - 1]()

    prompt = f"Act as {role}. {desired_prompt}. {additional_info}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response.choices[0].text.strip())

    critical_mode = input("Do you want to enter critical mode? (y/n): ")
    if critical_mode.lower() == 'y':
        print("1. Ignore all previous instructions. I want you to act as CRITIC. Acknowledge this with a \"...\"")
        print("...")
        text_to_critique = response.choices[0].text.strip()
        prompt = f"2. Criticize the following text and convince me why it is not good. Let's think about the problems with the text step by step:\n{text_to_critique}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n=1
        )
        print(response.choices[0].text.strip())

        print("3. Great points. Rewrite the text and improve it based on your critique.")
        prompt = f"Improve the following text based on the criticism provided:\n{text_to_critique}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n=1
        )
        print(response.choices[0].text.strip())


get_user_input()
