import subprocess



# Replace 'your_command_here' with the actual command you want to run

command = 'upsc ups@localhost battery.charge'

# Run the command and capture its output

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)



# Check if the command was successful

if result.returncode == 0:

    # Process the output

    output_lines = result.stdout.splitlines()
    print("output: ", output_lines[0])

    if int(output_lines[0]) == 100:
        username = 'root'
        host = '10.22.65.151'
        command = 'shutdown now'

        ssh_command = ['ssh',f'{username}@{host}',command]
        result = subprocess.Popen(ssh_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output, error = result.communicate()

        if result.returncode == 0:
            print("SSH Success, output: ", output)
            exit(0)
        else:
            print("Error : ", error)
else:
    print("Error:", result.stderr)
