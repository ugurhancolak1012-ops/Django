import os
import sys
import subprocess

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Tüm part klasörlerini bul
    parts = []
    for d in os.listdir(base_dir):
        if d.startswith("part") and os.path.isdir(os.path.join(base_dir, d)):
            # İçinde manage.py var mı kontrol et
            if os.path.exists(os.path.join(base_dir, d, "manage.py")):
                parts.append(d)
                
    parts.sort()
    
    print("=== Django Ödev Başlatıcı ===")
    
    if not parts:
        print("Henüz çalıştırılabilir hiçbir part bulunamadı (klasör içinde 'manage.py' olan).")
        print("Lütfen Antigravity'nin partları oluşturmasını bekleyin.")
        input("Çıkmak için Enter'a basın...")
        return

    print("Hangi partı çalıştırmak istersiniz?")
    for i, part in enumerate(parts):
        print(f"{i + 1}. {part}")
        
    choice = input("\nSeçiminiz (örn: 1): ")
    
    try:
        index = int(choice) - 1
        if 0 <= index < len(parts):
            selected_part = parts[index]
            print(f"\n>>>> {selected_part} sunucusu başlatılıyor... <<<<")
            print(f"Sunucu adresine (genellikle http://127.0.0.1:8000) tarayıcınızdan gidebilirsiniz.\n")
            
            # Sunucuyu başlat
            manage_py_path = os.path.join(base_dir, selected_part, "manage.py")
            try:
                subprocess.run([sys.executable, manage_py_path, "runserver"])
            except KeyboardInterrupt:
                print("\nSunucu durduruldu.")
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Lütfen geçerli bir numara girin.")

if __name__ == "__main__":
    main()
