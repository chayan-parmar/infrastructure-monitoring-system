import psutil
import socket
import requests
from datetime import datetime

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print(f"CPU Usage: {cpu}%")
print(f"RAM Usage: {ram}%")
print(f"Disk Usage: {disk}%")

if cpu > 80:
    print("ALERT: High CPU Usage!")

if ram > 80:
    print("ALERT: High Memory Usage!")

if disk > 90:
    print("ALERT: Low Disk Space!")

try:
    socket.create_connection(("google.com", 80), timeout=5)
    print("Network Status: Connected")
except:
    print("ALERT: Network Disconnected!")

try:
    response = requests.get("https://google.com")

    if response.status_code == 200:
        print("Website Status: UP")
    else:
        print("Website Status: DOWN")

except:
    print("Website Status: DOWN")

with open("system.log", "a") as f:
    f.write(f"\n{datetime.now()}\n")
    f.write(f"CPU: {cpu}%\n")
    f.write(f"RAM: {ram}%\n")
    f.write(f"Disk: {disk}%\n")
