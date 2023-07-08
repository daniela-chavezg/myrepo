import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges = response.json()
# print(challenges)

def calculate(num1, num2, operand):
    result = 0
    if(operand == "+"):
        result = num1 + num2
    elif(operand == "-"):
        result = num1 - num2
    elif(operand == "/"):
        result = num1 / num2
    elif(operand == "*"):
        result = num1 * num2
    return result

def solveChallenges(challenges):
    for i in challenges:
        problem = i['problem'][:-1].split()
        result = calculate(float(problem[0]), float(problem[2]), problem[1])

        print(f"Problem {i['id']}")
        print(f"{i['problem']} {result} \n")


print("Daniela Chavez blazerid: dchavez")
solveChallenges(challenges)