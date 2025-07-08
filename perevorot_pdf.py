import os
import fitz 
from pathlib import Path

# НАСТРОЙКИ - ИЗМЕНИТЕ ЭТИ ПУТИ НА СВОИ
input_folder = r"C:\Users\VybornovOA1\Desktop\py\perevorot_pdf\input"
output_folder = r"C:\Users\VybornovOA1\Desktop\py\perevorot_pdf\rotated_pdf"

def rotate_pdf_files():
    """Функция для поворота PDF файлов на 90 градусов по часовой стрелке"""
    
    # Проверяем, существует ли входная папка
    if not os.path.exists(input_folder):
        print(f"Ошибка: Папка {input_folder} не существует!")
        return
    
    # Создаем выходную папку
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    processed = 0
    errors = 0
    
    print("Начинаем поворот PDF файлов...")
    print("-" * 50)
    
    # Обрабатываем каждый PDF файл
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            try:
                # Открываем PDF документ
                doc = fitz.open(input_path)
                
                # СОХРАНЯЕМ КОЛИЧЕСТВО СТРАНИЦ ДО ЗАКРЫТИЯ
                page_count = len(doc)
                
                # Поворачиваем каждую страницу
                for page_num in range(page_count):
                    page = doc[page_num]
                    # Поворот на 90 градусов по часовой стрелке
                    page.set_rotation(90)
                
                # Сохраняем повернутый PDF
                doc.save(output_path)
                doc.close()
                
                # ТЕПЕРЬ ВЫВОДИМ РЕЗУЛЬТАТ ИСПОЛЬЗУЯ СОХРАНЕННОЕ ЗНАЧЕНИЕ
                print(f"УСПЕХ {filename} (страниц: {page_count})")
                processed += 1
                
            except Exception as e:
                print(f" Ошибка с файлом {filename}: {e}")
                errors += 1
                # Закрываем документ в случае ошибки, если он был открыт
                try:
                    if 'doc' in locals():
                        doc.close()
                except:
                    pass
    
    print("-" * 50)
    print(f"Готово!")
    print(f"Успешно обработано: {processed} PDF файлов")
    if errors > 0:
        print(f"Ошибок: {errors}")
    print(f"Результаты сохранены в: {output_folder}")
    print("\n" + "=" * 50)
    print("Для выхода нажмите Enter...")
    input()

if __name__ == "__main__":
    rotate_pdf_files()