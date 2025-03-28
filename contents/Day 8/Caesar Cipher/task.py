def encode_decode():
    
    print("Welcome to Ceasar Cipher Game!")
    
    
    def encoding(original_text, encoding):
            encode = ""
            if decision == 'encode':
                for i in message:
                    encode += chr(ord(i) + no).lower()
                print(f"Here is the encrypted message: {encode}")
            
    def decoding(original_text, decoding): 
            decode = ""
            if decision == 'decode':
                for i in message:
                    decode += chr(ord(i) - no).lower()
                print(f"Here is the decrypted message: {decode}")
                
    game_over = False
    while not game_over:
        
        decision = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: \n"))
        message = str(input("Type your message!\n"))
        no = int(input("Type the shift number:\n"))

        encoding(message, decision)
        decoding(message, decision)
        
        choice = str(input("Type yes to continue, type no to end the game!\n"))
        if choice == 'yes':
            continue
        else:
            game_over = True
            
encode_decode()     
