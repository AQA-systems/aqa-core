# ✳️ External LLM Feedback — Insights and Strategy 

> ✈️ AQA – Your AI-Powered Co-Pilot  
> Navigate, manage checklists, and monitor vital flight data seamlessly — all with the power of your voice.

This file summarizes early conceptual feedback from external assistant systems regarding architecture and design decisions in the AQA project.

---

## 🔍 Wake Word Detection (WWD)

### 🧭 Direction:
Begin with lightweight, open-source wake word detection for prototyping. Transition to high-reliability models for deployment in embedded systems.

---

## 🧠 Local ASR / STT (Speech-to-Text)

### 🧭 Direction:
Use compact, locally-runnable speech recognition engines suitable for real-time onboard use. Prioritize quantized, efficient formats.

---

## 🔁 Voice Pipeline Architecture

### ✅ Consensus
- Use modular FSM loop with async behavior modeling
- Organize voice loop: Wake → Recognition → Processing → Speech Output
- Use queue structures for inter-process communication
- Manage context state for checklist confirmations

### 🧭 Our Choice:
> Modular FSM loop with async behavior modeling. Each module async. Start with simulation loop.

---

## 🔊 Local TTS

### 🧭 Direction:
Use lightweight, locally hosted text-to-speech engines with clear output suitable for noisy cabin environments. Optimize for low latency.

---

## 🧩 Local RAG (Retrieval-Augmented Generation)

### 🧭 Direction:
Support optional retrieval-augmented workflows through local vector databases and embedding models. Maintain modular design to allow extension.

---

## 📡 Communication Layer (Data ↔ System)

### ✅ Recommended
| Method    | Use Case                  | Notes                              |
|-----------|---------------------------|------------------------------------|
| UART      | Direct serial data stream | Low-latency, stable                |
| MQTT      | Structured telemetry      | Use local broker where applicable  |
| Wireless  | Peer-to-peer module link  | For internal lightweight transfer  |

### 🧭 Our Choice:
> MQTT for structured data → UART fallback for critical channels

---

## 📘 Summary of Actions

| Decision Area        | Direction                           |
|----------------------|--------------------------------------|
| Wake Word Detection  | Lightweight engine, scalable         |
| Recognition Engine   | Local, quantized STT module          |
| Processing Core      | Embedded intent inference logic      |
| FSM Loop             | Async FSM with modular coordination  |
| Speech Output        | Local TTS, optimized for clarity     |
| Retrieval Support    | Modular vector indexing (optional)   |
| Data Link            | UART / MQTT with fallback layering   |

---
