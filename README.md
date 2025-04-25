# port-scanner-using-socket
# 🔍 Port Scanner in Python

This is a simple **port scanner** written in Python using the built-in `socket` module. It allows users to scan a range of ports on a given target IP address to check which ports are open or closed.

---

## 📌 Features

- Scan a specific IP address  
- Define a custom port range  
- Fast scanning using a short timeout  
- User-friendly output with open/closed port status  

---

## 🧠 How It Works

1. The script takes an IP address and a range of ports from the user.  
2. It attempts to connect to each port in the specified range using TCP.  
3. If the connection is successful, the port is considered **open**.  
4. If the connection fails, the port is **closed**.  
5. Results are printed to the console.  

---

## ▶️ Usage

1. Save the script as `port_scanner.py`.  
2. Run the script using Python:
   ```bash
   python port_scanner.py
