#Q4
# Credit  card numbers follow  certain patterns. A credit  card number must  have  between 13 and 16 digits. The number must start with the following: 
'''
starts with 4 for Visa cards
starts with 5 for MC cards
starts with 37 for AMEX cards
starts with 6 for Discover cards
'''
#Between 13 and 16 digits
#Must be valid
#Double even second digit from right to left, if doubling is a 2 digit number, add them
#Add the numbers in each odd space
#Add previous 2 numbers and divide them by 10, if num % 10 == 0, valid, else invalid. 

card_num = str(input("input your credit card information: "))
#num_length = len(card_num)
def verify_card(card_num):
    def valid_card(card_num):
        return card_len(card_num) and first_num(card_num) and card_num_total(card_num)

    def card_len(card_num):
        if len(card_num) <= 13 or len(card_num) >= 16:
            return True
        return False

    def first_num(card_num):
        if card_num[0] == 4 or card_num[0] == 5 or card_num[0] == 6 or (card_num[0] == 3 and card_num[1] == 7):
            return True
        return False
    
    def odd_places(card_num):
        odd_sum = 0
        for o in range(len(card_num) -1, -1, -2):
            odd_sum += card_num[o]
        return odd_sum
        
    def double_digits(card_num):
        double_sum = 0
        len = len(card_num)
        for d in range(len - 2, -1, -2):
            num = card_num[d]
            add = num * 2
            if add < 10:
                double_sum += add
            else:
                double_sum += ((add % 10) + (add // 10))
        return double_sum
    

    def card_num_total(card_num):
        if ((odd_places(card_num) + double_digits(card_num)) % 10 == 0):
            return True
        return False
        #card_len(card_num)
        #first_num(card_num)
    print(valid_card(str(4388576018402626)))
    print(valid_card(str(4388576018410707)))
verify_card(card_num)