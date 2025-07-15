# System Monitoring Script with Email Alerts

A Python script that monitors system resources (CPU, Memory, Disk) and sends email alerts when usage exceeds specified thresholds.

---

## Features

- Monitors CPU, Memory, and Disk usage using the `psutil` library.
- Sends email notifications via Gmail SMTP when thresholds are crossed.
- Easy to configure resource thresholds and email credentials.
- Can be scheduled to run automatically using cron or Task Scheduler.

---

## Requirements

- Python 3.x
- `psutil` library
- Gmail account with App Password enabled for SMTP

---

## Installation

1. Clone this repository:
2. install dependencies - pip install psutil

## setup 

Generate a Gmail App Password:

    Go to your Google Account > Security > App passwords.

    Create an app password for “Mail” and your device.

Update the script (system_monitor.py) with your email details and thresholds.

## Usage

run script manually..