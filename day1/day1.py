def find_number(line, word_to_number_list:{}):
    num = str()
    digit = str()
    text_number = str()
    last_number = str()
    for i in line:
        if i.isdigit():
            last_number = i
            if digit == "":
                digit = i
                num = num + digit
        else:
            text_number = text_number + i

            if any(word in text_number for word in word_to_number_list):
                text_number = [word for word in word_to_number_list if word in text_number][0]
                # print("Final number: ", text_number)
                last_number = word_to_number_list[text_number]
                if digit == "":
                    digit = last_number
                    num = num + digit
                text_number = str()
    return num

def main(lines):
    # PART 1
    numbers = list()

    for line in lines:
        num = str()
        num = ""
        digit1 = str()
        digit2 = str()
        last_number = str()
        for i in line:
            if i.isdigit():
                last_number = i
                if digit1 == "":
                    digit1 = i
                    num = num + digit1
        if digit2 == "":
            digit2 = last_number
            num = num + digit2    
            
        numbers.append(find_number(line))
    
    total_sum = sum(int(num) for num in numbers if isinstance(num, str))
    print("Total part 1: ", total_sum)
    
    
    # PART 2
    numbers1 = list()
    word_to_number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    # First digit
    for line in lines:
        numbers1.append(find_number(line, word_to_number))
    
    # Second digit, start from right to left
    reversed_word_to_number = {k[::-1]: v for k, v in word_to_number.items()}
    numbers2 = list()
    for line in lines:
        numbers2.append(find_number(line[::-1], reversed_word_to_number))
    
    
    # Concat the first and second digit
    numbers = [a+b for a,b in zip(numbers1, numbers2)]
    # print(numbers)
    total_sum = sum(int(num) for num in numbers if isinstance(num, str))
    print("Total part 2: ", total_sum) # 54676

    
if __name__ == "__main__":
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)

