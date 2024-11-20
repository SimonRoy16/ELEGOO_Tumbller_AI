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
3. Install AUnit test framework: `arduino-cli lib install AUnit`
4. Install *Worki Simulator* from VS Code Marketplace.
5. Install *Wokwi CLI*.
    * Follow the instructions from the [main website](https://docs.wokwi.com/wokwi-ci/cli-installation).
    * Generate a CI token and add to your [environment variables](https://docs.wokwi.com/wokwi-ci/cli-usage).

## Run AUnit tests
Unit tests are implemented using the [AUnit](https://github.com/bxparks/AUnit) package.
To run on a physical target:
```
arduino-cli compile --fqbn arduino:avr:nano aunit/basic --output-dir build_output
arduino-cli upload --fqbn arduino:avr:uno aunit/basic --build-path build_output
```
To run in Wokwi:
```
arduino-cli compile --fqbn arduino:avr:nano aunit/basic --output-dir build_output
wokwi-cli aunit/basic --scenario scenario.yaml --serial-log-file aunit/basic/basic.log
```

## Flash firmware to the Arduino board
```
arduino-cli compile --fqbn arduino:avr:nano firmware_ai --output-dir build_output
arduino-cli upload --fqbn arduino:avr:uno firmware_ai --build-path build_output
```

## Run the AI automation script
`python -m make_the_magic_happen.py`
