def quiz_game():
    score = 0
    questions = [
        ("What's 2+2?", "4"),
        ("Capital of France?", "paris"),
        ("Python first released?", "1991")
    ]
    
    for question, answer in questions:
        user_answer = input(question + " ").lower()
        match user_answer:
            case answer:
                print("Correct!")
                score += 1
            case _:
                print(f"Wrong! The answer is {answer}")
    
    print(f"Your score: {score}/{len(questions)}")