import os
import subprocess
import requests
import sqlite3

# --- 🚨 Hardcoded Secret (Triggers Secret Scanning) ---
aws_access_key = "AKIAIOSFODNN7EXAMPLE"
aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# --- 🚨 Subprocess Shell Injection (CodeQL) ---
def run_unsafe_command(user_input):
    command = "ls " + user_input
    subprocess.call(command, shell=True)  # Vulnerability: subprocess-shell-injection

# --- 🚨 Insecure HTTP Request (CodeQL) ---
def fetch_data_insecure(url):
    response = requests.get(url, verify=False)  # Vulnerability: SSL verification disabled
    return response.text

# --- 🚨 Path Traversal (CodeQL) ---
def read_file_unsafe(filename):
    file_path = "/tmp/" + filename
    with open(file_path, "r") as f:
        return f.read()

# --- 🚨 SQL Injection (CodeQL) ---
def login_unsafe(db_conn, username, password):
    cursor = db_conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)  # Vulnerability: SQL injection
    return cursor.fetchall()

# --- Main Logic ---
if __name__ == "__main__":
    user_input = input("Enter directory name: ")
    run_unsafe_command(user_input)

    try:
        print(fetch_data_insecure("http://example.com"))
    except Exception as e:
        print(f"Error fetching data: {e}")

    try:
        print(read_file_unsafe("../../etc/passwd"))
    except Exception as e:
        print(f"Error reading file: {e}")

    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE users (username TEXT, password TEXT);")
    conn.execute("INSERT INTO users VALUES ('admin', 'admin123');")
    
    try:
        users = login_unsafe(conn, "admin", "admin123")
        print(f"Logged in: {users}")
    except Exception as e:
        print(f"Login error: {e}")
