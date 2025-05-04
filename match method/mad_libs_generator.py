def mad_libs():
    print("Welcome to Mad Libs!")
    
    words = {}
    for prompt in ["adjective", "noun", "verb (past tense)", "adverb", "animal", "food"]:
        words[prompt] = input(f"Enter a {prompt}: ")
    
    story = f"""
    Once upon a time, there was a {words['adjective']} {words['noun']} who {words['verb (past tense)']} 
    {words['adverb']} through the forest. Suddenly, a {words['animal']} appeared and offered them 
    some {words['food']}. What an adventure!
    """
    
    print("\nHere's your story:")
    print(story)
mad_libs()