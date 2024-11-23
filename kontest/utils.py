from django.conf import settings
from .language_support import RunCmdGenerator
import requests
import json
import time
import shutil
import pathlib


DFILES = pathlib.Path(settings.BASE_DIR / 'dfiles')

if not DFILES.exists():
    DFILES.mkdir(exist_ok=True)


class PaizaIO:
    api_key = "guest"
    headers = {}

    @staticmethod
    def send_request(code, language, stdin=None, options=None):
        if stdin is None:
            stdin = ""
        if options is None:
            options = {'memory_limit': 1024**2, 'cpu_time_limit': 2.0}

        data = {
            "api_key": PaizaIO.api_key,
            "source_code": code,
            "language": language,
            "input": stdin.replace('\r', ''),
            "options": options
        }

        response = requests.post("https://api.paiza.io/runners/create.json", data=data, headers=PaizaIO.headers)
        if response.status_code == 200:
            result = response.json()
            return result.get('id')
        return None

    @staticmethod
    def check_status(result_id: str):
        data = {
            "api_key": PaizaIO.api_key,
            "id": result_id
        }

        response = requests.get("https://api.paiza.io/runners/get_status", json=data, headers=PaizaIO.headers)
        if response.status_code == 200:
            result = response.json()
            return result.get('status')
        return None

    @staticmethod
    def terminal_output(result_id: str):
        data = {
            "api_key": PaizaIO.api_key,
            "id": result_id
        }

        response = requests.get("https://api.paiza.io/runners/get_details", json=data, headers=PaizaIO.headers)
        if response.status_code == 200:
            result = response.json()
            return {
                "stdout": result.get("stdout"),
                "time": result.get("time"),
                "memory": result.get("memory")
            }
        return None

class Code:
    def __init__(self, mid, inputs, outputs, code, language):
        self.mid = mid
        self.inputs = inputs
        self.outputs = outputs
        self.code = code
        self.language = language

    def precheck(self):
        first_input, first_output = self.inputs[0], self.outputs[0]

        output = self.send(first_input)
        if first_output == output:
            return "Correct code"
        elif output == "":
            return "Error code"
        else:
            return "Incorrect code"

    def check(self):
        # for index in range(len(self.inputs)):
        #     print("Print running test", index+1)
        #     file_input, file_output = self.inputs[index], self.outputs[index]
        #     output = self.send(file_input)
        #     print(output, index+1, "|", file_input, file_output)
        #     if output != file_output:
        #         return "Incorrect code"
        #     elif output == "":
        #         return "Error code"
        # return "Correct code"

        folder = DFILES / f"fl{self.mid}"
        folder.mkdir(exist_ok=True)
        script_file = str(folder / 'script.file')

        print(hasattr(RunCmdGenerator, self.language), self.language)
        if hasattr(RunCmdGenerator, self.language):
            try:
                with open(script_file, 'w') as file:
                    file.write(self.code)

                func = getattr(RunCmdGenerator, self.language)

                for index in range(len(self.inputs)):
                    file_input, file_output = self.inputs[index], self.outputs[index]
                    file_input = file_input.replace("\r", "")
                    output = func(script_file, file_input)

                    if output == "":
                        shutil.rmtree(str(folder))
                        print("Error code")
                        return "Error code"
                    elif output != file_output:
                        shutil.rmtree(str(folder))
                        print("Incorrect code")
                        return "Incorrect code"
                shutil.rmtree(str(folder))
                return "Correct code"
            except:
                shutil.rmtree(str(folder))
                return "Error code"
        shutil.rmtree(str(folder))

    def send(self, stdin):
        request_id = PaizaIO.send_request(self.code, self.language, stdin)
        while PaizaIO.check_status(request_id) != "completed":
            time.sleep(1)
        return PaizaIO.terminal_output(request_id).get("stdout").strip('\n').strip()

