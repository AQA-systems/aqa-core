<p align="left">
  <img src="logo/aqa_logo.png" alt="AQA logo" width="200"/>
</p>


# Technical Architecture

This document outlines the core technical components, hardware options, and integration strategies of AQA — the Autonomous Flight Assistant.

---

## 🎛️ Core Modules

- **Speech Recognition**:  
  - Local speech engine for onboard voice input processing  
  - Optional fallback layer for external transcription sources

- **Language Understanding**:  
  - Embedded language inference module for intent detection  
  - Supports multiple device architectures and resource profiles

- **Voice Output**:  
  - Local text-to-speech engine for cockpit-grade voice feedback  
  - Optional external speech backend for extended fidelity (if needed)

---

## 🧠 Behavior & Trigger Logic

- Passive always-listening loop
- Triggered by keywords or sensor thresholds
- Contextual filtering: no chit-chat, only flight-relevant feedback

---

## 🛰️ Input & Sensors

- Navigation data from standard interfaces (e.g., NMEA)
- Inertial and motion input from onboard sensors
- Altitude sources via pressure or positional channels
- System status (voltage, fuel, RPM, temperature) via analog/digital signals
- Speech commands via audio input (intercom mic or PTT)

---

## 📦 Deployment Targets

- Mobile and desktop devices with embedded inference support
- Modular I/O gateways for legacy or discrete sensors

---

## 🔈 Audio Integration

- Output to cockpit speaker or Bluetooth module
- Input via:
  - intercom mic (wired 3.5mm jack)
  - USB mic
  - Optional wireless audio passthrough via low-latency channel

---

## 📂 Storage & Memory Extension (optional)

- Indexed RAQ (Retrieval-Augmented Query)
- PDF checklists, AFM, ATPL documents
- Navigation databases (open data or custom)

---

## 🔧 Maintenance & Debug

- Local terminal over USB / UART
- Debug dashboard (web-based or serial)
- Log output configurable

---

## ⚙️ Optional Modes

- Offline-only mode for full autonomy
- Hybrid mode supporting optional external inference sources
- Manual trigger via hardware button or PTT

---

## 📌 Notes

- AQA is not dependent on internet connectivity
- It is designed to operate under flight-safe conditions
- Architecture is modular and can be adapted for various platforms

> This file documents the technical direction of the project. For core vision, see `README.md`.
