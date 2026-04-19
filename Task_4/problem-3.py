def write_log(message):
    with open("log.txt", "a") as file:
        file.write(message + "\n")
def read_logs():
    try:
        with open("log.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        return "No logs found."
    
write_log("Start")
write_log("Error occurred")

read_logs()