import os
import subprocess
import requests

# 🔐 Hardcoded secret (will trigger secret scanning)
aws_secret_key = "AKIAIOSFODNN7EXAMPLE"

# 🚨 Insecure use of subprocess (Command Injection)
def run_command(user_input):
    command = "echo " + user_input
    subprocess.call(command, shell=True)  # CodeQL: subprocess-shell-injection

# 🚨 Insecure HTTP request (no SSL verification)
def fetch_data(url):
    response = requests.get(url, verify=False)  # CodeQL: request-without-ssl-verification
    return response.text

# 🚨 Potential Path Traversal
def read_user_file(filename):
    with open("/home/user/" + filename, "r") as f:
        return f.read()

# 🚨 SQL Injection example (if using a real DB)
def login(cursor, username, password):
    query = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    cursor.execute(query)  # CodeQL: sql-injection

if __name__ == "__main__":
    user_input = input("Enter something: ")
    run_command(user_input)

    data = fetch_data("http://example.com")
    print(data)

    file_content = read_user_file("../../../etc/passwd")
    print(file_content)
