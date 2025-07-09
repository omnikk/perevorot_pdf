import os
import fitz 
from pathlib import Path

# НАСТРОЙКИ - ИЗМЕНИТЕ ЭТИ ПУТИ НА СВОИ
input_folder = r"input"
output_folder = r"rotated_pdf"

def rotate_pdf_files():
    """Функция для поворота PDF файлов на 90 градусов по часовой стрелке"""
    
    if not os.path.exists(input_folder):
        print(f"Ошибка: Папка {input_folder} не существует!")
        return
    
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
                doc = fitz.open(input_path)                
                page_count = len(doc)
                
                for page_num in range(page_count):
                    page = doc[page_num]
                    # Поворот на 90 градусов по часовой стрелке
                    page.set_rotation(90)
                
                doc.save(output_path)
                doc.close()
                
                print(f"УСПЕХ {filename} (страниц: {page_count})")
                processed += 1
                
            except Exception as e:
                print(f" Ошибка с файлом {filename}: {e}")
                errors += 1
                try:
                    if 'doc' in locals():
                        doc.close()
                except:
                    pass
    
    print("-" * 50)
    print(f"Успешно обработано: {processed} PDF файлов")
    if errors > 0:
        print(f"Ошибок: {errors}")
    print(f"Результаты сохранены в: {output_folder}")
    print("Для выхода нажмите Enter...")
    input()

if __name__ == "__main__":
    rotate_pdf_files()