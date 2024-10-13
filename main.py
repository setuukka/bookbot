def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def word_count(file_contents):
    file_contents = file_contents.split()
    return len(file_contents)

def count_characters(file_contents):
    file_contents = file_contents.lower()
    chardict = {}
    for character in file_contents:
        if character in chardict:
            chardict[character] += 1
        else:
            chardict[character] = 1
    return chardict

def report_print(length, charcount: dict):
    dict_as_list = [{key: value} for key, value in charcount.items()]
    filtered_list =[d for d in dict_as_list if list(d.keys())[0].isalpha()]
    filtered_list.sort(reverse = True, key = lambda x: list(x.values())[0])

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{length} word found in the document")
    print()
    for item in filtered_list:
        for key, value in item.items():
            print(f"The '{key}' character was found {value} times")

if __name__ == '__main__':
    file_contents = main()
    length = word_count(file_contents)
    #print(length)
    charcount = count_characters(str(file_contents))
    report_print(length, charcount)
    