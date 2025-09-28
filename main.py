MORSE_CODE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'
}
MORSE_TO_TEXT = {morse: char for char, morse in MORSE_CODE.items()}


##### Text/Morse #####

def text_to_morse(text):
    text = text.lower()
    morse= []

    for char in text:
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
        else:
            morse.append("?")

    return ' '.join(morse)

def morse_to_text(morse_message):
    words = morse_message.split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = [MORSE_TO_TEXT.get(letter, '?') for letter in letters]
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)



def start():
    option = int(input("Select Option:\n   1.Text To Morse\n   2.Morse To Text\n"))

    if option == 1:
        message = input("Please enter your message:\n")
        morse_message = text_to_morse(message)
        print(morse_message)
    elif option == 2:
        message = input("Please enter your message:\n")
        text_message = morse_to_text(message)
        print(text_message)

    else:
        start()

start()