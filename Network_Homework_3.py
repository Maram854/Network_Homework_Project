import csv
import random
questions={
    "what is 1+1?":"2",
    "what is 2+2?":"4",
    "what is 3+3?":"6",
    "what is 4+4?":"8",
    "what is 5+5?":"10",
    "what is 6+6?":"12",
    "what is 7+7?":"14",
    "what is 8+8?":"16",
    "what is 9+9?":"18",
    "what is 10+10?":"20",
    "what is 11+11?":"22",
    "what is 12+12?":"24",
    "what is 13+13?":"26",
    "what is 14+14?":"28",
    "what is 15+15?":"30",
    "what is 16+16?":"32",
    "what is 17+17?":"34",
    "what is 18+18?":"36",
    "what is 19+19?":"38",
    "what is 20+20?":"40",
}
random.shuffle(list(questions.keys()))
score=0
for question in questions.keys():
    answer=input(f"{question}:")
    if answer==questions[question]:
        score+=1
percentage_score=(score/len(questions))*100
print(f"(your score is {score} out of{len(questions)}({percentage_score}%).")
with open("results.csv","a",newline='') as f:
    writer=csv.writer(f)
    writer.writerow([score.percentage_score])  