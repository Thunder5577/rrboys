from openai import OpenAI

client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "honesty is the best"}
    ],
    n=3,
    temperature=1
)

for i in range(len(completion.choices)):
    print(completion.choices[i].message.content)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": "honesty is the best"}
    ],
    n=3,
    temperature=1
)

for i in range(len(completion.choices)):
    print(completion.choices[i].message.content)