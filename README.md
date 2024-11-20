# ELEGOO Tumbller AI Code Generator
This project leverages AI multi-agents to generate the embedded firmware for the [ELEGOO Tumbller toy](https://www.amazon.ca/ELEGOO-Tumbller-Self-Blancing-Compatible-Arduino/dp/B07R1XP3YX).

## Installation instructions (Windows)
1. Install Arduino-CLI: https://arduino.github.io/arduino-cli/1.1/
    * Update the core index: `arduino-cli core update-index`
2. Configure Python environment:
    * `python -m venv venv`
    * `python -m pip install --upgrade pip`
    * `.\venv\Scripts\activate`
    * `pip install -r requirements.txt`
    * (optional) `deactivate`
3. Install *Worki Simulator* from VS Code Marketplace.
4. Install AUnit test framework: `arduino-cli lib install AUnit`

## Run AUnit tests
Unit tests are implemented using the [AUnit](https://github.com/bxparks/AUnit) package.
```
arduino-cli compile --fqbn arduino:avr:nano aunit/basic --output-dir build_output
arduino-cli upload --fqbn arduino:avr:uno aunit/basic --build-path build_output
```

## Generate firmware using AI
`python -m make_the_magic_happen.py`

## Flash firmware to the Arduino board
```
arduino-cli compile --fqbn arduino:avr:nano firmware_ai --output-dir build_output
arduino-cli upload --fqbn arduino:avr:uno firmware_ai --build-path build_output
```
