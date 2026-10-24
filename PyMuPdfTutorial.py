#From SOunak Da


import pymupdf
import os

def extract_images_from_page_as_png(pdf_path, page_index):
    output_dir=f"output_images_page{page_index+1}"
    os.makedirs(output_dir, exist_ok=True)

    doc = pymupdf.open(pdf_path)
    page = doc[page_index]

    image_list = page.get_images(full=True)
    print(f"Found {len(image_list)} images on page {page_index + 1}")

    for i, img in enumerate(image_list):
        xref = img[0]

        try:
            pix = pymupdf.Pixmap(doc, xref)

            # Skip mask-only images
            if pix.n < 3:
                print(f"Skipping mask image {xref}")
                continue

            # Convert everything to RGB
            if pix.n > 3:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

            filename = os.path.join(output_dir, f"page{page_index}_image_{i+1}.png")
            pix.save(filename)
            print("Saved:", filename)

        except Exception as e:
            print(f"Skipped image {xref}: {e}")

    doc.close()

extract_images_from_page_as_png("Smally.pdf", 3)