from flask import Flask, send_file, request, abort
import tempfile
from app.barcode import generate_barcode
import os

app = Flask(__name__)

@app.route("/barcode")
def barcode_route():
    data = request.args.get("data")
    if not data:
        return abort(400, "Missing 'data' query parameter")
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "barcode")
        filename = generate_barcode(data, out)
        return send_file(filename, mimetype="image/png")

if __name__ == "__main__":
    app.run(port=8000)
