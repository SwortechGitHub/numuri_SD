# Koda paraugs
# returns True if checksum is valid, otherwise returns False
def Luhn_checks_my_card(card_number):
    sum=0
    first = True
    # Reverse loops card_number
    for number in reversed(card_number):
        # Checks if its first number
        if first:
            sum+=int(number)
            first = False
        else:
            x =int(number)*2
            # Checks if 2 numbers
            if x>9:
                sum+=int(str(x)[0])
                sum+=int(str(x)[1])
            else:
                sum+=int(number)*2
            first = True

    return str(sum)[len(str(sum))-1]=="0"

# returns name of card if digits are valid, otherwise returns "INVALID"
def check_card_type(card_number):
    # American Exrpesss 15 cipari (34,37)
    # MasterCard 16 cipari(51,52,53,54,55)
    # Visa 13 vai 16 cipari(4)
    if card_number[0]=='3' and len(card_number)==15:
        if card_number[1]=='4' or card_number[1]=='7':  
            #American Express
            return "AMEX"
    elif card_number[0]=='5'and len(card_number)==16:
        if 0<int(card_number[1])<6:  
            #MasterCard
            return "MasterCard"
    elif card_number[0]=='4':
        if len(card_number)==13 or len(card_number)==16:
            #Visa
            return "VISA"
    else:
        return "INVALID"

# main logic
def main():
    card_number = input("Card number: ")

    if Luhn_checks_my_card(card_number):
        print(check_card_type(card_number))
    else:
        print("INVALID")
