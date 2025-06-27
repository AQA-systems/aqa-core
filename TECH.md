<p align="left">
  <img src="logo/aqa_logo.png" alt="AQA logo" width="200"/>
</p>


# Technical Architecture

This document outlines the core technical components, hardware options, and integration strategies of AQA — the Autonomous Flight Assistant.

---

## 🎛️ Core Modules

- **Speech Recognition (ASR)**: 
  - Local: Whisper (tiny/int8) or Vosk
  - Online fallback: OpenAI Whisper API or Gemini Audio

- **Language Model (LLM)**:
  - Quantized models (Gemma 2B, Mistral 7B Q4/5, Phi 3.5) via llama.cpp or ollama
  - On-device via Android, Raspberry Pi, or MacBook

- **Text-to-Speech (TTS)**:
  - Embedded: Piper, Silero, Coqui
  - Optional: cloud-based TTS for high fidelity

---

## 🧠 Behavior & Trigger Logic

- Passive always-listening loop
- Triggered by keywords or sensor thresholds
- Contextual filtering: no chit-chat, only flight-relevant feedback

---

## 🛰️ Input & Sensors

- GPS (UART / NMEA)
- IMU (MPU6050 / BNO085 / phone sensors)
- Altitude (barometric or GPS)
- Voltage / Fuel / Temp / RPM (via analog or digital sensors)
- Speech commands via audio input (intercom mic or PTT)

---

## 📦 Deployment Targets

- Android smartphone with model launcher app
- MacBook M1/M2 with local inference
- Raspberry Pi 5 with Coral/NPU optional
- ESP32 as I/O gateway for legacy sensors

---

## 🔈 Audio Integration

- Output to cockpit speaker or Bluetooth module
- Input via:
  - intercom mic (wired 3.5mm jack)
  - USB mic
  - ESP32-A2DP passthrough

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
- Hybrid with OpenAI API or Gemini
- Manual trigger via hardware button or PTT

---

## 📌 Notes

- AQA is not dependent on internet connectivity
- It is designed to operate under flight-safe conditions
- Architecture is modular and can be adapted for various platforms

> This file documents the technical direction of the project. For core vision, see `README.md`.
