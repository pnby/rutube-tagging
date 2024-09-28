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
        final_prompt = "Ваша задача — присвоить теги следующему тексту и вернуть ответ в формате JSON без комментариев и объяснений. Выходные теги должны соответствовать содержанию текста."
        final_prompt += "\nФормат ответа: {'tags': [...]}"
        final_prompt += f"\nЦелевой текст: {self.text}"
        final_prompt += f"\nНабор тегов приведен здесь, обратите внимание: {self.get_tags()}"
        return final_prompt