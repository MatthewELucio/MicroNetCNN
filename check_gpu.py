import torch

# Check if CUDA (GPU support) is available
gpu_available = torch.cuda.is_available()

print(f"Is GPU available? {gpu_available}")

if gpu_available:
    print(f"GPU Count: {torch.cuda.device_count()}")
    print(f"Current GPU Name: {torch.cuda.get_device_name(0)}")
    
    # Check VRAM usage
    print(f"Memory Allocated: {torch.cuda.memory_allocated(0) / 1024**3:.2f} GB")
    print(f"Memory Cached:    {torch.cuda.memory_reserved(0) / 1024**3:.2f} GB")
else:
    print("PyTorch is running on the CPU. Check your Slurm allocation or drivers.")