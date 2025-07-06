# File Organizer

A simple Python script to organize files in a directory into categorized folders based on their file extensions. Useful for cleaning up messy download folders, project directories, or any location with mixed file types.

## Features

- Automatically sorts files into folders like Images, Videos, Documents, Audio, Archives, Scripts, and Others
- Supports dry run mode (see what would happen without making changes)
- Verbose mode for detailed output
- Logging to a file

## Categories

Files are sorted into the following categories based on their extensions:

- **Images:** .jpg, .jpeg, .png, .gif, .bmp, .tiff
- **Videos:** .mp4, .avi, .mov, .mkv, .flv, .wmv
- **Documents:** .pdf, .docx, .txt, .xlsx, .pptx, .odt
- **Audio:** .mp3, .wav, .aac, .flac, .ogg, .m4a
- **Archives:** .zip, .rar, .tar, .gz, .7z
- **Scripts:** .py, .js, .sh, .bat, .pl, .rb
- **Others:** Any file not matching the above

## Usage

### Requirements

- Python 3.7 or higher

### Running the Script

```sh
python file_organizer.py <directory> [--verbose] [--dry-run] [--logname LOGFILE]
```

#### Arguments

- `<directory>`: The path to the directory you want to organize.
- `--verbose` or `-v`: Enable detailed output.
- `--dry-run` or `-d`: Show what would happen, but do not move any files.
- `--logname` or `-l`: Specify the log file name (default: file_organizer.log).

#### Example

Organize your Downloads folder with verbose output:

```sh
python file_organizer.py C:\Users\YourName\Downloads --verbose
```

Dry run (no changes made):

```sh
python file_organizer.py C:\Users\YourName\Downloads --dry-run
```

## Logging

All actions (except in dry run mode) are logged to the specified log file.

## License

MIT License

## Author

Your Name
