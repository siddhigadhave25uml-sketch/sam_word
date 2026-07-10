
def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
 
        words = content.split()

        print("\n" + "="*40)
        print("       WORD COUNTER")
        print("="*40)

        print("\nFile Content:")
        print(content)

        print("\nTotal Words:", len(words))
        print("Total Characters:", len(content))

    except FileNotFoundError:
        print("\nError: File Not Found!")

    except Exception as e:
        print("\nError:", e)

filename = input("Enter File Name: ")
count_words(filename)
