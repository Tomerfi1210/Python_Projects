class Caesar:
    def __init__(self, text: str, shift: int):
        self.__text = text
        self.__shift = shift

    def encrypt(self) -> str:
        """This function encrypt caesar cipher text"""

        self.__text = ''.join(
            [chr((ord(char) + self.__shift - ord('a')) % 26 + ord('a')) if char.isalpha() else char for char in
             self.__text])
        return self.__text

    def decrypt(self) -> str:
        """This function decrypt caesar cipher text"""

        self.__text = ''.join([chr((ord(char) - self.__shift - ord('a')) % 26 + ord('a')) if char != ' ' else char
                               for char in self.__text])
        return self.__text


if __name__ == '__main__':
    cipher = Caesar(input("Please enter text to encrypt: ").lower(),
                    int(input("Please enter number to shift the text: ")))
    print(f"The encrypt text is: {cipher.encrypt()}")
    print(f"The decrypt text is: {cipher.decrypt()}")
