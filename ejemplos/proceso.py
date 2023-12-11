import os
import multiprocessing

def imprimir_pid():
    pid = os.getpid()
    print(f"Soy el proceso hijo: {pid}")

def main():
    # Crear un proceso y asignarle la función imprimir_pid
    proceso = multiprocessing.Process(target=imprimir_pid)
    
    # Iniciar el proceso
    proceso.start()
    
    # Esperar a que el proceso termine (si es necesario)
    proceso.join()

if __name__ == "__main__":
    pid = os.getpid()
    print(f"Soy el proceso padre: {pid}")
    main() 
    print("hola")
