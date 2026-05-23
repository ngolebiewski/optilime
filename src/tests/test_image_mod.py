import pytest
from src.image_mod.img_transformer import open_any_image
from src.image_mod.constants import RAW_EXTENSIONS

def test_open_any_image_wrong_path():
    with pytest.raises(FileNotFoundError):
        open_any_image('./not_a_valid_path.jpg')
        