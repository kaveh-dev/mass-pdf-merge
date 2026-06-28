# mass-pdf-merge
A python script to mass merge pdf files in recursive mode.

## What is this for?
I have a learning resource repository site. I needed to create a cover page for each PDF. Programs that do this are not time-efficient. So I wrote this Python script that uses [PyMuPDF](https://github.com/pymupdf/PyMuPDF). 

## Benchmark
In my case, 118 PDF files, some of which were as large as 270 MB, were processed in about 43.7 seconds. In fact, [PyMuPDF](https://github.com/pymupdf/PyMuPDF) is a good option for large and sometimes corrupt PDFs.

## Installation
First, clone the repository:
```bash
git clone https://github.com/kaveh-dev/mass-pdf-merge.git
```

Then install the requirements:
```bash
pip install -r requirements.txt
```
Installation is now complete.

## Usage
To use, just type this line:
```bash
python mass-pdf-merge.py "[PATH_TO_YOUR_PDFS_FOLDER]" "[PATH_TO_YOUR_FIXED_PDF]"
```
> By the way you can use `-v` or `--verbose` at the end of command.

You can also do a fast test on examples I provided:
```bash
python .\mass-pdf-merge.py ".\example\pdfs" ".\example\fixed.pdf"
```
> NOTE : The paths vary depending on the operating system!

The outputs also included in [example/outputs](https://github.com/kaveh-dev/mass-pdf-merge/tree/main/example/outputs).

## License
This code is licensed under the MIT license.

## Contribution
Feel free to [open an issue](https://github.com/kaveh-dev/mass-pdf-merge/issues) or a [pull request](https://github.com/kaveh-dev/mass-pdf-merge/pulls)! Also, don't forget to star ⭐ if you like the code!


