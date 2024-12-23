import socket
from DES import encryption_large_text, decryption_large_text, generate_valid_key, text_to_hex, hex_to_text

def server_program():
    host = socket.gethostname()
    port = 5003
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from:", address)

    # Terima key dari klien
    key = conn.recv(1024).decode()
    print("Received Key from Client:", key)

    while True:
        # Terima pesan terenkripsi dari klien
        encrypted_data = conn.recv(1024).decode()
        if not encrypted_data:
            break

        # Deskripsi pesan dengan key
        decrypted_data = decryption_large_text(encrypted_data, key)
        decrypted_data = hex_to_text(decrypted_data)

        print("Received Encrypted Message:", encrypted_data)
        print("Decrypted Message:", decrypted_data)

        # Kirim pesan balik
        response = input("Server Response: ")
        if response.lower().strip() == "bye":
            break
        
        # Convert response to hex before encrypting
        response_hex = text_to_hex(response)  # Convert to hex format
        encrypted_response = encryption_large_text(response_hex, key)
        
        conn.send(encrypted_response.encode())
        print("Encrypted Response:", encrypted_response)

    conn.close()

if __name__ == '__main__':
    server_program()
