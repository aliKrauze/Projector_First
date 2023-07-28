# Лекція 10: Context Manager. Files

def gen_file():
    with open('lorem_ipsum.txt', 'w') as file:
        file.write("""Lorem ipsum dolor sit amet, consectetur adipiscing 
elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis 
nostrud exercitation ullamco laboris nisi ut aliquip
ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore 
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
non proident, sunt in culpa qui officia deserunt mollit animid
est laborum.""")
        

def copy_file():
    with open('lorem_ipsum.txt', 'r') as file:
        content = file.read()

    with open('lorem_ipsum2.txt', 'w') as copy_file:
        copy_file.write(content.upper())


if __name__ == "__main__":
    gen_file()
    copy_file()
