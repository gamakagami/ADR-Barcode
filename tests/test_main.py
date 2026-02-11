import subprocess
import sys
from pathlib import Path
import pytest

# Add project root to the path to allow imports.
sys.path.insert(0, str(Path(__file__).parent.parent))

from shared.constants import MAX_DATA_LENGTH

def test_cli_success():
    """Test the CLI runs successfully and creates a file."""
    output_file = "test_barcode.png"
    result = subprocess.run(
        [sys.executable, "-m", "app.main", "--data", "12345", "--out", output_file],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Saved:" in result.stdout
    # The actual filename includes the extension added by the library.
    # We will just check if the file with extension exists.
    created_file = Path(result.stdout.strip().split(" ")[1])
    assert created_file.exists()
    created_file.unlink()

def test_cli_long_data():
    """Test the CLI fails with data that is too long."""
    long_data = "a" * (MAX_DATA_LENGTH + 1)
    result = subprocess.run(
        [sys.executable, "-m", "app.main", "--data", long_data, "--out", "test_barcode"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "Input data is too long" in result.stderr


def test_cli_no_data():
    """Test the CLI fails when no data is provided."""
    result = subprocess.run(
        [sys.executable, "-m", "app.main", "--out", "test_barcode"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "the following arguments are required: --data" in result.stderr
