import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
import pygame

# 1. Автоматически определяем папку со скриптом
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Имена файлов точно так же, как они у тебя называются в VS Code:
IMG_NAME = "orange_phoenix.jpg.png"
SOUND_NAME = "glich1.mp3.mp3"

IMG_PATH = os.path.join(BASE_DIR, IMG_NAME)
SOUND_PATH = os.path.join(BASE_DIR, SOUND_NAME)

# 2. Инициализация звукового движка
try:
    pygame.mixer.init()
except Exception as e:
    print(f"[!] Ошибка звука: {e}")

# 3. Создание полноэкранного окна
root = tk.Tk()
root.attributes("-fullscreen", True)  # На весь экран
root.configure(bg="black")            # Чёрный фон
root.config(cursor="none")            # Прячем курсор мыши

photo = None

# Функция, которая сработает через 3 секунды
def show_effect():
    global photo
    
    # Включаем зацикленный звук
    if os.path.exists(SOUND_PATH):
        try:
            pygame.mixer.music.load(SOUND_PATH)
            pygame.mixer.music.play(loops=-1)
        except Exception as e:
            print(f"[!] Ошибка воспроизведения: {e}")

    # Показываем фото на весь экран
    if os.path.exists(IMG_PATH):
        try:
            screen_w = root.winfo_screenwidth()
            screen_h = root.winfo_screenheight()

            pil_img = Image.open(IMG_PATH)
            pil_img = pil_img.resize((screen_w, screen_h))
            photo = ImageTk.PhotoImage(pil_img)

            label = tk.Label(root, image=photo, bg="black", bd=0)
            label.pack(expand=True, fill="both")
        except Exception as e:
            print(f"[!] Ошибка загрузки фото: {e}")

    # Запланировать автоматическое закрытие через 10 секунд
    root.after(10000, close_program)

# Функция закрытия программы
def close_program():
    pygame.mixer.music.stop()
    root.destroy()

# Досрочный выход по кнопке ESC (на всякий случай)
root.bind("<Escape>", lambda e: close_program())

# Задержка 3 секунды на чёрном экране перед стартом
root.after(3000, show_effect)

# Запуск
root.mainloop()