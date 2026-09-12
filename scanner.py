import os
from PIL import Image
from PIL.ExifTags import TAGS

# Имя вашей картинки (она должна лежать в той же папке, что и этот скрипт!)
IMAGE_NAME = "Metaданные.jpg" 

def extract_metadata():
    # Проверяем, видит ли скрипт картинку в папке
    if not os.path.exists(IMAGE_NAME):
        print(f"Ошибка: Файл '{IMAGE_NAME}' не найден в этой папке!")
        print("Файлы, которые сейчас лежат в папке:", os.listdir('.'))
        return

    try:
        # Открываем изображение локально без интернета
        img = Image.open(IMAGE_NAME)
        exif = img._getexif()
        
        if not exif:
            print("Вайб-чек: Метаданные не найдены. Файл 'чист' от EXIF.")
            return
            
        print("=" * 45)
        print("       ЛОКАЛЬНО НАЙДЕНЫ МЕТАДАННЫЕ      ")
        print("=" * 45)
        
        for tag_id, value in exif.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if isinstance(value, (str, int, float, tuple)):
                print(f"{tag_name:<25} : {value}")
                
        print("=" * 45)
        
    except Exception as e:
        print(f"Произошла ошибка при анализе: {e}")

if __name__ == "__main__":
    extract_metadata()


