# CLI Expense Tracker

A lightweight, terminal-based Expense Tracker built from scratch using pure Python. This project focuses on strong object-oriented design patterns, dynamic command-line argument parsing, and structured data persistence without using heavy external database frameworks.

## 🚀 Key Features
- **Data Persistence:** Automatically tracks, loads, and saves expenses locally using a flat-file JSON structure.
- **Auto-Incrementing System:** Structurally tracks records using sequential custom IDs.
- **Flexible Data Filtering:** Supports interactive tracking to view transactions across independent monthly or category filters.
- **Robust Input Validation:** Gracefully handles invalid argument parameters and falls back safely to default operations instead of crashing.

## 🛠️ Concepts Applied
- **Object-Oriented Programming (OOP):** Separate models for individual `Expense` definitions and database orchestration workflows via an `ExpenseTracker` class.
- **CLI Subcommands:** Structured routing utilizing Python's native `argparse` library.
- **File Manipulation:** Safe runtime operations using Python's `json` and `os.path` systems.

## 📦 Installation & Setup

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/your-username/expense-tracker.git](https://github.com/your-username/expense-tracker.git)
   cd expense-tracker