def alphabet_position(letter):
    natos = "abcdefghijklmnopqrstuvwxyz"
    upper_natos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in upper_natos:
        return upper_natos.index(letter)

    else:
        return natos.index(letter)

def rotate_character(nato, rot):
    natos = "abcdefghijklmnopqrstuvwxyz"
    #print("len natos = ", len(natos))
    upper_natos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #print("len upper_natos = ", len(upper_natos))
    if rot > len(natos):
        # isGo = True
        # while isGo:
        #     rot = rot - len(natos)
        #     print(rot)
        #     if rot <= len(natos):
        #         print(rot)
        #         isGo = False
        rot = rot % len(natos)
    # #checking is variable is uppercase
    if nato.isupper():
        nato_idx = alphabet_position(nato)
    
        #finding the index of the character in string
        new_idx = nato_idx + rot
        
        if new_idx >= len(upper_natos):
            new_idx = new_idx - len(upper_natos)
        
        #finding the character represented by the index
        new_nato = upper_natos[new_idx]
    
    else:
        nato_idx = alphabet_position(nato)
        new_idx = nato_idx + rot
        if new_idx >= len(natos):
            new_idx = new_idx - len(natos)
        new_nato = natos[new_idx]
    return new_nato

# def main():
#     letter_test = "A"
#     #print(alphabet_position(letter_test))
#     print(rotate_character(letter_test, 54))


# if __name__ == "__main__":
#     main()