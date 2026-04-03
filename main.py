from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
import time
import socket
import psutil
import datetime

def get_internal_ip():
    """Get local IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))  
            return sock.getsockname()[0]   
    except OSError:
        return "NoNet"

def get_cpu_temp():
    """Get CPU temperature."""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read().strip()) / 1000.0  
            return f"{temp:.1f}°C"  
    except Exception:
        return "N/A"

LABEL_X = 1
VALUE_X = 45
LINE_HEIGHT = 12

def main():
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial, width=128, height=64)

    try:
        while True:
            now = datetime.datetime.now()
            top_line = f" {now.strftime('%Y-%m-%d %H:%M:%S')}"

            ip_address = get_internal_ip()
            cpu_usage = f"{psutil.cpu_percent(interval=0.5)}%"
            memory_usage = f"{psutil.virtual_memory().percent}%"
            cpu_temperature = get_cpu_temp()

            with canvas(device) as draw:
                draw.text((0, 0), top_line, fill="white")

                draw.text((LABEL_X, LINE_HEIGHT * 1), "IP:", fill="white")
                draw.text((VALUE_X, LINE_HEIGHT * 1), ip_address, fill="white")

                draw.text((LABEL_X, LINE_HEIGHT * 2), "CPU:", fill="white")
                draw.text((VALUE_X, LINE_HEIGHT * 2), cpu_usage, fill="white")

                draw.text((LABEL_X, LINE_HEIGHT * 3), "MEM:", fill="white")
                draw.text((VALUE_X, LINE_HEIGHT * 3), memory_usage, fill="white")

                draw.text((LABEL_X, LINE_HEIGHT * 4), "TEMP:", fill="white")
                draw.text((VALUE_X, LINE_HEIGHT * 4), cpu_temperature, fill="white")

            time.sleep(0.3)

    except KeyboardInterrupt:
        print("\nThe program has exited.")


if __name__ == "__main__":
    main()
