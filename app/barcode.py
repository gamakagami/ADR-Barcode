from pathlib import Path
from barcode import get_barcode_class
from barcode.writer import ImageWriter
from barcode.errors import BarcodeNotFoundError
from shared.constants import MAX_DATA_LENGTH

def generate_barcode(data: str, out_path: str|Path, barcode_type: str = "code128") -> str:
    """
    Generate a Code128 barcode image for `data` and save to out_path (without extension).
    Returns the filename created (full path with extension).
    """
    if len(data) > MAX_DATA_LENGTH:
        raise ValueError(f"Input data is too long. Maximum length is {MAX_DATA_LENGTH} characters.")

    out_path = Path(out_path)
    
    try:
        barcode_class = get_barcode_class(barcode_type)
    except BarcodeNotFoundError:
        raise ValueError(f"Invalid barcode type: {barcode_type}")

    # python-barcode will add extension; pass name without extension
    barcode_obj = barcode_class(data, writer=ImageWriter())
    filename = barcode_obj.save(str(out_path))
    return filename

if __name__ == "__main__":
    # quick manual test
    print(generate_barcode("1234567", "out/mybarcode"))
