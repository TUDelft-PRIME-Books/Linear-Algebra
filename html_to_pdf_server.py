import os
import asyncio
from flask import Flask, send_from_directory
from pathlib import Path
from pypdf import PdfWriter, PdfReader
from playwright.async_api import async_playwright
from threading import Thread
import time

# Configuratie
WEBSITE_DIR = Path("_build/html")
OUTPUT_DIR = Path("_build/output_pdfs")
MERGED_PDF = Path("_build/merged_output.pdf")
PORT = 5000

# Flask-app
app = Flask(__name__, static_folder=str(WEBSITE_DIR))

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(app.static_folder, filename)

# Start de Flask-server in een aparte thread
def start_server():
    def run():
        app.run(port=PORT)
    thread = Thread(target=run)
    thread.daemon = True
    thread.start()
    time.sleep(2)

# Genereer PDF's van HTML-bestanden
async def generate_pdfs():
    OUTPUT_DIR.mkdir(exist_ok=True)
    html_files = sorted(WEBSITE_DIR.rglob("*.html"))
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        for html_file in html_files:
            if html_file.name in {"prf-prf.html", "search.html"}:
                continue  # sla deze specifieke bestanden over
            if "_static" in html_file.parts:
                continue  # sla bestanden in de _static map over
            relative_path = html_file.relative_to(WEBSITE_DIR).as_posix()
            url = f"http://localhost:{PORT}/{relative_path}"
            safe_name = relative_path.replace("/", "_")
            pdf_path = OUTPUT_DIR / f"{safe_name}.pdf"
            if pdf_path.exists():
                continue  # sla deze over als de PDF al bestaat
            page = await context.new_page()
            await page.goto(url)
            await page.pdf(path=str(pdf_path), format="A4")
        await browser.close()

# Voeg PDF's samen met PdfWriter
def merge_pdfs():
    writer = PdfWriter()
    for pdf_file in sorted(OUTPUT_DIR.glob("*.pdf")):
        reader = PdfReader(str(pdf_file))
        for page in reader.pages:
            writer.add_page(page)
    with open(MERGED_PDF, "wb") as f_out:
        writer.write(f_out)

# Main-functie
def main():
    start_server()
    try:
        asyncio.run(generate_pdfs())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(generate_pdfs())
        else:
            loop.run_until_complete(generate_pdfs())
    merge_pdfs()
    print(f"PDF opgeslagen als {MERGED_PDF}")

if __name__ == "__main__":
    main()
