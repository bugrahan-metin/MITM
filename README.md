# Man-in-the-Middle (MITM) Application

This is a simple Man-in-the-Middle (MITM) application. It is easy to use, and by following the steps below, you can intercept traffic between a target system and its network.

## **Features**
- Easily select a target device on the local network.
- Get between the modem and the target device.

---

## **How to Use**

1. **Connect to the Same Network**  
   Ensure that your computer, the target computer, and the modem are all connected to the same local network.

2. **Information You Need:**  
   - **Target Computer's IP Address:** The IP address of the device you want to intercept traffic from.  
   - **Modem's IP Address:** The IP address of the default gateway (modem).

3. **Run the Program:**  
   Execute the program with the following parameters:
   ```bash
   python arp_poising.py -t <Target_IP> -g <Modem_IP>
4. ** For Example **
   ```bash
   python arp_poising.py -t 192.168.1.10 -g 192.168.1.1

## Notes
- Before running the application, ensure all necessary Python libraries are installed.
  you need the scapy library for network analysis:
  ```bash
   pip install scapy

- This application is intended for educational purposes only. Any unauthorized use is strictly prohibited.






