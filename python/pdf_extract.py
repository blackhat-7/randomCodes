import pdfplumber

with pdfplumber.open(r'/Users/macbookpro/Downloads/Flux_data_scientist.pdf') as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
print('Done')
