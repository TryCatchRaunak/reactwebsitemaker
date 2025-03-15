import fitz  
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import io
import os

# Hardcoded input and output file paths
PDF_PATH = "/home/trycatchraunak/PycharmProjects/websitemaker/src/websitemaker/SDD_FINAL (1).pdf"
OUTPUT_TXT_PATH = "/home/trycatchraunak/PycharmProjects/websitemaker/src/websitemaker/SDD.txt"

def extract_text_from_pdf(pdf_path, output_txt_path):
    if not os.path.exists(pdf_path):
        print(f"Error: File not found - {pdf_path}")
        return
    
    doc = fitz.open(pdf_path)
    extracted_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")  

        if text.strip():  
            extracted_text += f"\n\n--- Page {page_num + 1} ---\n{text}\n"
        else:  
            images = page.get_images(full=True)
            if images:
                extracted_text += f"\n\n--- Page {page_num + 1} (Image OCR) ---\n"
                for img_index, img in enumerate(images):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    img_pil = Image.open(io.BytesIO(image_bytes))

                    ocr_text = pytesseract.image_to_string(img_pil)
                    extracted_text += f"Image {img_index + 1} OCR Text:\n{ocr_text}\n"

    with open(output_txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(extracted_text)

    print(f"Extraction complete! Text saved to {output_txt_path}")

extract_text_from_pdf(PDF_PATH, OUTPUT_TXT_PATH)