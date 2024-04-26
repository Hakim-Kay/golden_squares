def count_words(text):
    words = text.split()
    print(words)

    counter = 0

    for word in words:
        if any(not char.isalnum() for char in word):
            # If the word contains non-alphanumeric characters, skip it
            continue
        counter += 1

    return counter


# Invoke the function
count_words("Count these words")
