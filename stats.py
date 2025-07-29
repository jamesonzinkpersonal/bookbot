def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lower_case_clean = text.lower()
    character_dict = {}
    for char in lower_case_clean:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    
    return character_dict

def sort_on(items):
    return items["num"]

def create_sorted_list(character_dict):
    character_list = []
    for key, value in character_dict.items():
        character_list.append({"char": key, "num": value})
    
    character_list.sort(reverse=True, key=sort_on)
    
    return character_list 

