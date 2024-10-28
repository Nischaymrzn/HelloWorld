def quiz():
    score = 0
    questions = {
        "What is 2 + 2? ": 4,
        "What is the capital of France? ": "Paris",
    }
    for question, answer in questions.items():
        response = input(question)
        if str(response).lower() == str(answer).lower():
            score += 1
    return f"Your score: {score}/{len(questions)}"
