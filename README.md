# Documentación de NetHunter

## Descripción
NetHunter es un script desarrollado en Python para escanear una red local utilizando el protocolo ARP (Protocolo de Resolución de Direcciones). Este script permite identificar los dispositivos conectados en una red, mostrando sus direcciones IP y MAC.


## Requisitos

1. **Python**: Asegúrate de tener instalada una versión reciente de Python (3.6 o superior).
2. **Scapy**: Una biblioteca de Python para el análisis y manipulación de paquetes de red.
3. **Npcap**: Un driver necesario para capturar y enviar paquetes en la capa 2 (enlace de datos) en sistemas Windows.

## Instalación

### Paso 1: Clonar el repositorio
Clona este repositorio en tu máquina local:
```bash
$ git clone https://github.com/tu_usuario/nethunter.git
$ cd nethunter
```

### Paso 2: Instalar las dependencias de Python
Ejecuta el siguiente comando para instalar las bibliotecas requeridas:
```bash
$ pip install -r requirements.txt
```

### Paso 3: Instalar Npcap
Si estás utilizando Windows, es necesario instalar Npcap:
1. Descarga Npcap desde [la página oficial](https://npcap.com/#download).
2. Durante la instalación, selecciona la opción **"WinPcap API compatibility"**.

## Uso

Ejecuta el script desde la terminal. Te pedirá ingresar el rango de IP de la red que deseas escanear (por ejemplo, `192.xxx.1.0/28`).

### Ejemplo de uso
```bash
$ python NetHunter.py
WARNING: No libpcap provider available! pcap won’t be used
Ingresa el rango de IP (e.g., 192.168.1.0/24): 192.168.1.0/24

Dispositivos encontrados:
-----------------------------------
IP: 192.168.1.1    MAC: 00:11:22:33:44:55
IP: 192.168.1.10   MAC: 66:77:88:99:AA:BB
```

## Cómo funciona

1. **Protocolo ARP**: El script utiliza paquetes ARP para identificar dispositivos en la red local.
2. **Scapy**: Genera paquetes ARP y los envía a cada IP dentro del rango especificado.
3. **Respuesta ARP**: Los dispositivos que responden son listados con sus direcciones IP y MAC.


## Notas

- Este script debe ejecutarse con privilegios de administrador para garantizar el acceso a las funciones de red necesarias.
- Asegúrate de que Npcap esté correctamente instalado y configurado en Windows.
- Scapy puede generar advertencias en sistemas Windows; esto no afecta el funcionamiento del script.

## Contribuciones
Si deseas contribuir al desarrollo de NetHunter, por favor abre un issue o envía un pull request. ¡Toda contribución es bienvenida!

## Licencia
Este proyecto está licenciado bajo la [MIT License](LICENSE).

