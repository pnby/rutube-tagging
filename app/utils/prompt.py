from app import logger
from app.utils.settings import MODE

class Prompt:
    def __init__(self, text: str):
        """
        Initializes the Prompt class with the input text.

        Args:
            text (str): The input text to be processed.
        """
        self.text = text

    def get_system_prompt(self) -> str:
        """
        Generates the system prompt by loading a template and appending available tags.

        Returns:
            str: The system prompt with available tags.
        """
        # prompt = "Your task is to assign tags to the following text and return the response in JSON format without comments and explanations. The output of the tags must match the content of the text"
        # prompt += "\nResponse format: {'tags': [...]}"
        return None

    @staticmethod
    def get_tags() -> str:
        """
        Retrieves the available tags from a file.

        Returns:
            str: The available tags as a string.
        """
        if MODE == "DEV":
            path = "/prompts/available_tags.json"
        else:
            path = "../prompts/available_tags.json"

        with open(path, mode='r', encoding='utf-8') as f:
            tags = f.read()

        return tags

    def get_user_prompt(self) -> str:
        """
        Generates the user prompt for tagging the input text.

        Returns:
            str: The user prompt with the input text and expected response format.
        """
        text = {"target_text": f"{self.text}"}
        final_prompt = f"""
        Тебе нужно расскать что происходит в этом тексте
        \n{text}
        """
        return final_prompt
