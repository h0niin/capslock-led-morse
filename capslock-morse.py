import ctypes, time

morse = {
	'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

user32 = ctypes.windll.user32

def turn_capslock(on):
	curr = user32.GetKeyState(20)  #20 = VK_CAPITAL
	if curr != on:
		user32.keybd_event(20, 69, 0, 0) #keydown
		user32.keybd_event(20, 69, 2, 0) #keyup

def to_morse(char):
	code = morse.get(char.upper())
	print(f"{char.upper()} => {code}")
	for c in code:
		turn_capslock(1)
		time.sleep(0.6 if c == '.' else 1.8)
		turn_capslock(0)
		time.sleep(0.6)

print("\nEnter a CHAR [A-Z/0-9] and your CAPS-LOCK LED will blink in MORSE CODE!\n")
while True:
	char = input("char: ")
	if char == '~': break
	to_morse(char)
		
