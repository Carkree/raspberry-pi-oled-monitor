# Raspberry Pi OLED Monitor

A lightweight single-file Raspberry Pi system information monitor for a 128x64 SSD1306 I2C OLED display.

一款适用于 128x64 SSD1306 I2C OLED 显示屏的轻量级单文件树莓派系统信息监控。

The script shows:
- Current date and time
- Local IP address
- CPU usage
- Memory usage
- CPU temperature

## Hardware

- Raspberry Pi with I2C enabled
- SSD1306 OLED display (size: 128x64)

## Installation and Run

```bash
python3 -m pip install -r requirements.txt
```

```bash
python3 main.py
```

## Notes

- If the network is unavailable, the IP field will show `NoNet`.
- If CPU temperature cannot be read, the temperature field will show `N/A`.
- This project is intended for Raspberry Pi and may not behave the same on non-Linux systems.
