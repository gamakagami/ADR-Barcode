import argparse
from app.barcode import generate_barcode
from pathlib import Path
import sys

import sys

def cli():
    p = argparse.ArgumentParser(description="ADR-Barcode CLI")
    p.add_argument("--data", required=True, help="Data to encode in the barcode")
    p.add_argument("--out", default="out/barcode", help="Output file path without extension")
    p.add_argument("--type", default="code128", help="Barcode type (default: code128)")
    args = p.parse_args()
    Path("out").mkdir(parents=True, exist_ok=True)
    try:
        name = generate_barcode(args.data, args.out, args.type)
        print("Saved:", name)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    cli()
