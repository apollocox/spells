from sys import exit

alphabet        = "abcdefghijklmnopqrstuvwxyz"
encode_alphabet = "mvxswdfguhjknbiolearycqztp"
def encode(message):
    encoded_message = ""
    for letter in message:
        # try to find letter in alphabet
        number = alphabet.find(letter)
        if number == -1:
            # if the "number" is less than zero, that means we didn't find it. just return whatever the input message letter was
            encoded_letter = letter
        else: 
            # 
            encoded_letter = encode_alphabet[number]
        encoded_message += encoded_letter
    return encoded_message

def decode(encoded_message):
    decoded_message = ""
    for letter in encoded_message:
        position = encode_alphabet.find(letter)
        if position == -1:
            decoded_letter = letter
        else:
            decoded_letter = alphabet[position]
        decoded_message += decoded_letter
    return decoded_message


def analyze(encoded_message):
    frequency = {}
    for letter in encoded_message:
        count = frequency.get(letter, 0)
        count = count + 1
        frequency[letter] = count
    for letter, count in frequency.items():
        print(letter, ":", count)

def main():
    message = input("Type your message:  ") # message = "hi i am a baby!"
    
    encoded_message = encode(message)
    print("original:", message)
    print("encoded:  ", encoded_message)
    print("decoded:  ", decode(encoded_message))

    analyze(encoded_message)

if __name__ == "__main__":
    main()
