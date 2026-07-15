# Advanced Multithreaded TCP Port Scanner

## Overview

Advanced Multithreaded TCP Port Scanner is a Python networking project that scans TCP ports on a target host using multiple threads. It supports scanning common ports or a custom port range and generates reports in both TXT and JSON formats.

This project was developed to strengthen networking, socket programming, multithreading, and Python programming skills.

---

## Features

* Multithreaded TCP Port Scanning
* Common Ports Scan Mode
* Custom Port Range Scan
* Service Detection
* Thread-safe Queue Implementation
* JSON Report Generation
* TXT Report Generation
* Timestamped Report Files
* Colored Terminal Output using Colorama
* Sorted Scan Results

---

## Technologies Used

* Python 3
* Socket Programming
* Threading
* Queue
* Colorama
* JSON
* File Handling

---

## Project Structure

```text
Advanced-Multithreaded-Port-Scanner/
│
├── scanner.py
├── commonports.py
├── README.md
├── notes.md
├── interview_questions.md
├── architecture.txt
├── requirements.txt
├── CHANGELOG.md
├── .gitignore
├── assets/
└── results/
```

---

## Installation

Clone the repository.

Install the required package.

```bash
pip install -r requirements.txt
```

---

## Usage

Run the scanner.

```bash
python scanner.py
```

Select:

* Common Ports Scan
* Custom Port Range Scan

Enter the required details.

After completion, the generated reports are stored inside the `results` folder.

---

## Sample Output

```text
============================================================
SCAN RESULTS
============================================================

PORT      STATUS      SERVICE

22        OPEN        SSH
80        OPEN        HTTP
443       OPEN        HTTPS
```

---

## Skills Demonstrated

* Python Programming
* Socket Programming
* TCP Networking
* Multithreading
* Queue-based Task Scheduling
* Thread Synchronization
* Report Generation
* JSON Processing
* File Handling

---

## Future Improvements

* Banner Grabbing
* OS Detection
* UDP Port Scanning
* Progress Bar
* CSV Export
* GUI Version

---

## Author

Y. Prashanth Kumar Reddy
