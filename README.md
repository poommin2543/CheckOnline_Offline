# CheckOnline Offline

## Overview
CheckOnline Offline is a Python script that allows users to test their internet connection speed, latency, jitter, and packet loss. This tool helps to monitor network performance by running multiple tests and displaying results in a tabulated format.

## Features
- Measures **download speed** and **upload speed** using `speedtest`.
- Calculates **latency (ping)** and **jitter** using `ping3`.
- Computes **packet loss percentage**.
- Runs **multiple tests** and calculates the **mean values** for better accuracy.

## Dependencies
This script requires the following Python libraries:
- `speedtest` (for speed measurement)
- `ping3` (for latency and packet loss measurement)
- `tabulate` (for formatting the output table)

Install them using pip:
```bash
pip install speedtest-cli ping3 tabulate
```

## How to Use
Run the script with Python:
```bash
python check_online.py
```
The script will run 10 tests, collecting download/upload speeds, latency, jitter, and packet loss. It will then display a tabulated result including mean values.

## Example Output
```
+---------+------------+-----------+---------+--------+-------------+
| Test No.| Download  | Upload    | Latency | Jitter | Packet Loss |
+---------+------------+-----------+---------+--------+-------------+
| 1       | 50.23 Mbps| 10.12 Mbps| 15.23 ms| 2.34 ms| 0.00 %      |
| 2       | 48.95 Mbps| 9.87 Mbps | 14.98 ms| 1.87 ms| 0.00 %      |
| ...     | ...       | ...       | ...     | ...    | ...         |
| Mean    | 49.10 Mbps| 9.95 Mbps | 15.12 ms| 2.10 ms| 0.00 %      |
+---------+------------+-----------+---------+--------+-------------+
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by [poommin2543](https://github.com/poommin2543)

