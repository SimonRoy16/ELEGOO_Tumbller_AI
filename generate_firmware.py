import json
import os
from openai import OpenAI
from pathlib import Path

def load_json_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def create_system_prompt():
    return """You are an expert embedded systems engineer. You will help generate C firmware for an Arduino-based self-balancing robot according to the provided requirements and abstraction layers.

Generate clean, efficient, and well-structured code that follows these principles:
1. Use clear and descriptive names for functions and variables.
2. Minimize comments - the code should be self-documenting.
3. Follow the specified abstraction layers.
4. Implement robust error handling.
5. Use consistent formatting.
6. Optimize for real-time performance.
7. Ask for clarification if requirements are unclear or information is missing.
"""

def create_user_prompt(requirements, abstraction_layers):
    return f"""Please generate the C firmware for the Elegoo Tumbller robot according to these requirements and abstraction layers:

Requirements:
{json.dumps(requirements, indent=2)}

Abstraction Layers:
{json.dumps(abstraction_layers, indent=2)}

Please provide two files:
1. generated_firmware.h - Contains all public declarations and interfaces
2. generated_firmware.c - Contains all implementations

The code should be complete and ready to compile."""

def save_file(content, filepath):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w') as f:
        f.write(content)

def extract_code_blocks(response):
    # Split response into sections for .h and .c files
    header_start = response.find("```c:generated_firmware.h")
    header_end = response.find("```", header_start + 3)
    source_start = response.find("```c:generated_firmware.c")
    source_end = response.find("```", source_start + 3)

    if header_start == -1 or source_start == -1:
        raise ValueError("Could not find both header and source code blocks in response")

    header_code = response[header_start:header_end].split('\n', 1)[1]
    source_code = response[source_start:source_end].split('\n', 1)[1]

    return header_code, source_code

def main():
    # Load configuration files
    requirements = load_json_file('design_requirements.json')
    abstraction_layers = load_json_file('knowledge/preferred_abstraction_layers.json')

    # Initialize OpenAI client
    client = OpenAI()  # Assumes OPENAI_API_KEY is set in environment variables

    # Create prompts
    system_prompt = create_system_prompt()
    user_prompt = create_user_prompt(requirements, abstraction_layers)

    # Generate code using OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",  # or your preferred model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0  # Lower temperature for more consistent output
    )

    # Extract and save the generated code
    try:
        header_code, source_code = extract_code_blocks(response.choices[0].message.content)

        save_file(header_code, 'firmware_ai/generated_firmware.h')
        save_file(source_code, 'firmware_ai/generated_firmware.c')

        print("Successfully generated firmware files!")

    except Exception as e:
        print(f"Error processing response: {e}")

if __name__ == "__main__":
    main()
