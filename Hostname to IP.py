import socket

def get_ip(hostname):
  try:
    ip = socket.gethostbyname(hostname)
    return ip
  except socket.error as e:
    print(f"Error resolving hostname: {e}")
    return None

hostname = "google.com"
ip = get_ip(hostname)
if ip:
  print(f"IP address of {hostname} is {ip}")
