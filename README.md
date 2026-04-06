# Raspberry Pi OLED Monitor

A lightweight single-file Raspberry Pi system information monitor for a SSD1306 I2C OLED display.

一款适用于 SSD1306 I2C OLED 显示屏的轻量级单文件树莓派系统信息监控。

## Features:
- Display local IP address
- CPU usage and temperature monitoring
- Memory usage monitoring
- Real-time clock

Supports multiple OLED resolutions:
- 128×64 
- 128×32 (only display CPU temperature)

## Hardware

- Raspberry Pi with I2C enabled
- SSD1306 OLED display (size: 128x64)

## Installation and Run
First, make sure that you have enabled I2C

```bash
python3 -m pip install -r requirements.txt
```

```bash
python3 oled_128x32.py
# or
python3 oled_128x64.py
```

## Notes

- This project was tested on the Raspberry Pi 4B with the Ubuntu system and may not behave the same on other systems.
