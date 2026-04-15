from docling_core.types.doc import DoclingDocument, SectionHeaderItem, TitleItem
import json

with open("output.json", "r") as file:
    data = json.load(file)

doc = DoclingDocument.model_validate(data)

for item, level in doc.iterate_items():
    if isinstance(item, (SectionHeaderItem, TitleItem)):
        print(f"Level {level}: {item.label}")
