import sounddevice as sd
import numpy as np
import time
import serial
import matplotlib.pyplot as plt
import pyaudio



com_num = input("Enter the COM port number: ")
ser = serial.Serial(port=f'COM{com_num}', baudrate=9600, timeout=None)

def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)
    volume_level = int(volume_norm)  # Convert to integer
    volume_level = max(1, min(10, volume_level))  # Clamp between 1 and 10
    print(f"Volume Level: {volume_level}")

# Use Voicemeeter Banana as the input device
input_device = "CABLE Output (VB-Audio Virtual , MME"  # Adjust this to match your setup

with sd.InputStream(device=input_device, callback=audio_callback):
    try:
        while True:
            sd.sleep(1000)  # Check every second
    except KeyboardInterrupt:
        print("Recording stopped by user.")








