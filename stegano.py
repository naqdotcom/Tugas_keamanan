from stegano import lsb
import os


def get_image_path():
    while True:
        img_path = input("Masukkan path gambar (contoh: E:/path/to/image.png): ")
        if os.path.exists(img_path) and img_path.endswith(('.png', '.jpg')):
            return img_path
        else:
            print("Path gambar tidak valid atau format salah. Silakan coba lagi.")


def hide_message():
    img_path = get_image_path()  # Perbaikan: Fungsi dipanggil dengan kurung
    message = input("Masukan pesan rahasia yang akan disembunyikan: ")

    try:
        # Proses menyembunyikan pesan
        secret = lsb.hide(img_path, message)
        save_path = input("Masukkan path untuk menyimpan gambar hasil (contoh: E:/hidden_img.png): ")

        # Validasi folder path
        if not os.path.exists(os.path.dirname(save_path)):
            print("Folder tujuan tidak ada. Silakan cek path yang dimasukkan.")
            return

        # Simpan gambar hasil
        secret.save(save_path)
        print(f"Pesan berhasil disembunyikan. Gambar disimpan di: {save_path}")
    except Exception as e:
        print(f"Gagal menyembunyikan pesan: {e}")


def show_message():
    img_path = get_image_path()  # Ambil path gambar
    try:
        # Ambil pesan dari gambar
        clear_message = lsb.reveal(img_path)
        if clear_message:
            print(f"Pesan tersembunyi: {clear_message}")
        else:
            print("Tidak ada pesan tersembunyi dalam gambar.")
    except Exception as e:
        print(f"Gagal menampilkan pesan dari gambar: {e}")


def main():
    while True:
        print("\nSteganography Tool - Terminal Version")
        print("1. Sembunyikan Pesan")
        print("2. Tampilkan Pesan")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            hide_message()
        elif choice == '2':
            show_message()
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih kembali.")


if __name__ == "__main__":
    main()