while True:
    iso = input("Please input a word.\n").lower()
    valid = True
    chars = []
    for i in iso:
        if i in chars:
            valid = False
            break
        chars.append(i)
    if valid:
        print("That is an isogram")
    else:
        print("that is not an isogram")
