class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age=0):
        if self.membership:
            self.name = name  # Attributes
            self.age = age

    def run(self):
        print(f"Hello {self.name}")


if __name__ == "__main__":
    player1 = PlayerCharacter("Josh", 43)
    player1.run()
