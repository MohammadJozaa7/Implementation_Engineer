
# Answer for question 1:

# Example:
arr = [104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 100, 115, 119, 107, 102, 119, 50, 51, 119, 48, 101, 107, 101, 103, 101, 102, 103]

def BriteCore(number):
    return chr(number)
    
answer_Q1 = ''.join(map(BriteCore, arr))
print("Answer Question 1:", answer_Q1)



# Answer for question 2:
from cryptography.fernet import Fernet
key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
message = b'gAAAAABc59nTih7J4tG7iJ2DSkjgpGmtMIFe6A6DK304PWGGd2KmqOuGDqtPlQ0znAPh_Vu3YStUXAKmO78PyKWjPNCb_tbXCw8RsZvkKGP2Lju5hck97PhRP840yOr7Pvw_7zppLfBb-66Jtk3VMrmS4raiWuvtqITb2ja15VPRtsqJjvPBX1bLcNK-v9d7SubUakM1VFvT'

def main():
    f = Fernet(key)
    print("Answer Question 2:", f.decrypt(message))
    
if __name__ == "__main__":
    main()