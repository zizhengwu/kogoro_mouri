# This is a sample Python script.

def run():
    with open('appearance_exceptions.txt', 'r') as file:
        content = file.read()
        for i in range(1, 1101):
            if " "+str(i)+":" not in content:
                print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

