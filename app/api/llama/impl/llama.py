from typing import override

import aiohttp

from app.api.llama.base_llama import BaseLlama
from app.constans import available_models


class Llama(BaseLlama):
    def __init__(self, prompt: str, model: available_models = "llama3:8b",
                 stream: bool = False, endpoint: str = "http://ollama:11434/api/generate"):
        """
        Initialize the Llama class.

        Args:
            prompt (str): The input prompt for the model.
            model (Literal["llama3:8b"], optional): The model to use. Defaults to "llama3:8b".
            stream (bool, optional): Whether to stream the response. Defaults to False.
            endpoint (str, optional): The API endpoint to send the request to. Defaults to "http://ollama:11434/api/generate".
        """
        super().__init__(prompt=prompt, model=model, stream=stream, endpoint=endpoint)

    @override
    async def send_request(self) -> None:
        """
        Send a request to the model.

        This method sends a POST request to the specified endpoint with the given prompt,
        model, and stream settings. The response is stored in self.response.
        """
        url = self.endpoint
        data = {
            "model": self.model,
            "prompt": self.prompt,
            "stream": self.stream,
            "options": {
                "temperature": 0.3
            },
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    self.response = result
                    print("Response from server:", result)
                else:
                    print(f"Error: {response.status}\n{await response.json()}")

    @override
    def get_formatted_response(self) -> str:
        """
        Get the formatted response from the model.

        This method formats the response stored in self.response and returns it as a string.

        Returns:
            str: The formatted response.
        """
        assert self.response is not None
        return self.response['response']
