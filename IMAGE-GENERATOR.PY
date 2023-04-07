import openai

PROMPT = input('pls enter your prompt to create an image: ')
number_of_images = int(input('pls enter the number of images you want: '))

openai.api_key = "OPEN-AI-API-KEY"

response = openai.Image.create(
    prompt=PROMPT,
    n=number_of_images,
    size="1024x1024",
)

for i in range(number_of_images):
    print()
    print(f'image {i+1}: ')
    print()
    print(response["data"][i]['url'])
    i += 1
