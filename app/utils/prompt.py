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
        text = {"target_text": f"""
        Business and sports share many commonalities that often go unnoticed. Both require strategic planning, discipline, and a relentless pursuit of excellence. In the world of business, success is measured by profitability, market share, and customer satisfaction. Similarly, in sports, success is gauged by wins, championships, and fan support. Both arenas demand a high level of competition, where only the best survive and thrive.

The parallels between business and sports are evident in the way they operate. Both require a clear vision and well-defined goals. In business, this might be a five-year plan with specific milestones, while in sports, it could be a seasonal strategy aimed at winning a championship. Both need effective leadership to guide teams towards these goals. CEOs and coaches play crucial roles in motivating their teams, making tough decisions, and ensuring everyone is aligned with the overall vision.

Teamwork is another critical aspect shared by business and sports. In a corporate setting, departments must collaborate to achieve common objectives. Similarly, in sports, players must work together, leveraging each other's strengths to win games. Communication, trust, and mutual respect are essential for both business teams and sports teams to function effectively.

Adaptability is another key trait required in both fields. Businesses must adapt to changing market conditions, technological advancements, and consumer preferences. Similarly, sports teams must adjust their strategies based on the strengths and weaknesses of their opponents, as well as changes in rules and regulations. The ability to pivot and adapt quickly can often determine success or failure in both arenas.

Risk management is also a common theme. Businesses must navigate financial risks, market volatility, and regulatory challenges. In sports, teams must manage the risk of injuries, player performance fluctuations, and strategic missteps. Effective risk management involves identifying potential threats, assessing their impact, and developing contingency plans.

Finally, both business and sports require continuous improvement and innovation. In business, this might involve developing new products, improving customer service, or adopting cutting-edge technologies. In sports, it could mean refining training methods, adopting new strategies, or leveraging data analytics to gain a competitive edge. The drive to constantly improve and innovate is what keeps both businesses and sports teams at the top of their game.

In conclusion, the worlds of business and sports are more alike than they might initially seem. Both demand strategic thinking, teamwork, adaptability, risk management, and a commitment to continuous improvement. Understanding these parallels can provide valuable insights for leaders in both fields, helping them to achieve greater success and sustainability.
"""}
        final_prompt = f"""
        Тебе нужно расскать что происходит в этом тексте
        \n{text}
        """
        return final_prompt
