import socket
from colored import fg

# Cores
main = fg("blue")
open_color = fg("green")
closed_color = fg("red")

# ASCII Art
print(
    main
    + r"""  
  ____        _   _                   _   _                       
 |  _ \ _   _| |_| |__   ___  _ __   | \ | |_ __ ___   __ _ _ __  
 | |_) | | | | __| '_ \ / _ \| '_ \  |  \| | '_ ` _ \ / _` | '_ \ 
 |  __/| |_| | |_| | | | (_) | | | | | |\  | | | | | | (_| | |_) |
 |_|    \__, |\__|_| |_|\___/|_| |_| |_| \_|_| |_| |_|\__,_| .__/ 
        |___/                                              |_|    
"""
)

print(main + "Coded by shawty1 (github.com/sh4wty1)\n")

# Entrada do usuário
target = input("URL or IP: ")
print(
    "\nTimeout é o tempo de resposta da URL/IP. Quanto maior, mais preciso (mas mais demorado)."
)
timeout = float(input("Set timeout (ex: 0.1, 0.2...) => "))

# Lê as portas do arquivo txt
with open("ports.txt", "r") as file:
    ports = [int(line.strip()) for line in file if line.strip().isdigit()]

# Scan
for port in ports:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        code = client.connect_ex((target, port))
        if code == 0:
            print(open_color + "#######")
            print(open_color + f"OPEN {port}")
            print(open_color + "#######")
        else:
            print(closed_color + f"CLOSED {port}")
        client.close()
    except Exception as e:
        print(f"[!] Erro ao escanear a porta {port}: {e}")
