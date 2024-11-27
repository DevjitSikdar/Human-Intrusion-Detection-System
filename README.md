# Human-Intrusion-Detection-System
 Developed a real-time human intrusion detection system using OpenCV, MediaPipe, and cvzone to analyze camera feeds and detect unauthorized presence. Alerts are sent instantly via Twilio SMS API. Features include live monitoring, configurable detection parameters, and event logs, deployable with a Streamlit-based web interface for user interaction.

 # Human Intrusion Detection System  

A real-time human intrusion detection system built using **OpenCV**, **MediaPipe**, and **cvzone**, designed to detect unauthorized human presence in camera feeds and send instant alerts via **Twilio SMS API**.  

---

## Features  
- **Real-Time Detection**: Identifies human presence in live video feeds.  
- **Instant Alerts**: Sends SMS notifications upon detection.  
- **Streamlit Web Interface** (optional):  
  - Live video monitoring with bounding boxes.  
  - Configuration panel for sensitivity and detection zones.  
  - Logs with timestamps and snapshots of intrusions.  
- **Customizable**: Easily adaptable for various use cases like home security, office surveillance, etc.  

---

## Technologies Used  
- **OpenCV**: For image processing and real-time detection.  
- **MediaPipe**: For robust human pose detection.  
- **cvzone**: For easier visualization and integration.  
- **Twilio API**: For sending real-time SMS alerts.  
- **Streamlit** (optional): For building an interactive web interface.  

---

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/human-intrusion-detection.git  
   cd human-intrusion-detection  

