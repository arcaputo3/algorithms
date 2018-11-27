class Question:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


prompts = [
"What is the capital of Connecticut?\n(a) Hartford\n(b) Westport\n(c) Greenwich\n(d) Wallingford\n\n",
"What are the first four digits of pi?\n(a) 4.123\n(b) 3.213\n(c) 2.090\n(d) 3.141\n\n",
"What color is the sky?\n(a) Green\n(b) Red\n(c) Blue\n(d) Yellow\n\n"
]

questions = [
Question(prompts[0], 'a'),
Question(prompts[1], 'd'),
Question(prompts[2], 'c')
]

def test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got {}/{} correct".format(score, len(questions)))

test(questions)
