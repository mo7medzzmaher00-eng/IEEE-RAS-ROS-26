import platform
from datetime import datetime

def log_system_info():
    with open("sys_log.txt", "a") as file:
        os_type = platform.system()
        current_time = datetime.now()

        file.write(f"OS: {os_type} | Time: {current_time}\n")

def main():
    log_system_info()

if __name__ == "__main__":
    main()