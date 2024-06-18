import sounddevice as sd
import numpy as np
import time
import serial

com_num = input("Enter the COM port number: ")
ser = serial.Serial(port=f'COM{com_num}', baudrate=9600, timeout=1)

def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)
    volume_level = int(volume_norm)
    volume_level = max(2, min(10, volume_level))# Convert to integer
      # Clamp between 1 and 10
    ser.write(f"{volume_level}\n".encode())
    print(f"Volume Level: {volume_level}")
    # Read Arduino's response


# Use Voicemeeter Banana to combine cable input and audio output so that cable output can be used as the input device
input_device = "CABLE Output (VB-Audio Virtual , MME"  # Adjust this to match your setup

with sd.InputStream(device=input_device, callback=audio_callback):
    try:
        while True:
            time.sleep(1000)  # Check every second
    except KeyboardInterrupt:
        print("Recording stopped by user.")


