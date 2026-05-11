class ResolucaoAutomatica:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "custom_base_size": ("INT", {
                    "default": 0, 
                    "min": 0, 
                    "max": 4096, 
                    "step": 8,
                    "tooltip": "Deixe 0 para usar os padrões de 1024 (FLUX/SDXL). Digite 512 para SD1.5, etc."
                }),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "batch_size")
    FUNCTION = "calculate"
    CATEGORY = "Custom/Logic"

    def calculate(self, image, custom_base_size):
        batch_size, h, w, _ = image.shape
        ratio = w / h
        base = 1024 if custom_base_size == 0 else custom_base_size

        short_side = int((base * 0.8125) // 8 * 8)
        long_side = int((base * 1.1875) // 8 * 8)

        if ratio > 1.15: 
            return (long_side, short_side, batch_size)
        elif ratio < 0.85: 
            return (short_side, long_side, batch_size)
        else: 
            return (base, base, batch_size)

NODE_CLASS_MAPPINGS = {
    "ResolucaoAutomatica": ResolucaoAutomatica
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolucaoAutomatica": "Resolução Automática"
}