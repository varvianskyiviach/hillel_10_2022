class Colorizer:
    __color_dic = {
        "grey": "\033[90m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "pink": "\033[95m",
        "turquoise": "\033[96m",
        "default": "\033[0m",
    }

    def __init__(self, color):
        if color in self.__color_dic:
            self.color = print(self.__color_dic[color])
        else:
            self.color = print(self.__color_dic["default"])
            print(f"Error, argument '{color}' not found")

    def __enter__(self):
        return self.color

    def __exit__(self, type, value, traceback):
        self.color = print(self.__color_dic["default"])


with Colorizer("r"):
    print("printed in yellow")

print("printed in default color")
