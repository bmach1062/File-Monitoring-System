import logging
import os
import hashlib
import sys
import time
import signal
# To install packages, do sudo apt python3-<package>
full_path = ""
file_hashes = {}

# Configure logging
logging.basicConfig(
    filename = './logs/file_changes.log', # Log file name
    level = logging.INFO,          # Log level of increasing order severity (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format = '%(asctime)s - %(levelname)s - %(message)s' # Log format
    # asctime adds timestamp of when log entry was created
    # levelname is the log level
    # message is the actual log message
)

# This is the specified directory to "monitored"
monitored_dir = "./monitored"

# For safety, make sure the "monitored" directory exists
if not os.path.exists(monitored_dir):
    os.mkdir("./monitored")
    # Create initial test files
    with open(os.path.join(monitored_dir, "example_file_1.txt"), "w") as f:
        f.write("This is a test file for monitoring.")
    with open(os.path.join(monitored_dir, "example_file_2.txt"), "w") as f:
        f.write("Another test file for monitoring.")

# # Traverse through the "monitored" directory
# # os.listdir returns a list of all the files and directories in the path
for file in os.listdir(monitored_dir):
    full_path = os.path.join(monitored_dir, file) # os.path.join combines directory paths and file names into a complete file path

# This function calculates the file's hash
def calculate_file_hash(file_path):
    try:
        with open(file_path, "rb") as file: # for rb, "r" means read mode and "b" is for binary mode (useful for reading non-text files like images)
            """hashlib.sha256() creates a new SHA256 hash object
            file.read() reads the entire file content as raw binary data
            hexdigest() converts the hash value into a readable hexadecimal string"""
            file_hash = hashlib.sha256(file.read()).hexdigest()
        return file_hash
    except Exception as e: # In case file access goes wrong
        logging.error(f"Error accessiong {file_path}: {e}")
        return None

# Signal handler for graceful exit
def signal_handler(sig, frame):
    """
    Handles termination signals (e.g., SIGINT or SIGTERM) to exit gracefully.
    """
    logging.info("Program terminated by user.")
    print("\nProgram terminated by user.")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signals

# This function detects file changes
def detect_file_changes(file_path):
    # Iterate over all entries in the "monitored" directory
    for file in os.listdir(monitored_dir):
        full_path = os.path.join(monitored_dir, file) # Get the full path of the file
        

        if os.path.isfile(full_path): # Check if it is a regular file
            file_hash = calculate_file_hash(full_path)
            file_hashes[file] = file_hash

    while True: 
        current_files = os.listdir(monitored_dir)

        # Detect added files
        for file in current_files:
            full_path = os.path.join(monitored_dir, file)

            # Check if the file is not already tracked in file_hashes
            if file not in file_hashes and os.path.isfile(full_path):
                logging.info(f"File added: {full_path}")

                # Calculate the hash of the newly added file and add it to the file_hashes dictionary
                # Allows for future monitoring for modifications to the new file
                file_hashes[file] = calculate_file_hash(full_path)

        # Detect deleted files
        for file in list(file_hashes.keys()): # Go through the current files in dictionary
            if file not in current_files: # Checks if file is not present
                logging.info(f"File deleted: {os.path.join(monitored_dir, file)}")
                del file_hashes[file] # Since file is no longer in the directory, we remove it from the dictionary


        # Detect modified files
        for file in current_files:
            full_path = os.path.join(monitored_dir, file)

            # Check if file is actually a file
            if os.path.isfile(full_path): 
                current_hash = calculate_file_hash(full_path) # Gets the hash of the file

                # If the file is recorded and it has a different hash than what is recorded, file has been modified
                if file in file_hashes and file_hashes[file] != current_hash:
                    logging.info(f"File modified: {full_path}")
                    file_hashes[file] = current_hash
        
        # Prevents unnecessary resource consumption
        time.sleep(1)

# Start monitoring
logging.info("Starting file monitoring...")
print("Monitoring files in the directory. Press Ctrl+C to exit.")
detect_file_changes(monitored_dir)