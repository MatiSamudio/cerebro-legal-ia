from PIL import Image
import easyocr 
import fitz
import os



def extraer_texto_pdf(pdf_path):
      
    pdf_document = fitz.open(pdf_path)

    text_extracted = ""
      
    for page_num in range(pdf_document.page_count):
      page = pdf_document.load_page(page_num)

      page_text = page.get_text()

      text_extracted += page_text + "\n"

    return text_extracted






def extraer_texto_imagen(path):

        reader = easyocr.Reader(['es'])  
        resultados = reader.readtext(path, detail=0) 
        return "\n".join(resultados).strip()



