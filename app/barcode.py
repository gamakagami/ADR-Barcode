from pathlib import Path
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode(data: str, out_path: str|Path) -> str:
    """
    Generate a Code128 barcode image for `data` and save to out_path (without extension).
    Returns the filename created (full path with extension).
    """
    out_path = Path(out_path)
    # python-barcode will add extension; pass name without extension
    barcode_obj = Code128(data, writer=ImageWriter())
    filename = barcode_obj.save(str(out_path))
    return filename

if __name__ == "__main__":
    # quick manual test
    print(generate_barcode("1234567", "out/mybarcode"))
