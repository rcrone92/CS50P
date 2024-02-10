import emoji

#emoji.emojize(language='alias')
def main():
    emo = input("Input: ")
    print(emoji.emojize('Output: ' + emo, language='alias'))


if __name__ == "__main__":
    main()
