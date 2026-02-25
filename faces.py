def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    text = input("Type a sentence: ")
    result = convert(text)
    print(result)

if __name__ == "__main__":
    main()
