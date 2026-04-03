# Raspberry Pi OLED Monitor

A lightweight single-file Raspberry Pi system information monitor for a 128x64 SSD1306 I2C OLED display.
一款适用于 128x64 SSD1306 I2C OLED 显示屏的轻量级单文件树莓派系统信息监控。

The script shows:
- Current date and time
- Local IP address
- CPU usage
- Memory usage
- CPU temperature

该脚本显示：
- 当前日期和时间
- 当地 IP 地址
- CPU 使用率
- 内存使用率
- CPU 温度

## Hardware

- Raspberry Pi with I2C enabled
- SSD1306 OLED display (size: 128x64)

- 启用了 I2C 功能的树莓派
- SSD1306 OLED 显示屏（尺寸：128x64）

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

- 如果网络不可用，IP 字段将显示“NoNet”。
- 如果无法读取 CPU 温度，温度字段将显示“N/A”。
- 本项目专为树莓派设计，可能在非 Linux 系统上运行效果不同。
