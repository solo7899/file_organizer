import argparse
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description="Organize files into directories based on their extensions.")
    parser.add_argument("directory", type=str, help="The directory to organize files in.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output.")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Perform a dry run without making changes.")  
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
        
    if Path(args.directory).exists():
        pass
    if args.verbose:
        print(f"Organizing files in directory: {args.directory}")
    if args.dry_run:
        print("Dry run mode enabled. No changes will be made.")
    else:
        print("Files will be organized into directories based on their extensions.")
    # Here you would add the logic to organize files based on their extensions.

