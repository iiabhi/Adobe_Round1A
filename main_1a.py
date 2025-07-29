
import json, time
from pathlib import Path

from src.outline_extractor import extract_outline

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")


def main() -> None:
    if not INPUT_DIR.exists():
        raise SystemExit("❌  'input/' directory not found.")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(INPUT_DIR.glob("*.pdf"))
    if not pdf_files:
        print("⚠️  No PDFs detected in 'input/'")
        return

    for pdf in pdf_files:
        t0 = time.perf_counter()
        outline = extract_outline(pdf)
        out_path = OUTPUT_DIR / (pdf.stem + ".json")
        out_path.write_text(json.dumps(outline, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        print(f"✔ {pdf.name:30} → {out_path.name:20} "
              f"{time.perf_counter() - t0:.2f}s")


if __name__ == "__main__":
    main()
