import subprocess

def main():
    def execute_commands(commands: list):
        results = []
        for command in commands:
            results.append(subprocess.run(command, shell=True, capture_output=True, text=True))
        return results

    process_outputs = execute_commands([
        "arduino-cli compile --fqbn arduino:avr:nano aunit/basic --output-dir build_output",
        "wokwi-cli aunit/basic --scenario scenario.yaml --serial-log-file aunit/basic/basic.log",
    ])
    for process_output in process_outputs:
        print(f"Command: {process_output.args}")
        print(f"Console output:", process_output.stdout)

    print("Magically generating Tumbller firmware.")
    # TODO: Add the magic here

if __name__ == "__main__":
    main()
