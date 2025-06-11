# Ghost Script

Ghost Script è un client da command line per la gestione dei documenti (pdf ma non solo).

Qui riporto alcuni dei comandi che ho utilizzato, ma la documentazione ufficiale è [qui](https://ghostscript.readthedocs.io/en/latest/Use.html).

## -sDEVICE

I device sono i "motori" di GS.
Determinano cosa il client deve fare, quindi determina l'output.

* pdfwrite: produce un pdf;
* pnggray: png in scala di grigio;
* png16m: png a colori;
* pngalpha: png a colori con trasparenza;
* jpeg: jpeg.

I device hanno poi delle opzioni specifiche.

* dPDFSETTING: **pdfwrite** imposta la qualità (dpi): /screen, /ebook, /prepress, /printer, /default;
* r\<num\>: **png...** imposta la qualità (il numero sono i dpi);

## Flag generiche

* sOutputFile: nome del file di output;
* dNOPAUSE: non si ferma dopo aver processato ogni pagina (utile);
* dQUIET: disattiva gli output su terminale;
* dBATCH: chiude GS dopo l'esecuzione del comando;
* dSAFER: attiva le sicurezze;
* dNOSAFER: disattiva le sicurezze;
* dFirstPage: prima pagina dell'input da salvare nell'output;
* dLastPage: ultima pagina (inclusa) dell'input da salvare nell'output;
* q: ???

## Esempi

Convertire in png:

```bash
gs -dBATCH -dNOPAUSE -sDEVICE=pnggray -r300 -sOutputFile=out.png input.pdf
```

Unire pdf:

```bash
gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=union.pdf page1.pdf page2.pdf
```

Cambiare qualità di un pdf:

```bash
gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dPDFSETTING=/screen -sOutputFile=smaller.pdf default.pdf
```

Dividere un pdf nelle sue pagine:

```python
import os

number_of_pages = 10
input_pdf = "input.pdf"

for i in range(1, number_of_pages +1):
    os.system("gs -q -dBATCH -dNOPAUSE -sOutputFile=page{page:02d}.pdf"
              " -dFirstPage={page} -dLastPage={page}"
              " -sDEVICE=pdfwrite {input_pdf}"
              .format(page=i, input_pdf=input_pdf))
```

**Attenzione**: GS non converte i png in pdf, usare ```img2pdf```:

```bash
img2pdf input.png -o output.pdf
```
