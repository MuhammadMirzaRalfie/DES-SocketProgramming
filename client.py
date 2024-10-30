import socket
from DES import encryption_large_text, decryption_large_text, generate_valid_key, text_to_hex, hex_to_text

def client_program():
    host = socket.gethostname()
    port = 5003
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    # Meminta input untuk key dari pengguna
    key = generate_valid_key()
    client_socket.send(key.encode())  # Mengirim key ke server
    print("Generated Key sent to Server:", key)

    while True:
        message = input("Client Message: ")
        if message.lower().strip() == "bye":
            break

        # Enkripsi pesan dengan key
        encrypted_message = encryption_large_text(text_to_hex(message), key)  # Convert message to hex before encrypting
        client_socket.send(encrypted_message.encode())
        print("Message:", message)
        print("Encrypted Message:", encrypted_message)

        # Terima respons terenkripsi dari server
        encrypted_response = client_socket.recv(1024).decode()
        if not encrypted_response:
            break

        decrypted_response = decryption_large_text(encrypted_response, key)
        print("Received Encrypted Response:", encrypted_response)
        print("Decrypted Response:", decrypted_response)
        

    client_socket.close()

if __name__ == '__main__':
    client_program()
