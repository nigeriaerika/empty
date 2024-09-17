import subprocess

def get_gpu_info():
    try:
        result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error running nvidia-smi: {result.stderr}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"
