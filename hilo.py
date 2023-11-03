import os
import threading

def imprimir_pid():
    pid = os.getpid()
    print(f"El PID de este proceso es: {pid}")

def main():
    # Crear un hilo y asignarle la función imprimir_pid
    thread = threading.Thread(target=imprimir_pid)
    
    # Iniciar el hilo
    thread.start()
    
    # Esperar a que el hilo termine (si es necesario)
    thread.join()

if __name__ == "__main__":
    pid = os.getpid()
    print(f"El PID de este proceso es: {pid}")
    main()
