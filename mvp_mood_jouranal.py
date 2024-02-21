
def take_input():
    name = input("Please enter your name: ")
    get_input = input("Tell about your day: ")
    return get_input,name

print(take_input())

moods = {
    "Happy": {"Happy", "Excited", "Delighted"},
    "Sadness": {"Unhappy", "Depressed", "Sorrowfull"},
    "Anger": {"Furious", "Annoyed", "Irritated"},
}

