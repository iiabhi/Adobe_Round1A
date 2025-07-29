

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List

from megaparse import Document   


def extract_outline(pdf_path: str | Path) -> Dict:
    pdf_path = Path(pdf_path)
    doc = Document.parse(str(pdf_path), ocr=False)   

    outline_raw: List[Dict] = doc.outline

    title = None
    outline_formatted = []

    for item in outline_raw:
        level_num = int(item["level"])            
        level_tag = f"H{level_num}"
        if level_tag == "H1" and title is None:
            title = item["text"]
        outline_formatted.append(
            {
                "level": level_tag,
                "text": item["text"],
                "page": int(item["page"]),
            }
        )

    return {
        "title": title or "Untitled Document",
        "outline": outline_formatted,
    }


if __name__ == "__main__":
    import argparse, time
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", help="Path to a PDF file")
    args = ap.parse_args()

    t0 = time.perf_counter()
    data = extract_outline(args.pdf)
    out_path = Path(args.pdf).with_suffix(".json")
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Saved → {out_path}  ({time.perf_counter() - t0:.2f}s)")
