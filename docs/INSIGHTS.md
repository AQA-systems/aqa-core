
# ✳️ External LLM Feedback — Insights and Strategy 

This file summarizes the feedback received from two advanced AI assistants — **Gemini** and **Perplexity** — regarding the architecture and technical decisions of the AQA project (Autonomous Quantum Assistant).

---

## 🔍 Wake Word Detection (WWD)

### ✅ Recommended
- **Porcupine** (Picovoice): high performance, low resource, ideal for final builds.
- **OpenWakeWord**: open-source, lighter, great for prototyping.
- **Silero VAD**: lightweight option for voice activity detection.

### 🧭 Our Choice:
> Start with **OpenWakeWord** for fast integration, then switch to **Porcupine** for stable deployment.

---

## 🧠 Local ASR / STT (Speech-to-Text)

### ✅ Recommended
- **Whisper.cpp** (tiny.en / base.en, quantized GGUF)
- **Vosk** (optional for embedded ASR)

### 🧭 Our Choice:
> Use `whisper.cpp` with `tiny.en` model for onboard transcription. Optimize later.

---

## 🔁 Voice Pipeline Architecture

### ✅ Consensus
- Use **asyncio**-based modular architecture with **Finite State Machine (FSM)**
- Organize voice loop: Wake → ASR → LLM → TTS
- Use `queue.Queue` or `asyncio.Queue` for inter-process communication
- Manage context state for checklist confirmations

### 🧭 Our Choice:
> FSM with `transitions` lib in Python. Each module async. Start with simulation loop.

---

## 🔊 Local TTS

### ✅ Recommended
- **Piper** — clear, lightweight, good voice
- **Coqui** — very natural, but heavier
- **eSpeak-ng** — fallback only (low quality)

### 🧭 Our Choice:
> Use `Piper` with voice `en_amy-low` (for cabin clarity). Optimize later if needed.

---

## 🧩 Local RAG (Retrieval-Augmented Generation)

### ✅ Recommended stack:
- Embedding model: `all-MiniLM-L6-v2` or `gte-small` (sentence-transformers)
- Vector DB: **FAISS**, **ChromaDB**, or **LanceDB**
- Framework: `LangChain` or `LlamaIndex`

### 🧭 Our Choice:
> Use FAISS + all-MiniLM-L6-v2, integrate into `llama_index`, test with checklists.

---

## 📡 Communication ESP32 ↔ Host

### ✅ Recommended
| Method    | Use Case                  | Notes                         |
|-----------|---------------------------|-------------------------------|
| UART      | Direct wired link         | Low-latency, stable            |
| MQTT      | Telemetry via Wi-Fi       | Use local broker (Mosquitto)  |
| ESP-NOW   | Peer-to-peer ESP comms    | Not suitable for SBC host     |

### 🧭 Our Choice:
> MQTT for structured data → UART fallback for critical channels

---

## 📘 Summary of Actions

| Decision Area        | Action                              |
|----------------------|--------------------------------------|
| Wake Word Detection  | Start OpenWakeWord, plan Porcupine  |
| ASR Engine           | Whisper.cpp tiny.en GGUF            |
| LLM Core             | Phi-3 or Gemma 2B (quantized)       |
| FSM Loop             | `asyncio` + `transitions`           |
| Local TTS            | Piper (Amy voice)                   |
| RAG Stack            | FAISS + MiniLM + Langchain          |
| ESP32 Link           | MQTT primary, UART fallback         |

---

