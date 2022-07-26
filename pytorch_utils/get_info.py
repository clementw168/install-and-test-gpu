import torch

def torch_info():
    print('Torch version:', torch.__version__)
    print('Torch is build with CUDA:', torch.cuda.is_available())

def gpu_info():
    gpu_number = torch.cuda.device_count()
    print('GPU is available:', gpu_number > 0)
    if gpu_number > 0:
        print('Torch GPU count:', gpu_number)
        for ind in range(gpu_number):
            print("*"*20)
            print("GPU {}:".format(ind))
            print("Device name:", torch.cuda.get_device_name(ind))
            print("Compute capability:", torch.cuda.get_device_capability(ind))
            print("Memory:", torch.cuda.get_device_properties(ind).total_memory/1024/1024, "MB")