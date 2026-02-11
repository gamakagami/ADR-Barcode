from flask import Flask, send_file, request, abort
import tempfile
from app.barcode import generate_barcode
from shared.constants import MAX_DATA_LENGTH
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ADR Barcode Generator</title>
        <style>
            body { font-family: sans-serif; max-width: 600px; margin: 2rem auto; padding: 0 1rem; }
            form { display: flex; flex-direction: column; gap: 1rem; }
            label { font-weight: bold; }
            input, select, button { padding: 0.5rem; font-size: 1rem; }
            button { background-color: #007bff; color: white; border: none; cursor: pointer; }
            button:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <h1>ADR Barcode Generator</h1>
        <form action="/barcode" method="get">
            <label for="data">Data:</label>
            <input type="text" id="data" name="data" required placeholder="Enter barcode data">
            
            <label for="type">Barcode Type:</label>
            <select id="type" name="type">
                <option value="code128">Code 128</option>
                <option value="ean13">EAN-13</option>
                <option value="ean8">EAN-8</option>
                <option value="gs1">GS1-128</option>
                <option value="gtin">GTIN</option>
                <option value="isbn">ISBN</option>
                <option value="isbn10">ISBN-10</option>
                <option value="isbn13">ISBN-13</option>
                <option value="issn">ISSN</option>
                <option value="jan">JAN</option>
                <option value="pzn">PZN</option>
                <option value="upc">UPC</option>
                <option value="upca">UPC-A</option>
            </select>
            
            <button type="submit">Generate Barcode</button>
        </form>
    </body>
    </html>
    """

@app.route("/barcode")
def barcode_route():
    data = request.args.get("data")
    if not data:
        return abort(400, "Missing 'data' query parameter")
    if len(data) > MAX_DATA_LENGTH:
        return abort(400, f"Input data is too long. Maximum length is {MAX_DATA_LENGTH} characters.")
    try:
        with tempfile.TemporaryDirectory() as td:
            out = os.path.join(td, "barcode")
            barcode_type = request.args.get("type", "code128")
            filename = generate_barcode(data, out, barcode_type)
            return send_file(filename, mimetype="image/png")
    except ValueError as e:
        return abort(400, str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
