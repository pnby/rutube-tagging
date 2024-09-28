import json

from app.utils.settings import MODE


class Prompt:
    def __init__(self, text: str):
        self.text = text


    def get_system_prompt(self) -> str:
        if MODE == "DEV":
            path = "C:\\Users\\artyom\\PycharmProjects\\ru-tags\\prompts\\system-prompt.json"
        else:
            path = "../prompts/system-prompt.json"

        tags = self.get_tags()
        with open(path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            data['prompt'] += f"Доступный набор тэгов:\n {tags}"
            return data['prompt']


    @staticmethod
    def get_tags() -> str:
        if MODE == "DEV":
            path = "/prompts/available_tags.txt"
        else:
            path = "../prompts/available_tags.txt"

        with open(path, mode='r', encoding='utf-8') as f:
            tags = f.read()

        return tags


    def get_user_prompt(self) -> str:
        final_prompt = f"""
        Твоя задача - присвоить следующему тексту тэги и вернуть ответ в формате JSON без комментариев и объяснений.

        Целевой текст: {self.text}

        """ + "\nФормат ответа: {'tags': [...]}"
        return final_prompt



obj = Prompt("1")
print(obj.get_system_prompt())