import random
import string
import time
import os

def generatetext(length=100):
    
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def createtext():
    
    filename = "randomFile.txt"
    content = generatetext()
    
    with open('/storeage/randomFileNo.txt', 'w') as file:
        file.write(content)
    
    print(f"Generated file: {filename}")

def main():
    # timestamp=0
    while True:
        # timestamp = timestamp + 1
        createtext()
        time.sleep(60) 

if __name__ == "__main__":
    main()
