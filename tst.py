from transformers import pipeline
generator = pipeline("text-generation", model="microsoft/Phi-3.5-mini-inst")

res = generator(
    "On the first day of Christmas, my true love gave to me",
    max_length = 30,
    num_return_sequences=1,
)
print(res)