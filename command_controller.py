import os

#get output of command "python3.8 pox.py forwarding.l2_learning_mod" to a text and extract information from it
def get_output():
    os.system("python3.8 pox.py forwarding.l2_learning_mod > output.txt")
    f = open("output.txt", "r")
    output = f.read()
    f.close()
def main():
    get_output()
    f = open("output.txt", "r")
    output = f.read()
    f.close()
    print(output)


if __name__ == "__main__":
    main()
