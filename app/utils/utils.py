from transformers import GPT2LMHeadModel, GPT2Tokenizer


def generate_text(prompt, model_name="sberbank-ai/rugpt3large_based_on_gpt2", max_length=100, num_return_sequences=1):
    """
    Функция для генерации текста с помощью модели ruGPT3.

    :param prompt: Строка с текстом (промт), который необходимо продолжить
    :param model_name: Название модели в Hugging Face (по умолчанию ruGPT3Small)
    :param max_length: Максимальная длина сгенерированного текста
    :param num_return_sequences: Количество вариантов сгенерированного текста
    :return: Сгенерированные тексты
    """
    # Загрузка модели и токенизатора
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Токенизация промта
    inputs = tokenizer(prompt, return_tensors="pt")

    # Генерация текста
    outputs = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=2,  # избегать повторяющихся фраз
        do_sample=True,  # включить семплирование для большей вариативности
        top_k=50,  # рассматривать топ-50 вариантов для каждого шага генерации
        top_p=0.95,  # использовать метод nucleus sampling (когда сумма вероятностей >= 0.95)
        temperature=0.7  # параметр для управления разнообразием генерации
    )

    # Декодирование сгенерированного текста
    generated_texts = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

    return generated_texts


prompt = "У меня есть такой набор строк. sad das gk ddd, сформируй из него JSON"
generated_text = generate_text(prompt, max_length=150, num_return_sequences=2)

for i, text in enumerate(generated_text, 1):
    print(f"Вариант {i}:\n{text}\n")
