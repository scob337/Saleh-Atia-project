import fitz
import os
import glob

# Find PDF file in directory
pdf_files = glob.glob(os.path.join(r'e:\FreeLance\project2', '*.pdf'))
print(f"Found PDFs: {pdf_files}")

if pdf_files:
    pdf_path = pdf_files[0]
    print(f"Opening: {pdf_path}")
    doc = fitz.open(pdf_path)
    print(f"Total pages: {len(doc)}")
    
    out_dir = os.path.join(r'e:\FreeLance\project2', 'images', 'projects')
    os.makedirs(out_dir, exist_ok=True)
    
    for i, page in enumerate(doc):
        # Render at 2x for quality
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)
        out_path = os.path.join(out_dir, f'project-{i+1}.png')
        pix.save(out_path)
        print(f"Saved page {i+1} -> {out_path} ({pix.width}x{pix.height})")
    
    doc.close()
    print("Done!")
else:
    print("No PDF found!")
