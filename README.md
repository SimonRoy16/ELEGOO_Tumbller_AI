# ELEGOO Tumbller AI Code Generator
This project leverages AI multi-agents to generate the embedded firmware for the [ELEGOO Tumbller toy](https://www.amazon.ca/ELEGOO-Tumbller-Self-Blancing-Compatible-Arduino/dp/B07R1XP3YX).

## Installation Instructions (Windows)
1. Install Arduino-CLI: https://arduino.github.io/arduino-cli/1.1/
    * Update the core index: `arduino-cli core update-index`
2. Configure Python environment:
    * python3 -m venv venv
    * .\venv\Scripts\activate
    * pip install -r requirements.txt
    * (optional) deactivate

## Generate Firmware
`python -m make_the_magic_happen.py`

## Flash to the Arduino board
```
arduino-cli compile --fqbn arduino:avr:nano Tumbller_AI --output-dir build_output
arduino-cli upload --fqbn arduino:avr:uno Tumbller_AI --build-path build_output
```
