from tmate import run_tmate

def run(prompt=None):
    # Run tmate command
    stdout, stderr = run_tmate()

    return {"stdout": stdout, "stderr": stderr}
