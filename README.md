# File Organizer

A Python utility to automatically organize files in a directory into categorized folders based on their file extensions. This tool is ideal for cleaning up messy folders, such as Downloads, project directories, or any location with mixed file types.

## Features

- **Automatic categorization:** Sorts files into folders like Images, Videos, Documents, Audio, Archives, Scripts, and Others.
- **Progress bar:** Visual feedback using [`alive-progress`](https://github.com/rsalmei/alive-progress).
- **Dry run mode:** Preview what will happen without making any changes.
- **Verbose mode:** Get detailed output of the organization process.
- **Logging:** All actions are logged to a file.
- **Customizable:** Easily add or modify file extension categories.

## Categories

Files are sorted into the following categories based on their extensions:

- **Images:** .jpg, .jpeg, .png, .gif, .bmp, .tiff
- **Videos:** .mp4, .avi, .mov, .mkv, .flv, .wmv
- **Documents:** .pdf, .docx, .txt, .xlsx, .pptx, .odt
- **Audio:** .mp3, .wav, .aac, .flac, .ogg, .m4a
- **Archives:** .zip, .rar, .tar, .gz, .7z
- **Scripts:** .py, .js, .sh, .bat, .pl, .rb
- **Others:** Any file not matching the above

## Installation

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd file_organizer
   ```

2. **(Recommended) Create a virtual environment:**

   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

```sh
python file_organizer.py <directory> [--verbose] [--dry-run] [--logname LOGFILE]
```

### Arguments

- `<directory>`: The path to the directory you want to organize.
- `--verbose` or `-v`: Enable detailed output.
- `--dry-run` or `-d`: Show what would happen, but do not move any files.
- `--logname` or `-l`: Specify the log file name (default: file_organizer.log).

### Example

Organize your Downloads folder with verbose output:

```sh
python file_organizer.py C:\Users\YourName\Downloads --verbose
```

Dry run (no changes made):

```sh
python file_organizer.py C:\Users\YourName\Downloads --dry-run
```

## Progress Bar

This script uses the [`alive-progress`](https://github.com/rsalmei/alive-progress) library to display a progress bar while organizing files.  
It is included in `requirements.txt`.

## Logging

All actions are logged to the specified log file (default: `file_organizer.log`).

## .gitignore

The following files and folders are ignored by git:

- `.venv/` (your virtual environment)
- `*.log` (all log files)

## License

MIT License

## Author

SOLO7899
