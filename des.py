from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def des_encrypt(plaintext, key):
    """
    Fungsi untuk mengenkripsi teks menggunakan DES.
    plaintext: string teks yang akan dienkripsi.
    key: kunci (panjang harus 8 byte).
    """
    # Inisialisasi objek DES dengan mode ECB
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Padding plaintext agar panjangnya kelipatan 8 byte
    padded_text = pad(plaintext.encode(), DES.block_size)
    
    # Enkripsi dan encoding hasil dalam base64
    encrypted_bytes = cipher.encrypt(padded_text)
    encrypted_text = base64.b64encode(encrypted_bytes).decode()
    return encrypted_text


def des_decrypt(encrypted_text, key):
    """
    Fungsi untuk mendekripsi teks yang telah dienkripsi menggunakan DES.
    encrypted_text: string teks terenkripsi dalam base64.
    key: kunci (panjang harus 8 byte).
    """
    # Decode base64 menjadi byte terenkripsi
    encrypted_bytes = base64.b64decode(encrypted_text)
    
    # Inisialisasi objek DES dengan mode ECB
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Dekripsi dan hapus padding
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), DES.block_size)
    return decrypted_bytes.decode()


# Contoh Penggunaan
plaintext = "Halo Dunia!"
key = b"8bytekey"  # Kunci harus 8 byte

# Enkripsi
encrypted_text = des_encrypt(plaintext, key)
print("Teks Asli:       ", plaintext)
print("Teks Terenkripsi:", encrypted_text)

# Dekripsi
decrypted_text = des_decrypt(encrypted_text, key)
print("Teks Didekripsi: ", decrypted_text)
