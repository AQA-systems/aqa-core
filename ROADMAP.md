
<p align="left">
  <img src="logo/aqa_logo.png" alt="AQA logo" width="200"/>
</p>

# AQA Project Roadmap 

## Phase I: Core System Architecture
- Voice interface (Whisper / Speech-to-Text)
- Text generation module (LLM)
- TTS (Text-to-Speech) with confirmation logic
- Modular ESP32 data endpoints (sensors, GPS)
- UART / MQTT / ESP-NOW communication bridge

## Phase II: Sensor Integration
- BME280 / BMP280 barometric input
- GPS NMEA stream parsing
- Heading sensor (BNO085)
- Altitude calculation with QNH support
- Real-time annunciator output

## ✅ Voice Confirmation Layer (VCL)
- No parameter is applied without pilot confirmation
- Example flow:
  1. Whisper detects "QNH 1015"
  2. AQA: "Confirm: set QNH 1015?"
  3. Pilot: "Affirm"
  4. AQA applies and announces confirmation
- Applies to QNH, radio freq, autopilot modes, checklists, heading/course

## 🧠 Smart Passive Watch Mode (SPWM)
- Continuous passive listening (Whisper + VAD)
- Contextual interpretation of speech (NLP filter)
- Wait-for-silence before intervention (~2.5 sec delay)
- Gentle confirm: "Confirm QNH 1015 to all instruments?"
- If pilot says "No, already set" — system acknowledges silently
- Cross-check against sensor readings (e.g. QNH set ≠ QNH heard)
- Optional alert if discrepancy detected

## Phase IV: Networked Integration
- Inter-device QNH synchronization
- Multi-display redundancy with shared data pool
- Remote voice control with fallback modes

## Phase V: AI Personality Layer (Experimental)
- Long-term memory per flight
- Context-aware behavior (fatigue, workload, emergencies)
- Flight plan memory and voice updates
- Integration with ATPL material & emergency logic

## ✈️ Flight Phase Awareness (FPA)
- Real-time detection of flight phase (Taxi, Takeoff, Climb, Cruise, Descent, Approach, Landing)
- Contextual behavior: silence when not needed, suggestions when required
- Adaptive checklist triggering based on phase
- Voice alerts for transition altitudes, flap settings, gear states, etc.

## 👨‍✈️ Virtual FO Logic (VFO)
- Voice-based execution of standard operating procedures (SOP)
- Example: "Set flaps 5" → "Flaps 5 set."
- Checklist execution and confirmation
- Callouts and readbacks consistent with two-crew operations

## 🧪 Anomaly Detection & Gentle Alerts (ADGA)
- Logical consistency checks across systems:
  - FL370 set, but QNH = 980 → mismatch
  - Descend clearance received, no vertical movement
  - Gear not retracted after takeoff
- Gentle reminders: "Check gear", "Altimeter still set to 1013", etc.
- Operates passively with override capability
