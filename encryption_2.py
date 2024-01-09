import os

def read_file(key):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop") # creating path for files to read
    filePath = os.path.join(desktop, key)
    in_file = open(filePath, "rb")  # opening for [r]eading as [b]inary
    data = in_file.read()  
    in_file.close()
    return data


def write_file(file_name, content):
    print("hello")
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # creating path for files to write
    filePath = os.path.join(desktop, file_name)
    out_file = open(filePath,"wb")
    out_file.write(bytes(content))
    out_file.close()

def encrypt(plain_text,key):
    K = []    # creating a permuted key(K) 
    for i in range(len(key)):
        K.append(key[key[i]])  
    mapin = dict(zip(key,K))   # map values from key -> K 
    return mapin

def decrypt(cipher_text,mapin):
    plain_text1 = []
    key_list=list(mapin.keys())
    val_list = list(mapin.values())
    
    for i in range(len(cipher_text)):
        ind = val_list.index(cipher_text[i])
        plain_text1.append(key_list[ind])
    return plain_text1
    

def test_encryption():
    key = list(read_file('key'))
    plain_text= list(read_file('plain_text'))
    mapin = encrypt(plain_text,key)
    content = []   # USING mapin to map values from plain_text file using key -> K to encrypt plain_text file     ( As plain_text consist of same values as key )
    for j in range(len(plain_text)):
        content.append(mapin[plain_text[j]])
    write_file('cipher_text',content)   # writing  encrypted plain_text to cipher_text file
    cipher_text = list(read_file('cipher_text')) # reading from cipher_text file
    plain_text1 = decrypt(cipher_text,mapin)  # decrypting cipher_text file using mapin (key -> K)
    write_file('plain_text1',plain_text1)  # writing decrypted to plain_text1 which is same as plain_text
    
test_encryption()
