import torch
print(torch.__version__)  # 打印 PyTorch 版本
print(torch.cuda.is_available())  # 如果返回 True，表示 CUDA 可用
print(torch.cuda.get_device_name(0))  # 显示 GPU 名称
