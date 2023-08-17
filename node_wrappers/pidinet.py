from ..utils import common_annotator_call, annotator_ckpts_path, HF_MODEL_NAME
import controlnet_aux
import comfy.model_management as model_management

class PIDINET_Preprocessor:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",), "safe": (["enable", "disable"], {"default": "enable"})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "preprocessors/edge_line"

    def execute(self, image, safe, **kwargs):
        model = controlnet_aux.PidiNetDetector.from_pretrained(HF_MODEL_NAME, cache_dir=annotator_ckpts_path).to(model_management.get_torch_device())
        return (common_annotator_call(model, image, safe = safe == "enable"), )

NODE_CLASS_MAPPINGS = {
    "PiDiNetPreprocessor": PIDINET_Preprocessor,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "PiDiNetPreprocessor": "PiDiNet Lines"
}