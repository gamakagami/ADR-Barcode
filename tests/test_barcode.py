import os
from app.barcode import generate_barcode
from pathlib import Path
import pytest
from shared.constants import MAX_DATA_LENGTH

def test_generate_barcode_creates_file(tmp_path):
    out = tmp_path / "barcode"
    filename = generate_barcode("TEST123", out)
    assert Path(filename).exists()
    # Clean up
    Path(filename).unlink()

def test_generate_barcode_long_data_raises_error():
    """Test that generate_barcode raises ValueError for data that is too long."""
    long_data = "a" * (MAX_DATA_LENGTH + 1)
    with pytest.raises(ValueError, match=f"Input data is too long. Maximum length is {MAX_DATA_LENGTH} characters."):
        generate_barcode(long_data, "out/barcode")

def test_generate_barcode_invalid_type_raises_error():
    """Test that generate_barcode raises ValueError for invalid barcode type."""
    with pytest.raises(ValueError, match="Invalid barcode type: invalid_type"):
        generate_barcode("TEST123", "out/barcode", "invalid_type")

def test_generate_barcode_valid_type(tmp_path):
    """Test that generate_barcode works with a valid, non-default type."""
    out = tmp_path / "barcode_ean13"
    # EAN13 requires 12 or 13 digits
    filename = generate_barcode("123456789012", out, "ean13")
    assert Path(filename).exists()
    Path(filename).unlink()
