import openai

# Set the OpenAI API key
openai.api_key = ""

# Set the engine name
engine_name = "text-davinci-003"


def get_user_input():
    try:
        options = [
            "Simulate an expert",
            "Challenge the conventional narrative",
            "Write in different styles or tones, such as satire or irony"
        ]
        print("Please choose an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = int(input("Enter the option number: "))
        while choice not in range(1, len(options) + 1):
            choice = int(
                input("Invalid choice. Enter a valid option number: "))

        if choice == 1:
            desired_prompt = input("Enter the prompt: ")
            roles = ["a teacher", "a scientist", "Enter your own role"]
            print("Choose a role:")
            for i, role in enumerate(roles, 1):
                print(f"{i}. {role}")

            role_choice = int(input("Enter the role number: "))
            while role_choice not in range(1, len(roles) + 1):
                role_choice = int(
                    input("Invalid choice. Enter a valid role number: "))

            role = roles[role_choice -
                         1] if role_choice != len(roles) else input("Enter the role: ")
            additional_info = input("Any additional information or context? ")

        elif choice == 2:
            topic = input("Enter a Topic: ")
            dominant_narrative = input("What is the dominant narrative? ")
            desired_prompt = f"For the topic about {topic}, give examples that contradict the dominant narrative that said {dominant_narrative}."
            role = "a thought-provoking writer"
            additional_info = ""

        elif choice == 3:
            desired_prompt = input("Enter the prompt: ")
            styles = ["satire", "irony", "Enter your own style or tone"]
            print("Choose a style or tone:")
            for i, style in enumerate(styles, 1):
                print(f"{i}. {style}")

            style_choice = int(input("Enter the style number: "))
            while style_choice not in range(1, len(styles) + 1):
                style_choice = int(
                    input("Invalid choice. Enter a valid style number: "))

            style = styles[style_choice - 1] if style_choice != len(
                styles) else input("Enter the style or tone: ")
            role = f"a {style} writer"
            additional_info = ""

        prompt = f"Act as {role}. {desired_prompt}. {additional_info}."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            top=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response.choices[0].text)

        critical_mode = input("Do you want to enter critical mode? (y/n): ")
        if critical_mode.lower() == 'y':
            prompt = f"Act as a critic. Criticize these answers and convince me why they are bad. Let's think step by step and provide a new perspective. {response.choices[0].text}"
        response = openai.Completion.create(
            engine=engine_name,
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response.choices[0].text)

    except Exception as e:
        print(f"An error occurred: {e}")


get_user_input()
