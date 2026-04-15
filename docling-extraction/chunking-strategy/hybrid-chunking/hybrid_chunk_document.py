import json
from pathlib import Path
from docling_core.types.doc import DoclingDocument
from docling.chunking import HybridChunker

def generate_hybrid_rag_chunks(input_json_path: str, output_json_path: str):
    """
    Reads a Docling extracted JSON file, chunks it using HybridChunker, 
    and exports a RAG-ready JSON payload.
    """
    print(f"Loading document from {input_json_path}...")
    with open(input_json_path, "r") as file:
        data = json.load(file)

    # Validate and load the document model
    doc = DoclingDocument.model_validate(data)
    
    # Initialize the hybrid chunker.
    # HybridChunker combines structural hierarchy with token-based splitting
    # to ensure chunks respect both document structure and maximum context window sizes.
    chunker = HybridChunker()
    
    rag_chunks = []
    print("Chunking document using HybridChunker...")
    
    for chunk in chunker.chunk(doc):
        # Extract the core text
        text = chunk.text
        
        # Extract headings path (e.g., ["Chapter 1", "Section 1.1"])
        headings = chunk.meta.headings if chunk.meta.headings else []
        
        # Extract origin metadata if available
        source_filename = chunk.meta.origin.filename if chunk.meta.origin else "Unknown"
        
        # Format the chunk for vector DB ingestion
        rag_payload = {
            "text": text,
            "metadata": {
                "source": source_filename,
                "headings": headings,
                # Contextual string: Appends the header to the beginning for better embedding semantics
                "context_string": f"{' > '.join(headings)}\n{text}" if headings else text
            }
        }
        rag_chunks.append(rag_payload)
        
    print(f"Generated {len(rag_chunks)} chunks.")
    
    # Save the chunked data
    with open(output_json_path, "w") as out_file:
        json.dump(rag_chunks, out_file, indent=2)
        
    print(f"Successfully saved RAG chunks to {output_json_path}")

if __name__ == "__main__":
    # Define input and output paths based on the workspace
    INPUT_FILE = "output.json"
    OUTPUT_FILE = "hybrid_rag_chunks.json"
    
    generate_hybrid_rag_chunks(INPUT_FILE, OUTPUT_FILE)
