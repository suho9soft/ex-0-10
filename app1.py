import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import streamlit as st
import threading

# MySQL 데이터베이스에 데이터 삽입 함수
def insert_data(num, name, age, gender):
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='123f5678',
            database='python4'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            
            # 중복된 num 값 확인
            cursor.execute("SELECT COUNT(*) FROM user WHERE num = %s", (num,))
            result = cursor.fetchone()
            if result[0] > 0:
                st.error(f"번호 {num} 는 이미 존재합니다. 다른 번호를 입력해 주세요.")
                return

            query = "INSERT INTO user (num, name, age, gender) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (num, name, age, gender))
            connection.commit()
            st.success("데이터가 성공적으로 삽입되었습니다.")
    except Error as e:
        st.error(f"Error: '{e}'")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# 입력값을 데이터베이스에 삽입하는 함수
def print_input():
    num = num_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()

    # num과 age 입력값을 정수로 변환
    try:
        num = int(num)
        age = int(age)
        insert_data(num, name, age, gender)
        print(f"번호: {num}, 이름: {name}, 나이: {age}, 성별: {gender}")
    except ValueError:
        st.error("번호와 나이는 숫자로 입력해 주세요.")

# Tkinter 윈도우 설정 함수
def tkinter_app():
    global num_entry, name_entry, age_entry, gender_var
    root = tk.Tk()
    root.title("입력 폼")
    root.geometry("300x250")

    # 번호 입력 필드
    tk.Label(root, text="번호:").grid(row=0, column=0, padx=10, pady=5)
    num_entry = tk.Entry(root)
    num_entry.grid(row=0, column=1, padx=10, pady=5)

    # 이름 입력 필드
    tk.Label(root, text="이름:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    # 나이 입력 필드
    tk.Label(root, text="나이:").grid(row=2, column=0, padx=10, pady=5)
    age_entry = tk.Entry(root)
    age_entry.grid(row=2, column=1, padx=10, pady=5)

    # 성별 선택 라디오 버튼
    tk.Label(root, text="성별:").grid(row=3, column=0, padx=10, pady=5)
    gender_var = tk.StringVar(value="남성")
    tk.Radiobutton(root, text="남성", variable=gender_var, value="남성").grid(row=3, column=1, padx=10, pady=5)
    tk.Radiobutton(root, text="여성", variable=gender_var, value="여성").grid(row=3, column=2, padx=10, pady=5)

    # 입력 버튼
    submit_button = tk.Button(root, text="입력", command=print_input)
    submit_button.grid(row=4, columnspan=3, pady=10)

    # Tkinter 윈도우 실행
    root.mainloop()

# Streamlit 앱 함수
def streamlit_app():
    st.title("서버 주소 입력 폼")
    
    # 서버 주소 입력 받기
    server_url = st.text_input('서버 주소를 입력하세요:', 'http://172.30.1.177:8501')

    # 서버로 이동할 링크 생성 버튼
    if st.button('서버로 이동하기'):
        st.markdown(f'[서버로 이동하기]({server_url})', unsafe_allow_html=True)

# Streamlit 애플리케이션을 별도의 스레드에서 실행
streamlit_thread = threading.Thread(target=streamlit_app)
streamlit_thread.start()

# Tkinter 애플리케이션 실행
tkinter_app()
