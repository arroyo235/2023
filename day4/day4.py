import re

def main(lines):
    
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """
    cards = {}
    for line in lines:
        card = line.split(":")[0]
        # Obtengo el numero del card
        num_card = int(re.findall(r"\d+", card)[0])
        cards[num_card] = []
        # List of winnning numbers
        winning_numbers = line.split(":")[1].split("|")[0].split()
        # List of numbers i have
        my_numbers = line.split(":")[1].split("|")[1].split()
        # Convertimos los numeros a int
        winning_numbers = [int(x) for x in winning_numbers]
        my_numbers = [int(x) for x in my_numbers]
        # print(winning_numbers)
        # print(my_numbers)
        for num in my_numbers:
            if num in winning_numbers:
                cards[num_card].append(num)
    
    # Part 1    
    points = 0
    for k, v in cards.items():
        if (len(v) > 0):
            points += pow(2, len(v)-1)

    print("Part 1: ", points)
    
    # Part 2
    # Number of instances of each card
    copies = {}
    # Inicializa las copias con 1
    for k, v in cards.items():
        copies[k] = 1
    
    # Recorre las cartas
    for k, v in cards.items():
        # Recorre segun el numero de copias de cada carta
        for i in range(copies.get(k)):
            # Suma una copia a cada carta
            for i in range(1, len(v)+1):
                copies[k+i] += 1
        # print(copies)   
        
    print("Part 2: ", sum(copies.values()))

if __name__ == "__main__":
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)

