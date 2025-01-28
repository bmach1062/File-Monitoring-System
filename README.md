# File-Monitoring-System

## Objective
This project aims to simulate monitoring a file directory for cases of added files, deleted files, and modified files. The primary focus was to implement a Python-based solution that utilizes hashing (SHA-256) for file integrity checks, logging to track changes in real-time, and signal handling for graceful termination. The system periodically scans a specified directory, detects changes efficiently, and logs them with timestamps for future reference, showcasing skills in automation, scripting, and error handling.

### Skills Learned
- Python
  - Writing efficient and modular scripts.
- File System Monitoring
  - Detecting file additions, deletions, and modifications. 
- Hashing and Integrity Checks
  - Using SHA-256 to ensure file integrity.
- Logging
  - Implementing structured logging to track events and changes.
- Signal Handling
  - Managing graceful program termination with system signals.
- Error Handling
  - Identifying and managing exceptions in file operations.
- Automation
  - Designing an automated system to monitor directories periodically.
- Resource Management
  - Optimizing performance with controlled scan intervals.
- Linux/Unix Tools
  - Testing and manipulating file directories in a Linux/Unix environment.
- Problem Solving
  - Addressing challenges in file access and handling concurrent changes. 

## Steps to Run Code
1. **Clone the Repository**  
   Run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/bmach1062/File-Monitoring-System.git
2. **Navigate to the IDS Directory**  
   Change into the project directory:
   ```bash
   cd File-Monitoring-System/IDS
2. **Run the Program**  
   Start monitoring the files from "monitored":
   ```bash
   python3 ids.py

![before ctrlc](https://github.com/bmach1062/File-Monitoring-System/blob/4477bc4ade034980aeeeb0368c0c2be60abb368c/before_ctrlc.png)
![program start](https://github.com/bmach1062/File-Monitoring-System/blob/4477bc4ade034980aeeeb0368c0c2be60abb368c/program_start.png)

* Please note that if you do not see changes to file_changes.log, you should either do ctrl+s to save MODIFIED changes or click on any other file and then click on the file_changes.log file again
## Added Files Scenario
- When you add a new file to the "monitored" directory, file_changes.log (under "logs" directory) will update and present a message about the newly added file.
![file added](https://github.com/bmach1062/File-Monitoring-System/blob/4477bc4ade034980aeeeb0368c0c2be60abb368c/after_file_added.png)
