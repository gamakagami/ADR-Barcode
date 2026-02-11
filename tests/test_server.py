import pytest
from flask import Flask
from app.barcode import generate_barcode
from server.app import app
from shared.constants import MAX_DATA_LENGTH

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_barcode_route_success(client, tmp_path):
    """Test the /barcode route with valid data."""
    # Mock generate_barcode to avoid actual file creation during tests
    # We will rely on our unit test for generate_barcode for actual file creation check.
    # Here, we only care about the Flask response.
    # A simple way to do this is to patch the generate_barcode function for this test.
    # However, for this simple case, we can assume generate_barcode works correctly
    # and focus on the Flask app's handling of requests and responses.

    # To truly isolate, one would use unittest.mock.patch
    # For now, let's ensure it returns a file-like object or similar.

    response = client.get("/barcode?data=TEST123")
    assert response.status_code == 200
    assert response.mimetype == "image/png"
    # Basic check to ensure some content is returned
    assert len(response.data) > 0

def test_barcode_route_missing_data(client):
    """Test the /barcode route with missing data parameter."""
    response = client.get("/barcode")
    assert response.status_code == 400
    assert b"Missing &#39;data&#39; query parameter" in response.data

def test_barcode_route_long_data(client):
    """Test the /barcode route with data that is too long."""
    long_data = "a" * (MAX_DATA_LENGTH + 1)
    response = client.get(f"/barcode?data={long_data}")
    assert response.status_code == 400
    assert f"Input data is too long. Maximum length is {MAX_DATA_LENGTH} characters.".replace("'", "&#39;").encode() in response.data
