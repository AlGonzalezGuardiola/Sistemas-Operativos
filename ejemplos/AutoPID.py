import os

def imprimir_pid():
    pid = os.getpid()
    print(f"El PID de este proceso es: {pid}")

if __name__ == "__main__":
    imprimir_pid()
