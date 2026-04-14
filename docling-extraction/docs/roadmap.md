# Docling Prototype Roadmap

## 1. Environment Setup
- Activate the virtual environment: `source venv/bin/activate` (already exists at `/home/fourandhalf/Documents/Projects/experiments/docling-extraction/venv`).
- Install docling: `pip install docling`.

## 2. Basic Conversion Script
- Create `parse_pdf.py`.
- Implementation:
  ```python
  from docling.document_converter import DocumentConverter
  from pathlib import Path
  import json

  source = "data/dynamo-amazons-highly-available-key-value-store-2007.pdf"
  converter = DocumentConverter()
  result = converter.convert(source)

  # Export to Markdown
  Path("output.md").write_text(result.document.export_to_markdown())
  
  # Export to JSON
  with open("output.json", "w") as f:
      json.dump(result.document.export_to_dict(), f, indent=2)
  ```

## 3. Optional: Hybrid Chunking
- Integrate `docling.chunking.HybridChunker` to test document segmentation for RAG workflows.
