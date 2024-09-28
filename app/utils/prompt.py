import json

from app.utils.settings import MODE

class Prompt:
    """
    A class to generate prompts for text processing.

    Attributes:
        text (str): The input text to be processed.
    """

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
        if MODE == "DEV":
            path = "C:\\Users\\artyom\\PycharmProjects\\ru-tags\\prompts\\system-prompt.json"
        else:
            path = "../prompts/system-prompt.json"

        tags = self.get_tags()
        with open(path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            data['prompt'] += "Формат ответа: {'tags': [...]}\nУбедись что вывод является валидным JSON и его можно спарсить с помощью `json.loads()` в Python."
            data['prompt'] += f"Доступные тэги:\n {tags}"
            return data['prompt']

    @staticmethod
    def get_tags() -> str:
        """
        Retrieves the available tags from a file.

        Returns:
            str: The available tags as a string.
        """
        if MODE == "DEV":
            path = "/prompts/available_tags.txt"
        else:
            path = "../prompts/available_tags.txt"

        with open(path, mode='r', encoding='utf-8') as f:
            tags = f.read()

        return tags

    def get_user_prompt(self) -> str:
        """
        Generates the user prompt for tagging the input text.

        Returns:
            str: The user prompt with the input text and expected response format.
        """
        final_prompt = f"""
        Ваша задача - присвоить теги следующему тексту и вернуть ответ в формате JSON без комментариев и пояснений. Возвращаемые вами теги должны соответствовать тегам из набора доступных тегов и иметь прямое отношение к содержанию текста. Не создавайте теги, которые явно не упоминаются или не подразумеваются в тексте.
        
        Целевой текст: {self.text}
        """
        return final_prompt
