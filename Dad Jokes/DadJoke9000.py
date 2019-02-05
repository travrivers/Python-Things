from colorama import init
import requests
from random import choice
import pyfiglet
from termcolor import colored
init()

header = pyfiglet.figlet_format("DAD JOKE 9000")
color_header = colored(header, color="red")
print(color_header)

url = 'https://icanhazdadjoke.com/search'

topic = input("I got jokes son! Give me a topic:\n")
response = requests.get(
	url, 
	headers={"Accept":"application/json"},
	params={"term": topic,
	}
	)

result = response.json()
jk = result['results']
num_jokes = result['total_jokes']

if num_jokes > 1:
		print(f"I've got {result['total_jokes']}  jokes about {topic}.  Here you go: \n")
		print(choice(jk)['joke'])
elif num_jokes == 1:
	print(f"I've got one joke about {topic}.  Here it is: \n")
	print(jk[0]['joke'])
else:
	print(f'My bad, I have no jokes about {topic}.')


