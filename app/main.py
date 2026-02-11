import argparse
from app.barcode import generate_barcode
from pathlib import Path

def cli():
    p = argparse.ArgumentParser(description="ADR-Barcode CLI")
    p.add_argument("--data", required=True, help="Data to encode in the barcode")
    p.add_argument("--out", default="out/barcode", help="Output file path without extension")
    args = p.parse_args()
    Path("out").mkdir(parents=True, exist_ok=True)
    name = generate_barcode(args.data, args.out)
    print("Saved:", name)

if __name__ == "__main__":
    cli()
