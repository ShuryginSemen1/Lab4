import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")
        self.root.geometry("350x280")  # Увеличим окно для кнопки копирования

        # Переменные для хранения состояния checkbox
        self.lower_var = tk.BooleanVar(value=True)  # По умолчанию включено
        self.digits_var = tk.BooleanVar(value=True)  # По умолчанию включено
        self.symbols_var = tk.BooleanVar(value=False)  # По умолчанию выключено

        self._create_widgets()

    def _create_widgets(self):
        # Фрейм для checkbox'ов
        options_frame = ttk.LabelFrame(self.root, text="Параметры пароля")
        options_frame.pack(padx=10, pady=10, fill="x")

        # Checkbox'ы
        ttk.Checkbutton(options_frame, text="Включить нижний регистр (a-z)", variable=self.lower_var).pack(anchor="w",
                                                                                                           padx=5,
                                                                                                           pady=2)
        ttk.Checkbutton(options_frame, text="Включить цифры (0-9)", variable=self.digits_var).pack(anchor="w", padx=5,
                                                                                                   pady=2)
        ttk.Checkbutton(options_frame, text="Включить спецсимволы (!@#$%)", variable=self.symbols_var).pack(anchor="w",
                                                                                                            padx=5,
                                                                                                            pady=2)

        # Кнопка генерации
        ttk.Button(self.root, text="Сгенерировать пароль", command=self.generate_password).pack(pady=10)

        # Лейбл для вывода пароля (изменяемый)
        self.password_label = ttk.Label(self.root, text="Пароль будет здесь", font=("Helvetica", 12))
        self.password_label.pack(pady=10)

        # Кнопка копирования
        ttk.Button(self.root, text="Копировать пароль", command=self.copy_password).pack(pady=5)

    def generate_password(self):

        characters = ""
        if self.lower_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += "!@#$%"

        if not characters:
            messagebox.showerror("Ошибка", "Выберите хотя бы один параметр")
            return

        password = "".join(random.choice(characters) for _ in range(12))  # Пароль длиной 12
        self.password_label.config(text=password)
        self.generated_password = password  # Сохраняем сгенерированный пароль для копирования

    def copy_password(self):
        try:
            pyperclip.copy(self.generated_password)
            messagebox.showinfo("Успех", "Пароль скопирован в буфер обмена")
        except AttributeError:
            messagebox.showerror("Ошибка", "Сначала сгенерируйте пароль")
        except pyperclip.PyperclipException:
            messagebox.showerror("Ошибка",
                                 "Не удалось скопировать пароль. Убедитесь, что у вас есть нужные зависимости (например, xclip или xsel на Linux)")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()