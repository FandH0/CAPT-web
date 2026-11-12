import torch, numpy, librosa, soundfile

print("torch", torch.__version__, "| CUDA в сборке:", torch.version.cuda)
print("видеокарта доступна:", torch.cuda.is_available())
if torch.cuda.is_available():
    p = torch.cuda.get_device_properties(0)
    print("GPU:", p.name, f"{p.total_memory / 2**30:.1f} ГБ")
    x = torch.randn(1000, 1000, device="cuda")
    print("тест на GPU:", (x @ x).shape)
print("numpy", numpy.__version__, "| librosa", librosa.__version__)
