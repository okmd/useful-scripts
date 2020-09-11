import os
import argparse
try:
    from PyPDF2 import PdfFileMerger, PdfFileReader
except ImportError:
    print("Please install pypdf2 as pip install PyPDF2")
    # pip install PyPDF2


parser = argparse.ArgumentParser(description='Take inputs pdfs to be merged into single pdf.')
parser.add_argument('--ifiles', nargs='+', required=True, help='Input files to be merged into single pdf file.')
parser.add_argument('--ofile', required=True, help='Final output single pdf file.')

args = parser.parse_args()

def mergeFiles():
    merger = PdfFileMerger()
    for filename in args.ifiles:
        filetype = filename.split(".")[-1].lower()
        if filetype != "pdf":
            print(f"{filename} is not a pdf file.")
            return
        elif os.path.exists(filename):
            merger.append(PdfFileReader(open(filename, 'rb')))
        else:
            print(f"{filename} not exist.")
    return merger.write(os.path.join(os.getcwd(), args.ofile))

if __name__ == "__main__":
    mergeFiles()
    print(f"Sucessfully written to {args.ofile}.")
    
   
   
 ## USAGE ##
 # python .\merge-n-pdfs-into-single-pdf.py --ifiles x.pdf y.pdf --ofile z.PDF
