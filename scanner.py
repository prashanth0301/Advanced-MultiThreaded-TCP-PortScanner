import socket
import threading
import queue
import json
import time
import os

from datetime import datetime
from colorama import Fore, Style, init
from commonports import COMMON_PORTS

# ==========================
# Colorama Initialization
# ==========================

init(autoreset=True)

GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
RESET = Style.RESET_ALL

# ==========================
# Configuration
# ==========================

DEFAULT_TIMEOUT = 1
DEFAULT_THREADS = 100

# ==========================
# Global Variables
# ==========================

port_queue = queue.Queue()

open_ports = []

lock = threading.Lock()

scanned_ports = 0

def display_banner():

    print(CYAN + "=" * 70)
    print(CYAN + "      ADVANCED MULTITHREADED TCP PORT SCANNER")
    print(CYAN + "=" * 70)

    print(YELLOW + " Author  : Prashanth Reddy")
    print(YELLOW + " Version : 1.0")
    print(YELLOW + " Scan    : TCP Connect Scan")

    print(CYAN + "=" * 70)
    print()

def get_target():
    return input("Enter Target (IP / Hostname): ").strip()

def validate_target(target):

    try:
        return socket.gethostbyname(target)

    except socket.gaierror:
        return None
    
def get_service_name(port):

    service = COMMON_PORTS.get(port)

    if service:
        return service

    try:
        return socket.getservbyport(port)

    except OSError:
        return "Unknown"
    
def scan_port(target_ip, port):

    global scanned_ports

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(DEFAULT_TIMEOUT)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:

        with lock:

            open_ports.append({

                "port": port,

                "service": get_service_name(port)

            })

    scanner.close()

    with lock:

        scanned_ports += 1

        print(
            CYAN +
            f"\rScanned Ports : {scanned_ports}",
            end=""
        )

def worker(target_ip):

    while not port_queue.empty():

        port = port_queue.get()

        scan_port(target_ip, port)

        port_queue.task_done()

def get_scan_mode():

    print(CYAN + "\nSelect Scan Mode")
    print(YELLOW + "1. Common Ports")
    print(YELLOW + "2. Custom Port Range")

    while True:

        choice = input("Choice: ").strip()

        if choice in ("1", "2"):
            return choice

        print(RED + "Invalid choice! Try again.")

def get_port_range():

    while True:

        try:

            start_port = int(input("Enter Start Port : "))
            end_port = int(input("Enter End Port   : "))

            if 1 <= start_port <= 65535 and 1 <= end_port <= 65535:

                if start_port <= end_port:
                    return start_port, end_port

            print(RED + "Invalid Port Range!")

        except ValueError:

            print(RED + "Enter numbers only!")

def get_thread_count():

    user_input = input(
        f"Thread Count (Press Enter for {DEFAULT_THREADS}): "
    ).strip()

    if user_input == "":
        return DEFAULT_THREADS

    try:

        threads = int(user_input)

        if 1 <= threads <= 500:
            return threads

    except ValueError:
        pass

    print(YELLOW + "Invalid input. Using default thread count.")

    return DEFAULT_THREADS

def get_sorted_results():

    return sorted(
        open_ports,
        key=lambda x: x["port"]
    )

def display_results():

    print()

    print(CYAN + "=" * 60)
    print(CYAN + "SCAN RESULTS")
    print(CYAN + "=" * 60)

    if not open_ports:

        print(RED + "No Open Ports Found.")
        return

    print(
        YELLOW +
        f"{'PORT':<10}{'STATUS':<10}{'SERVICE'}"
    )

    print(CYAN + "-" * 60)

    for result in get_sorted_results():

        print(
            GREEN +
            f"{result['port']:<10}"
            f"{'OPEN':<10}"
            f"{result['service']}"
        )

    print(CYAN + "=" * 60)

def save_results(target, elapsed_time):

    os.makedirs("results", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"results/scan_{timestamp}.txt"

    with open(filename, "w") as file:

        file.write("=" * 60 + "\n")
        file.write("ADVANCED MULTITHREADED PORT SCANNER\n")
        file.write("=" * 60 + "\n")

        file.write(f"Target      : {target}\n")
        file.write(f"Scan Time   : {elapsed_time:.2f} seconds\n")
        file.write(f"Open Ports  : {len(open_ports)}\n\n")

        file.write(
            f"{'PORT':<10}{'STATUS':<10}{'SERVICE'}\n"
        )

        file.write("-" * 60 + "\n")

        for result in get_sorted_results():

            file.write(
                f"{result['port']:<10}"
                f"{'OPEN':<10}"
                f"{result['service']}\n"
            )

    print(GREEN + f"\nTXT Report Saved : {filename}")

def save_json(target, elapsed_time):

    os.makedirs("results", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"results/scan_{timestamp}.json"

    report = {

        "target": target,

        "scan_time": round(elapsed_time, 2),

        "total_open_ports": len(open_ports),

        "results": get_sorted_results()

    }

    with open(filename, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )

    print(GREEN + f"JSON Report Saved : {filename}")

def main():

    display_banner()

    target = get_target()

    ip = validate_target(target)

    if ip is None:

        print(RED + "Invalid Target.")
        return

    print(GREEN + f"Resolved IP : {ip}")

    scan_mode = get_scan_mode()

    thread_count = get_thread_count()

    if scan_mode == "1":

        for port in COMMON_PORTS:
            port_queue.put(port)

    else:

        start_port, end_port = get_port_range()

        for port in range(start_port, end_port + 1):
            port_queue.put(port)

    start_time = time.time()

    threads = []

    for _ in range(thread_count):

        thread = threading.Thread(
            target=worker,
            args=(ip,)
        )

        thread.start()

        threads.append(thread)

    port_queue.join()

    elapsed_time = time.time() - start_time

    display_results()

    print()

    print(CYAN + "=" * 60)
    print(GREEN + "SCAN COMPLETED")
    print(CYAN + "=" * 60)

    print(YELLOW + f"Target       : {target}")
    print(YELLOW + f"Open Ports   : {len(open_ports)}")
    print(YELLOW + f"Threads Used : {thread_count}")
    print(YELLOW + f"Time Taken   : {elapsed_time:.2f} seconds")

    print(CYAN + "=" * 60)

    save_results(target, elapsed_time)

    save_json(target, elapsed_time)

if __name__ == "__main__":
    main()
