def get_num_words(book_path):
    with open(book_path) as f:
        file_content = f.read()
        word_count = len(file_content.split())
        print(f"Found {word_count} total words")

def count_characters(book_path):
    with open(book_path) as f:
        file_content = f.read()
        character_dictionary = {}
        list_characters = list(file_content.lower())
        set_of_characters = set(list_characters)
        for character in set_of_characters:
            char_num = list_characters.count(character)
            character_dictionary[character] = char_num
    character_dictionary = sorted(character_dictionary.items(), key=lambda x: x[1], reverse=True)
    return character_dictionary



