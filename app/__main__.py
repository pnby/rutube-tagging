from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cuda()
text = "Александр Сергеевич Пушкин родился в "
input_ids = tokenizer.encode(text, return_tensors="pt").cuda()
out = model.generate(input_ids.cuda())
generated_text = list(map(tokenizer.decode, out))[0]
print(generated_text)