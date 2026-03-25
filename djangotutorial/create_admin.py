import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Süper kullanıcı oluşturuldu: admin / admin")
else:
    print("Süper kullanıcı zaten var. Şifresi biliniyorsa kullanılabilir, değilse değiştirilmelidir.")
