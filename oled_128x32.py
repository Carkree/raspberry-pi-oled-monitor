import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

def get_cpu_temperature():
    """
    Get CPU temperature.
    """
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = float(f.read()) / 1000.0
        return temp
    except Exception as e:
        print(f"error: {e}")
        return 0.0

def main():
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial, width=128, height=32)

    # Load DejaVuSansMono font (which I think is good)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    font_size = 15
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Error: Unable to locate font file {font_path}")
        # Use default font
        font = ImageFont.load_default()

    try:
        while True:
            temp = get_cpu_temperature()
            
            msg = f"TEMP: {temp:.1f}°C"

            with canvas(device) as draw:
                draw.text((5, 8), msg, font=font, fill="white")

            time.sleep(1)

    except KeyboardInterrupt:
        device.cleanup()
        print("The program has exited.")

if __name__ == "__main__":
    main()
