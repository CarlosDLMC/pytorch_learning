import torch

print(f"Is the GPU available? {torch.cuda.is_available()}")
print(f"Device count: {torch.cuda.device_count()}")
used_device = torch.cuda.current_device()
print(f"Used device: {used_device}")
print(f"Used device name: {torch.cuda.get_device_name(used_device)}")