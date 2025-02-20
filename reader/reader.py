import time 
def readtext():
    with open('/storeage/randomFileNo.txt') as f:
        contents = f.read()
        print(contents)



def main():
    
    while True:
        
        readtext()
        time.sleep(60) 

if __name__ == "__main__":
    main()