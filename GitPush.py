import subprocess


def execute_commands(commands):
    for command in commands:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(f"Command '{command}' executed with exit code {process.returncode}")


commands = [
    "hugo",
    "git add .",
    'git commit -m "upload again"',
    "git push -u origin master",
]

if __name__ == '__main__':
    execute_commands(commands)
