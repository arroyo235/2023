import re

def main(lines):
    hands = []
    
    for line in lines:
        line = line.split()
        hand = line[0]
        bid = int(line[1])
        
        # Append the [hand, bid] to the hands list
        hands.append([hand, bid])
        
    """
    Type of hands. Every hand is exactly one type. From strongest to weakest, they are:
    
    - Five of a kind, where all five cards have the same label: AAAAA
    - Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    - Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    - Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    - Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    - One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    - High card, where all cards' labels are distinct: 23456
    """
    def get_hand_type(hand):
        """
        Return the type of the hand
        """
        hand_types = {
            "Five of a kind": r'([2-9TJQKA])\1{4}', # OK
            "Four of a kind": r'([2-9TJQKA])\1{3}', # OK
            "Full house": r'([2-9TJQKA])\1{2}([2-9TJQKA])\2|([2-9TJQKA])\3([2-9TJQKA])\4{2}', # OK AAABB, AABBB
            "Three of a kind": r'([2-9TJQKA])\1{2}', # OK
            "Two pair": r'([2-9TJQKA])\1([2-9TJQKA])\2.|.([2-9TJQKA])\3([2-9TJQKA])\4|([2-9TJQKA])\5.([2-9TJQKA])\6', # OK AABBC, AABCC, ABBCC
            "One pair": r'([2-9TJQKA])\1', # OK
            "High card": r'([2-9TJQKA])(?:(?!\1)[2-9TJQKA]){4}' # OK
        }
        
        for hand_type, regex in hand_types.items():
            if re.search(regex, hand):
                return hand_type
        return None
    
    def get_hand_values(hand_type):
        """
        Return the value of the handby the type
        """
        hand_values = {
            "Five of a kind": 1,
            "Four of a kind": 2,
            "Full house": 3,
            "Three of a kind": 4,
            "Two pair": 5,
            "One pair": 6,
            "High card": 7,
        }
        
        return hand_values[hand_type]
    
    # Used for part 2
    initial_hands = hands
    # {hand_type: [[hand, bid], ...]} (unsorted)
    hands_groups = {} 
    for hand, bid in hands:
        # Order just to get the hand type but keeps the original order to compare the hands    
        sorted_hand = "".join(sorted(hand)) 
        hand_type = get_hand_type(sorted_hand)
        
        if hand_type not in hands_groups:
            hands_groups[hand_type] = []
        hands_groups[hand_type].append([hand, bid]) 
    
    def sort_hands(hands):
        """Sort hands by the value of the cards

        Args:
            hands = [[hand, bid], ...] -> x[0] = hand, x[1] = bid

        Returns:
            list: Sorted list of hands
        """
        card_order = "AKQJT98765432"
        sorted_hands = sorted(hands, key=lambda x: [card_order.index(card) for card in x[0]], reverse=True)
        
        return sorted_hands

    # Sort the hands for each hand type
    # {hand_type: [[hand, bid], ...]}
    
    sorted_hands_groups = {}
    for hand_type, hands in hands_groups.items():
        if hand_type not in sorted_hands_groups:
            sorted_hands_groups[hand_type] = []
        sorted_hands_groups[hand_type] = sort_hands(hands)

    # Sort he groups
    # {hand_type: [[hand, bid], ...]}
    sorted_hands_groups = dict(sorted(sorted_hands_groups.items(), key=lambda x: get_hand_values(x[0]), reverse=True))     
    
    # Putting all the hands in order in a list
    result_list = []
    for hand_type, hands in sorted_hands_groups.items():
        result_list.extend(hands)
    
    # print("\nResult list:", result_list)

    solution = sum(hand[1] * i for i, hand in enumerate(result_list, 1))

    # Solution part 1
    print("Part 1: ", solution)
    
    
    
    
    ############ PART 2 ############
    
    # For part 2, the J card is joker and can be any card that can act like whatever card would make the hand the strongest type possible
    new_card_order = "AKQT98765432J" # Whern J is alone, it is the lowest card
    
    # Parse the hands and try replacing the J card with the best card possible
        
    # print("Hands:", initial_hands)
    def get_best_hand_type(hand):
        """
        Return the best hand type for the hands with J cards
        """
        # Replace the J card with all the cards in the new_card_order in order to find the best hand type
        max_value = 99 # Value 1 is the best hand type 
        for card in new_card_order:
            new_hand = hand.replace("J", card)
            new_sorted_hand = "".join(sorted(new_hand))
            hand_type = get_hand_type(new_sorted_hand)
            hand_value = get_hand_values(hand_type)
            if (hand_value < max_value):
                max_value = hand_value
                best_hand_type = hand_type
                best_hand = new_hand
        return best_hand_type
            
            
    hands_groups = {}
    for hand, bid in initial_hands:
        sorted_hand = "".join(sorted(hand))
        # Parse the hand and replace the J card with the best card possible to get the best hand type
        # If the hand has not J card, the hand is the same
        if("J" in sorted_hand):
            hand_type = get_best_hand_type(sorted_hand)
        else:
            hand_type = get_hand_type(sorted_hand)
            
        if hand_type not in hands_groups:
            hands_groups[hand_type] = []
        hands_groups[hand_type].append([hand, bid])
    
    def sort_joker_hands(hands):
        """Sort hands by the value of the cards

        Args:
            hands = [[hand, bid], ...] -> x[0] = hand, x[1] = bid

        Returns:
            list: Sorted list of hands
        """
        new_card_order = "AKQT98765432J"
        sorted_hands = sorted(hands, key=lambda x: [new_card_order.index(card) for card in x[0]], reverse=True)
        
        return sorted_hands
    
    # Sort the hands for each hand type
    # {hand_type: [[hand, bid], ...]} (unsorted groups)
    sorted_hands_groups = {}
    for hand_type, hands in hands_groups.items():
        if hand_type not in sorted_hands_groups:
            sorted_hands_groups[hand_type] = []
        sorted_hands_groups[hand_type] = sort_joker_hands(hands)

    # Sort he groups
    # {hand_type: [[hand, bid], ...]} (sorted)
    sorted_hands_groups = dict(sorted(sorted_hands_groups.items(), key=lambda x: get_hand_values(x[0]), reverse=True))     
    
    # Putting all the hands in order in a list
    result_list = []
    for hand_type, hands in sorted_hands_groups.items():
        result_list.extend(hands)
    
    solution = sum(hand[1] * i for i, hand in enumerate(result_list, 1))

    # Solution part 2
    print("Part 2: ", solution)
        
        
   
if __name__ == "__main__":
    file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)