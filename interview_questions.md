# Interview Questions

## Why did you use multithreading?

To scan multiple ports concurrently, reducing total scan time.

---

## Why use Queue?

Queue safely distributes ports among worker threads and prevents duplicate work.

---

## Why use Lock?

To protect shared resources from race conditions when multiple threads update them.

---

## Why use connect_ex() instead of connect()?

`connect_ex()` returns an error code instead of raising an exception, making it easier to check whether a port is open.

---

## Why save reports as JSON?

JSON is structured and machine-readable, making it suitable for automation and integration with other tools.

---

## What is socket.getservbyport()?

It returns the standard service name associated with a TCP port.

---

## Difference between Thread and Process?

Threads share the same memory within a process, while processes have separate memory spaces.

---

## Why sort results before displaying them?

Threads complete at different times, so sorting produces consistent and readable output.

---

## Why use functions?

Functions improve readability, modularity, reuse, and maintenance.

---

## One improvement you would add?

Banner grabbing, UDP scanning, service version detection, CSV export, and a GUI.
