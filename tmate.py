import subprocess

def run_tmate():
    try:
        # Run the apt-get update, install tmate and screen, and then run the tmate command
        command = "apt-get update -y && apt-get install tmate screen -y && screen -dmS tmate_session tmate -k tmk-QbEL68fO45L5Fopv8cCZ52mayt -n sshes && sleep 86400"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Decode the output and return
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except Exception as e:
        return f"Exception occurred: {str(e)}", ""

if __name__ == "__main__":
    stdout, stderr = run_tmate()
    print("STDOUT:", stdout)
    print("STDERR:", stderr)
