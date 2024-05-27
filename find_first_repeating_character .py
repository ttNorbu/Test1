def find_first_repeating_character(j):
    count = {}
    for char in j:
        if char in count:
            return char, id(char) # print(f"{char} "and" id{char}")
        else:
            count[char] = 1  #like {count.add(char)} but it is for set only...set only store unique vale not duplicate
    return None
