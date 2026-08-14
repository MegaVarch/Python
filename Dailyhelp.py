class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter your daily message: ")

    def print_message(self):
        print("Message:", self.message.upper())


# Create object and call methods
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()


class HelperSession:
    def __init__(self):
        print("Helper session started.")

    def __del__(self):
        print("Helper session ended.")


def create_session():
    session = HelperSession()
    return session


# Create HelperSession object
session = create_session()


class PairFinder:
    def find_pair(self, numbers, target):
        for i, number in enumerate(numbers):
            for j in range(i + 1, len(numbers)):
                if number + numbers[j] == target:
                    print("Index pair:", i, j)


# Example
numbers = [10, 20, 30, 40, 50]
target = int(input("Enter target sum: "))

finder = PairFinder()
finder.find_pair(numbers, target)