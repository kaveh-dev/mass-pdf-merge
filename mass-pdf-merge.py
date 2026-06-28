# Initializing libraries
from pathlib import Path
from tqdm import tqdm
from colorama import Fore
import tempfile
import time
import logging
import click
import fitz

# Setting up the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)

version = "v1.0.0"

'''
These are for command-like interface.
Example: python mass=pdf-merge.py "C:\\My Folder" "C:\\My fixed pdf.pdf"
You can add the -v switch for verbose mode.
''' 
@click.command()
@click.argument(
    "root_folder",
    type=click.Path(exists=True, path_type=Path, file_okay=False, dir_okay=True)
    )
@click.argument(
    "fixed_pdf",
    type=click.Path(exists=True, path_type=Path, file_okay=True, dir_okay=False)
    )
@click.option(
    "-v",
    "--verbose",
    is_flag=True
)
def main(root_folder: Path, fixed_pdf: Path, verbose: bool):
    """Mass-merges a fixed pdf with other pdfs in a folder recursively."""


    pdf_files = [
        pdf for pdf in root_folder.rglob("*.pdf")
        if pdf.resolve() != fixed_pdf.resolve()
    ]

    logger.info(Fore.GREEN + f"KAVEH-DEV Mass PDF Merger | Version {version}" + Fore.RESET)
    logger.info(f"Found {Fore.GREEN + str(len(pdf_files)) + Fore.RESET} PDF files.")

    processed = 0
    failed = 0
    start_time = time.time()

    for pdf in tqdm(pdf_files, desc="Processing PDFs...", unit="file"):

        try:
       
            output = fitz.open()

            fixed = fitz.open(fixed_pdf)
            output.insert_pdf(fixed)
            fixed.close()

            current = fitz.open(pdf)
            output.insert_pdf(current)
            current.close()

            with tempfile.NamedTemporaryFile(
                dir=pdf.parent,
                suffix=".pdf",
                delete=False
            ) as tmp:
                temp_path = Path(tmp.name)


            output.save(temp_path)
            output.close()

            temp_path.replace(pdf)
       
            processed += 1
            if verbose:
                logger.info(f"{Fore.GREEN + "SUCCESS" + Fore.RESET} | {pdf}")

        except Exception:
            failed += 1
            if verbose:
                logger.info(f"{Fore.RED + "FAIL" + Fore.RESET} | {pdf}")

    elapsed = time.time() - start_time

    logger.info("=" * 60)
    logger.info(Fore.BLUE + "Finished!" + Fore.RESET)
    logger.info(f"Processed : {Fore.GREEN + str(processed) + Fore.RESET}")
    logger.info(f"Failed    : {Fore.RED + str(failed) + Fore.RESET}")
    logger.info(f"Elapsed   : {Fore.YELLOW}{elapsed:.2f}{Fore.RESET} sec")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()