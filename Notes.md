# Project Notes

## What I Learned

### Socket Programming

Used Python sockets to establish TCP connections and determine whether a port is open.

### connect_ex()

Returns:

* 0 → Port Open
* Non-zero → Port Closed or Unreachable

Unlike `connect()`, it does not raise an exception for closed ports.

### Multithreading

Multiple worker threads scan different ports simultaneously, significantly reducing scan time.

### Queue

A queue safely distributes ports among threads.

Benefits:

* No duplicate scanning
* Automatic work distribution
* Thread-safe task management

### Lock

A lock protects shared resources such as the `open_ports` list and scan counter from simultaneous modification.

### Service Detection

Known ports are mapped using `COMMON_PORTS` from `commonports.py`.

Unknown ports are resolved using `socket.getservbyport()` when available.

### JSON Report

Stores scan results in a structured format that can be consumed by other programs.

### TXT Report

Creates a readable report for users.

### Key Python Concepts

* Functions
* Dictionaries
* Lists
* Threading
* Queue
* Exception Handling
* File Handling
* JSON
