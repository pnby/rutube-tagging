import asyncio

from app.api.llama.impl.llama import Llama


async def main():
    text = """
    Напиши рассказ про то как писали chat gpt. Рассказ должен быть на русском языке
    """
    llama = Llama(text)
    await llama.send_request()
    response = llama.get_formatted_response()

    print(response)

if __name__ == '__main__':
    asyncio.run(main())