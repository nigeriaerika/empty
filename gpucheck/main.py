from nvidiasmi import get_gpu_info

def getgpu(prompt=None):
    gpu_info = get_gpu_info()
    return {"gpu_info": gpu_info}
