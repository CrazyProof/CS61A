LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class Capslock:
    def __init__(self):
        self.pressed = 0
    def press(self):
        self.pressed += 1

class Button:

    caps_lock = Capslock()
    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0
    def press(self):
        self.pressed += 1
        if caps_lock.pressed % 2 == 1:
            return self.output(self.letter.upper())
        else:
            return self.output(self.letter)

class Keyboard:
    def __init__(self):
        self.typed = []
        self.keys = {i: Button(i, print) for i in LOWERCASE_LETTERS}
    def typed(self, word):
        assert all([s in LOWERCASE_LETTERS for s in word])
        for s in word:
            self.typed.append(self.keys[s].press())
