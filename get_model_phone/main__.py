import subprocess

def get_phone_model():
    # Reemplaza con la ruta completa a adb.exe
    adb_path = r"C:\Users\calde\AppData\Local\Android\Sdk\platform-tools\adb.exe"

    # Obtén la lista de dispositivos conectados
    devices = subprocess.check_output([adb_path, 'devices']).decode().splitlines()

    # Filtra las líneas que contienen los dispositivos conectados
    connected_devices = [line.split()[0] for line in devices if '\tdevice' in line]

    if not connected_devices:
        print("No hay dispositivos conectados.")
        return

    # Usa adb shell para obtener el modelo del dispositivo
    for device in connected_devices:
        try:
            model = subprocess.check_output([adb_path, '-s', device, 'shell', 'getprop', 'ro.product.model']).decode().strip()
            print(f"Dispositivo {device}: Modelo {model}")
        except subprocess.CalledProcessError:
            print(f"No se pudo obtener el modelo del dispositivo {device}.")

# Llama a la función para obtener el modelo del teléfono
get_phone_model()
