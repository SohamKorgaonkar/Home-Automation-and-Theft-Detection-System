## Home Automation and Theft Detection System
The project consists of all things necessary to convert an ordinary home to a fully automated smart home with Google Assistant Integration and a Dashboard.  
The Project also has a Theft Detection Part which can sense movements and upload the pictures to a Cloud Server if any suspicious movement is detected.  
The Project makes use of Node-Red to create a Dashboard that runs on a Raspberry Pi. The Pi Server runs all the scripts and connects to the internet, while the NodMCUs connect to the Pi.  
The Codes for Raspberry Pi are made in python and NodeMCUs runs C++.

 - Automation Part 1: Handles web requests and controls other node mcus
 - Automation Part 2: Runs on Nodemcu to accept commands from Raspberry Pi
 - Theft Detection: Uses PIR to detect movement and clicks photo using Pi Camera
