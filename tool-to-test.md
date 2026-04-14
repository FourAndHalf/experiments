# Tooling Test Plan

## 1. Document Extraction Tools

This section outlines the testing plan for document extraction tools. The goal is to evaluate their performance, accuracy, and ease of use for our specific use cases.

---

### 1.1. unstructured.io

- **Objective:** Evaluate the effectiveness of `unstructured.io` for extracting clean, structured text and metadata from various document formats, particularly complex PDFs and Word documents.
- **Website:** [https://unstructured.io/](https://unstructured.io/)

#### Key Features to Test:

- **Partitioning:** Accuracy of document element partitioning (e.g., titles, paragraphs, tables, lists).
- **Chunking:** Effectiveness of text chunking strategies for downstream RAG applications.
- **Metadata Extraction:** Completeness and accuracy of extracted metadata (e.g., filename, page number, parent directory).
- **Format Support:** Performance across different file types (.pdf, .docx, .pptx, .html).
- **Cleaning:** Quality of text cleaning (e.g., removal of headers/footers, handling of special characters).
- **Scalability:** Performance on large documents and in batch processing scenarios.

#### Test Cases:

| Case ID | Description                                                                 | Expected Outcome                                                              | Actual Outcome | Status      |
| :------ | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :------------- | :---------- |
| **TC-U01**  | Extract content from a multi-page PDF with headers, footers, and tables.  | Text is accurately extracted, tables are preserved in a structured format, and headers/footers are ignored. | *Pending*      | `Not Started` |
| **TC-U02**  | Process a directory of mixed-format documents (`.pdf`, `.docx`).            | All documents are processed successfully without errors. The output is consistent and well-structured. | *Pending*      | `Not Started` |
| **TC-U03**  | Extract text from a scanned PDF (requires OCR).                             | The OCR engine accurately converts image-based text to machine-readable text. | *Pending*      | `Not Started` |
| **TC-U04**  | Run the tool on a large (500+ pages) document to test performance.        | The process completes within an acceptable time frame without excessive memory usage. | *Pending*      | `Not Started` |

#### Notes:

- *Initial setup seems straightforward with their Docker image.*
- *Need to investigate the different "strategies" (e.g., `fast`, `hi_res`) and their impact on performance vs. accuracy.*

---

### 1.2. Apache Tika

- **Objective:** Assess the capability of Apache Tika to extract content and metadata from a wide variety of file formats, focusing on its robustness and extensibility.
- **Website:** [https://tika.apache.org/](https://tika.apache.org/)

#### Key Features to Test:

- **Content Extraction:** Raw text extraction quality from various document formats.
- **Metadata Detection:** Ability to automatically detect and extract rich metadata (e.g., author, creation date, software used).
- **Language Detection:** Accuracy of identifying the primary language of the document content.
- **Parser Integration:** How well it handles different document parsers (e.g., PDFBox for PDFs, POI for Office documents).
- **MIME Type Detection:** Robustness of file type identification.
- **Deployment:** Ease of running as a standalone server or integrating as a Java library.

#### Test Cases:

| Case ID | Description                                                                 | Expected Outcome                                                              | Actual Outcome | Status      |
| :------ | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :------------- | :---------- |
| **TC-T01**  | Extract content and metadata from a PDF document.                           | Both the full text and key metadata fields (Author, Title, Subject) are extracted successfully. | *Pending*      | `Not Started` |
| **TC-T02**  | Process an embedded file within a `.docx` document.                         | Tika's recursive parsing identifies and extracts content from the embedded file. | *Pending*      | `Not Started` |
| **TC-T03**  | Run language detection on a document containing multiple languages.         | The primary language is correctly identified in the metadata.                 | *Pending*      | `Not Started` |
| **TC-T04**  | Use the Tika Server (`tika-server`) to process a file via a REST API call.  | The server responds with the extracted content in the requested format (e.g., plain text, JSON). | *Pending*      | `Not Started` |

#### Notes:

- *Mature and well-established tool with a huge range of supported formats.*
- *The Tika Server provides a convenient way to integrate with non-JVM applications.*
- *Need to compare the output quality directly against `unstructured.io` for the same set of test documents.*
