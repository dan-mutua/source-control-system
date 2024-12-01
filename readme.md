# Simple Source Control System

## Overview

This is a lightweight, Python-based version control system designed to mimic basic Git functionalities. The project provides a simple command-line interface for managing source code repositories, tracking changes, and maintaining commit history.

## Features

- 🏗️ Repository Initialization
- 📁 File Staging
- 💾 Commit Management
- 📋 Commit History Tracking

## Prerequisites

- Python 3.8+
- No external dependencies required

## Installation

1. Clone the repository:
```bash
git clone
cd simple-source-system
```

2. Ensure you have Python installed:
```bash
python --version
```

## Usage

### Initialize a Repository

```bash
python main.py --init
```
Creates a new source control repository in the current directory.

### Stage Files

```bash
# Stage a single file
python main.py --stage filename.txt

# Stage multiple files by running the command for each
python main.py --stage file1.txt
python main.py --stage file2.txt
```

### Commit Changes

```bash
python main.py --commit "Your commit message here"
```
Commits all staged files with the specified message.

### View Commit History

```bash
# Show last 10 commits (default)
python main.py --history

# Show specific number of commits
python main.py --history --limit 5
```

## CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `--init` | Initialize a new repository | `python main.py --init` |
| `--stage <file>` | Stage a file for commit | `python main.py --stage README.md` |
| `--unstage <file>` | Unstage a previously staged file | `python main.py --unstage README.md` |
| `--commit "<message>"` | Commit staged files | `python main.py --commit "Add README"` |
| `--history` | View recent commits | `python main.py --history` |
| `--limit <number>` | Specify number of history entries | `python main.py --history --limit 5` |

## Project Structure

```
source_control/
├── main.py                 # Main CLI interface
└── srccontrol/
    ├── __init__.py         # Package initialization
    ├── repository.py       # Repository management
    ├── index.py            # Staging area management
    ├── commit.py           # Commit operations
    └── history.py          # Commit history tracking
```


## Limitations

- Does not support full Git functionality
- Basic commit and history tracking only
- No network/remote repository support
- Minimal branching capabilities

## Future Improvements

- [ ] Add branch management
- [ ] Implement merge functionality
- [ ] Create remote repository support
- [ ] Add more robust error handling

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - damutua15@gmail.com.com

