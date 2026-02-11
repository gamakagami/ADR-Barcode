# ADR-Barcode

Short description
This repository provides a small Python utility and optional HTTP endpoint to generate barcode images from input strings. The project is named "ADR-Barcode" (fill in what ADR stands for in your project context — e.g., "Automated Data Recorder" or "Architectural Decision Record" — clarify in this README).

Quick start:
  
  **Using Docker (Recommended for professional use case):**
  1. `docker build -t adr-barcode .`
  2. `docker run -p 8000:8000 adr-barcode`
  3. Open `http://localhost:8000` in your browser.

  **Using Python directly (Recommended for development and testing):**
  1. `python -m venv .venv`
  2. `source .venv/bin/activate` (or `source .venv/bin/activate.fish` for fish shell)
  3. `pip install -r requirements.txt`
  4. `python -m server.app`
  5. Open `http://localhost:8000` in your browser.

  **Using the Desktop GUI:**
  1. Ensure dependencies are installed: `pip install -r requirements.txt`
  2. Run the GUI: `python -m app.gui`

Example usage

Generate a barcode image via CLI, HTTP endpoint, or GUI:

  1. **Web Interface**: Go to `http://localhost:8000` and use the form.
  2. **Desktop GUI**: Run `python -m app.gui` and use the graphical interface.
  3. **HTTP API**: `GET /barcode?data=123456789012&type=ean13`
  4. **CLI**: `python -m app.main --data "123456789012" --type ean13`
