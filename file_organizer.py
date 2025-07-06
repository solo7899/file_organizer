import argparse
import logging

from pathlib import Path

EXTENSION_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".odt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".pl", ".rb"],
}

def scan_directory(directory):
    directory = Path(directory)
    return [f for f in directory.rglob("*") if f.is_file()]

def parse_arguments():
    parser = argparse.ArgumentParser(description="Organize files into directories based on their extensions.")
    parser.add_argument("directory", type=str, help="The directory to organize files in.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output.")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Perform a dry run without making changes.")  
    return parser.parse_args()

def logging_setup():
    logging.basicConfig(
        filename="file_organizer.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    return logger

def log(logger, message, level=logging.INFO, verbose=False):
    if level == logging.INFO:
        logger.info(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.DEBUG:
        logger.debug(message)
    else:
        logger.warning(message)
    
    if verbose:
        print(message)  

if __name__ == "__main__":
    logger = logging_setup() 
    args = parse_arguments()
        
    if not Path(args.directory).exists():
        print("Directory does not exists.")
        exit(1)
    print(f"Organizing files in directory: {args.directory}")
    if args.verbose:
        print("Verbose mode enabled. Detailed output will be shown.")
    if args.dry_run:
        print("Dry run mode enabled. No changes will be made.")
    else:
        print("Files will be organized into directories based on their extensions.")

    files = scan_directory(args.directory)
    log(logger, f"Found {len(files)} files in directory: {args.directory}", verbose=args.verbose)

    
