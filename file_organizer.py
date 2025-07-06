import argparse
import logging
import shutil

from pathlib import Path


EXTENSION_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".odt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".pl", ".rb"],
}


def scan_directory(directory, verbose=False, dry_run=False, logfile=None):
    if not dry_run:
        logger.info(f"Scanning directory: {directory}")
    if verbose:
        print(f"Scanning directory: {directory}")
    directory = Path(directory)
    return [f for f in directory.rglob("*") if f.is_file() and f.name != logfile]


def parse_arguments():
    parser = argparse.ArgumentParser(description="Organize files into directories based on their extensions.")
    parser.add_argument("directory", type=str, help="The directory to organize files in.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output.")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Perform a dry run without making changes.")  
    parser.add_argument("--logname", "-l", type=str, default="file_organizer.log", help="Name of the log file.")
    return parser.parse_args()


def logging_setup(logname):
    logging.basicConfig(
        filename=Path.cwd()/logname,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    return logger


def log(logger, message, level=logging.INFO):
    if level == logging.INFO:
        logger.info(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.DEBUG:
        logger.debug(message)
    else:
        logger.warning(message)


def categorize_file(file:Path):
    file_extension = file.suffix.lower()
    for category, extensions in EXTENSION_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Others"
    

def move(file:Path, file_category, verbose=False, dry_run=False):
    if dry_run:
        print(f"Dry run: {file} would be moved to {file_category}")
        return
    if not file_category.exists():
        Path(file_category).mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory: {file_category}")
        if verbose:
            print(f"Created directory: {file_category}")
    shutil.move(file, file_category)
    logger.info(f"Moved {file} to {file_category}")
    if verbose:
        print(f"Moving {file} to {file_category}")


def organize_files(files:list[Path], dry_run=False, verbose=False):
    if len(files) == 0:
        print("No files found to organize.")
        return

    cwd = Path.cwd()
    for file in files:
        file_category = categorize_file(file)
        move(file, cwd/file_category, verbose,dry_run)

if __name__ == "__main__":
    args = parse_arguments()

    global logger  
    logger = logging_setup(args.logname)
        
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

    files = scan_directory(args.directory, args.verbose, args.dry_run, logfile=args.logname)
    if not args.dry_run:
        logger.info(f"Found {len(files)} files in {args.directory}")
    if args.verbose or args.dry_run:
        print(f"Found {len(files)} files to organize.")

    organize_files(files, args.dry_run, args.verbose)
    
