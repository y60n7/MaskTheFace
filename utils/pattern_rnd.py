import random
from pathlib import Path

def get_random_texture_paths():
    base_path = Path("/content/MaskTheFace")
    texture_path = base_path / "masks" / "textures" 
    textures_file_paths = []
    for texture_file in texture_path.iterdir():
        if texture_file.is_file() and texture_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            textures_file_paths.append(texture_file)
    return random.choice(textures_file_paths)
