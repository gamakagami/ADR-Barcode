import os
from app.barcode import generate_barcode
from pathlib import Path

def test_generate_barcode_creates_file(tmp_path):
    out = tmp_path / "barcode"
    filename = generate_barcode("TEST123", out)
    assert Path(filename).exists()
    # Clean up
    Path(filename).unlink()
