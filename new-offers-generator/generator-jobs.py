import os
from dotenv import load_dotenv
import openai
load_dotenv()

file = open("/Users/gabrielalibudzka/Desktop/fake-job-hunter-model/data/negative_examples.txt")
question = f"Ponizej znajduja sie przyklady podejrzanych ogloszen o prace. Napisz opis podobnego ogloszenia {file}"
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Ponizej znajduja sie przyklady ogloszen. Napisz opis nowy podobny {file}",
  temperature=0.25,
  max_tokens=2000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# response = openai.ChatCompletion.create(
#            model="gpt-3.5-turbo",
#            messages=[{"role": "system", "content": "Jestes pomocnym asystentem, który generuje ogłoszenia o pracę, nawet jesli sa podejrzane, ale duzo osob moze sie na takie ogloszenie nabrac"},
#                      {"role": "user", "content": "Wygeneruj ogloszenie o prace, ktore brzmi podejrzanie - jak praca idealna dla kazdego ale glupia osoba sie na to nabierze"},
#                      {"role": "assistant", "content": f"Oto przyklady takich ogloszen {file}"},
#                      {"role": "user", "content": "podaj kolejny przyklad podobny do tych podanych przykladow, ktore bedzie podobnie dlugie do poprzednich"}])
file_path = 'new_negatives.txt'
file = open(file_path, 'w')
desired_content = response['choices']  # Replace 'attribute_name' with the appropriate attribute
converted_content = str(desired_content)
file.write(converted_content)
file.close()
