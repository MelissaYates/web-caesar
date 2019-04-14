from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    new_natos = ""
    natos = "abcdefghijklmnopqrstuvwxyz"
    upper_natos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for nato in text:
        if (nato in upper_natos) or (nato in natos):
            new_nato = rotate_character(nato, rot)
            new_natos = new_natos + new_nato
        else:
            new_natos = new_natos + nato     
    return new_natos
    
    
def main():
    #from sys import argv
    #print("argv: ",argv)
    string = input("Type a message: \n")
    # print()
    # print(string)
    rotate = int(input("Rotate by: \n"))
    # print(rotate)
    #print(encrypt(string, int(argv[1])))
    print(rotate_string(string, rotate))

if __name__ == "__main__":
    main()