## OpenAI Prompt Generator, Expert Simulation with Prompt Filter
This Python script uses OpenAI's GPT-4 engine to simulate a variety of experts in different scenarios. The user selects an option from a list, and the AI generates a response according to the chosen role and prompt. Additionally, the script features a critical mode, where the AI can critique and improve its own generated content. A unique aspect of this script is the prompt filter, which helps create more refined prompts for the AI to answer.

## Features

* Simulate Expert: The AI simulates an expert in a chosen field.

* Challenge Narrative: The AI provides examples contradicting a given dominant narrative.

* Write in Different Styles: The AI generates content in various writing styles and tones.

* Critical Mode (Optional): After displaying the generated text, the program asks the user whether they want to enter "critical mode." If the user answers 'y' (yes), the program constructs a new prompt that asks the GPT-3.5 model to act as a critic and criticize the previously generated response, providing a new perspective. The program then displays the critical response.

## Usage
Ensure you have Python 3.x installed.

Install the openai package using pip: 

``
pip install openai
``

Replace the placeholder API key in the script with your own OpenAI API key.

Run the script: 

``
python prompt_generator_v5.py
``

Follow the prompts to choose an option, provide the required information, and receive the AI-generated response.
Optionally, enter critical mode to have the AI critique and improve its own generated content.

## Dependencies
Python 3.x
openai
## License
This project is licensed under the MIT License.

Please note that this project uses the OpenAI API, and you will need an API key to run the script. Additionally, the AI model used is GPT-4, so make sure you have access to it before running the script.
