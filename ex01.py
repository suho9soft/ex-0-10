import tkinter as tk
from tkinter import ttk

# 입력값을 터미널에 출력하는 함수
def print_input():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    print(f"이름: {name}, 나이: {age}, 성별: {gender}")

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("입력 폼")
root.geometry("300x200")

# 이름 입력 필드
tk.Label(root, text="이름:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# 나이 입력 필드
tk.Label(root, text="나이:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# 성별 선택 라디오 버튼
tk.Label(root, text="성별:").grid(row=2, column=0, padx=10, pady=5)
gender_var = tk.StringVar(value="남성")
tk.Radiobutton(root, text="남성", variable=gender_var, value="남성").grid(row=2, column=1, padx=10, pady=5)
tk.Radiobutton(root, text="여성", variable=gender_var, value="여성").grid(row=2, column=2, padx=10, pady=5)

# 입력 버튼
submit_button = tk.Button(root, text="입력", command=print_input)
submit_button.grid(row=3, columnspan=3, pady=10)

# Tkinter 윈도우 실행
root.mainloop()
