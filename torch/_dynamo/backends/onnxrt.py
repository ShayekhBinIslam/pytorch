# This backend is maintained by ONNX team. To direct issues
# to the right people, please tag related GitHub issues with `module: onnx`.
#
# Maintainers' Github IDs: wschin, thiagocrepaldi, BowenBao, abock
from torch.onnx._internal.onnxruntime import is_onnxrt_supported, torch_compile_backend
from .registry import register_backend

def has_onnxruntime():
    # FIXME(abock): update test/dynamo/test_backends.py to call is_onnxrt_supported()
    return is_onnxrt_supported()

if is_onnxrt_supported():
    register_backend(name="onnxrt", compiler_fn=torch_compile_backend)
else:

    def information_displaying_backend(*args, **kwargs):
        raise ImportError(
            "onnxrt is not registered as a backend. "
            "Please make sure all dependencies such as "
            "numpy, onnx, onnxscript-preview, and onnxruntime-training are installed. "
            "Suggested procedure to fix dependency problem:\n"
            "  (1) pip or conda install numpy onnx onnxscript-preview onnxruntime-training.\n"
            "  (2) Open a new python terminal.\n"
            "  (3) Call the API `torch.onnx.is_onnxrt_supported()`:\n"
            "  (4)   If it returns `True`, then you can use `onnxrt` backend.\n"
            "  (5)   If it returns `False`, please execute the package importing section in "
            "torch/onnx/_internal/onnxruntime.py under pdb line-by-line to see which import fails."
        )

    register_backend(name="onnxrt", compiler_fn=information_displaying_backend)
