from ai71 import AI71 

AI71_API_KEY = "api71-api-5bccbff2-dede-4274-8470-ca8dbcd1e5d1"

for chunk in AI71(AI71_API_KEY).chat.completions.create(
    model="tiiuae/falcon-180b-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
    stream=True,
):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, sep="", end="", flush=True)