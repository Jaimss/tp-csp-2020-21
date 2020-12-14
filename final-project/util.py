def int_to_binary(number) -> int:
    """Turn an integer into a binary number"""
    return int('{0:b}'.format(int(number)))


def binary_to_int(binary_num) -> int:
    """Turn a binary string or number into an int"""
    return int(str(binary_num), 2)


def int_to_char(number) -> chr:
    """turn ints into their respective character"""
    return chr(number)


def char_to_int(character) -> int:
    """turn a character into its respective int"""
    return ord(character)


def encode(message: str, change_amount: int) -> list:
    """the encoding 'formula'. converts to random chars/nums then binary for those"""
    final_msg = []
    # the first thing in the final message will be a binary representation of
    # the amount each character is changed by +7
    modified_change = change_amount + 7
    final_msg.append(int_to_binary(change_amount))
    for c in message:
        # for every character swap it with one change_amount to the left
        num = char_to_int(c)
        num -= modified_change

        # for every new character convert it to a binary digit
        binary_num = int_to_binary(num)
        final_msg.append(binary_num)

    return final_msg


def decode(message: list) -> str:
    """decode an encoded message"""
    # get the amount each number has changed and remove that from the list
    modified_change_amt = message.pop(0)
    change_amount = binary_to_int(modified_change_amt) + 7

    # the final message string
    final_msg = ''

    # for every binary thing in the final message
    for b in message:
        # get the number and change it
        num = binary_to_int(b)
        num += change_amount

        # get the character
        c = int_to_char(num)
        final_msg += c

    return final_msg
