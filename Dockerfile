FROM lmsysorg/sglang:v0.4.10.post1-cu126

# Install PyTorch nightly with CUDA 12.9
RUN pip install --upgrade pip && \
    pip install flashinfer-python -i https://flashinfer.ai/whl/cu126/torch2.6/ \
    pip install --pre torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/nightly/cu129
