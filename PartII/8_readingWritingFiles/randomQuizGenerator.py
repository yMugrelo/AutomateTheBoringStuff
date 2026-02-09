import json 
import random 

def load_question(filename):
    filename = "PartII\8_readingWritingFiles\questions.json"
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
def run_quiz(questions, num_questions = 5):
    score = 0

    selected = random.sample(questions, min(num_questions, len(questions)))

    for q in selected:
        print("\n" + q["question"])
        options = q["options"][:]
        random.shuffle(options)


        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        try: 
            choice = int(input("Your Answer: ")) - 1

            if options[choice] == q["answer"]:
                print("Correct!")
                score += 1

            else:
                print("Wrong!")

        except:
            print("Invalid input!")

    print(f"\nFinal score: {score}/{len(selected)}")

questions = load_question("questions.json")
run_quiz(questions)    