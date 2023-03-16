import subprocess
import threading
import re
import os.path
from voice_bot.speech_text.interface import SpeechTextInterface
from voice_bot.console import console


class WhisperSpeechText(SpeechTextInterface):
    def __init__(self, device_index, process_sentence):
        self._command = None
        self._device_index = device_index
        self._process_sentence = process_sentence
        self.setup_whisper()

    def run(self) -> None:
        process = subprocess.Popen(
            self.command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        def stream_stdout(process, callback):
            transcription_pattern = re.compile(r"\[.*\]   (.*)")
            buffer = ""
            while True:
                output = process.stdout.read(1).decode("utf-8")
                if output == "" and process.poll() is not None:
                    break
                if output:
                    buffer += output
                    lines = buffer.split("\n")
                    for line in lines[:-1]:
                        match = transcription_pattern.match(line)
                        if match:
                            sentence = match.group(1).strip()
                            callback(sentence)
                    buffer = lines[-1]

        thread = threading.Thread(
            target=stream_stdout, args=(process, self._process_sentence)
        )
        thread.start()
        thread.join()

    def setup_whisper(self):
        whisper_setup_instructions = """Whisper is not set up. Please follow these steps to set it up:

1. Download the repo at https://github.com/ggerganov/whisper.cpp
2. Run `bash ./models/download-ggml-model.sh base.en`
3. Run `make stream`

Then the command to run is `./stream -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000`. 
"""

        if not os.path.exists("./stream"):
            console.print(
                "[bold yellow]Whisper is not set up on this system.[/bold yellow]"
            )

            # Prompt user if they want to set up Whisper
            console.print(
                "[bold yellow]Do you want to set it up now?[/bold yellow] (y/n)"
            )
            response = input()
            if response.lower() == "y":
                console.print("[bold]Setting up Whisper...[/bold]")

                # Clone whisper.cpp repo and download ggml-base.en.bin model
                try:
                    subprocess.run(
                        "git clone https://github.com/ggerganov/whisper.cpp.git",
                        check=True,
                        shell=True,
                    )
                    subprocess.run(
                        "cd whisper.cpp && bash ./models/download-ggml-model.sh base.en",
                        check=True,
                        shell=True,
                    )
                    console.print(
                        "[bold green]Whisper downloaded successfully![/bold green]"
                    )
                    subprocess.run("make stream", check=True, shell=True)
                    console.print(
                        "[bold green]Whisper set up successfully![/bold green]"
                    )
                except subprocess.CalledProcessError as e:
                    console.print(
                        f"[bold red]Error setting up Whisper: {e.stderr}[/bold red]"
                    )

            else:
                exit()

        # Set up command to run Whisper
        self.command = f"./stream -m ./whisper.cpp/models/ggml-base.en.bin -t 8 --step 500 --length 5000 --capture {self._device_index}"