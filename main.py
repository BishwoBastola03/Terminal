import subprocess

def execute_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

if __name__ == '__main__':
    command = input("Enter a command: ")
    output = execute_command(command)
    print(output)