# https://ghostscript.readthedocs.io/en/latest/Use.html

# to convert pdf to png
# gs -dBATCH -dNOPAUSE -sDEVICE=pnggray -r600 -sOutputFile=certificato.png certificato.pdf

# to attach pdfs
# gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTING=/prepress -sOutputFile=out.pdf cert_1.PDF page0002.pdf page0003.pdf page0004.pdf

# to convert png to pdf
# img2pdf dott_marca_small.png -o out.pdf