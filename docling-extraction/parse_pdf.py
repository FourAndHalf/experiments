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

print("Successfully converted PDF to Markdown and JSON.")
