# AQA Core: Voice Interaction Pipeline Skeleton
# Author: AQA Systems
# License: MIT

import asyncio
from transitions import Machine
from queue import Queue

class AQA_Core:
    states = ['idle', 'listening_command', 'processing_command', 'responding', 'awaiting_confirmation']

    def __init__(self):
        self.machine = Machine(model=self, states=AQA_Core.states, initial='idle')
        self.machine.add_transition('activate', 'idle', 'listening_command')
        self.machine.add_transition('command_received', 'listening_command', 'processing_command')
        self.machine.add_transition('response_generated', 'processing_command', 'responding')
        self.machine.add_transition('response_done', 'responding', 'idle')
        self.machine.add_transition('await_confirm', 'processing_command', 'awaiting_confirmation')
        self.machine.add_transition('confirm_received', 'awaiting_confirmation', 'responding')
        self.machine.add_transition('timeout_confirm', 'awaiting_confirmation', 'idle')

        self.asr_input_queue = asyncio.Queue()
        self.llm_input_queue = asyncio.Queue()
        self.tts_input_queue = asyncio.Queue()

    async def wake_word_listener(self):
        while True:
            await asyncio.sleep(2)
            print("[WakeWord] Listening...")
            if self.state == 'idle':
                self.activate()
                print(f"[WakeWord] Activated → {self.state}")
                await self.asr_input_queue.put("Check QNH")

    async def asr_processor(self):
        while True:
            audio_data = await self.asr_input_queue.get()
            print(f"[ASR] Input: {audio_data}")
            text = f"Recognized: {audio_data}"
            self.command_received()
            await self.llm_input_queue.put(text)
            self.asr_input_queue.task_done()

    async def llm_handler(self):
        while True:
            text = await self.llm_input_queue.get()
            print(f"[LLM] Processing: {text}")
            response = f"Set QNH 1013?"
            if "QNH" in text:
                self.await_confirm()
                await self.tts_input_queue.put(response)
            else:
                self.response_generated()
                await self.tts_input_queue.put("Roger that.")
            self.llm_input_queue.task_done()

    async def tts_player(self):
        while True:
            to_speak = await self.tts_input_queue.get()
            print(f"[TTS] Speaking: {to_speak}")
            await asyncio.sleep(len(to_speak) * 0.05)
            if self.state == 'awaiting_confirmation':
                print("[CONFIRM] Simulated: 'Affirm'")
                self.confirm_received()
                await self.tts_input_queue.put("QNH set.")
            else:
                self.response_done()
            self.tts_input_queue.task_done()

async def main():
    core = AQA_Core()
    await asyncio.gather(
        core.wake_word_listener(),
        core.asr_processor(),
        core.llm_handler(),
        core.tts_player()
    )

if __name__ == "__main__":
    asyncio.run(main())
