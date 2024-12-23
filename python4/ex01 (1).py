import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

mysql_info = {"host":"localhost","user":"root","password":"123f5678","database":"python4"}


#이름, 나이, 성별 입력값을 DB에 저장한다!
def insert_data():
    try:
        # 데이터베이스에 연결합니다.
        conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            database=mysql_info["database"],
            cursorclass=pymysql.cursors.DictCursor 
        )

        cursor = conn.cursor()
        
        myname =name_entry.get()
        myage = age_var.get()
        mygender = selected_gender.get()

        # SQL 쿼리를 준비합니다.
        sql = "insert into user(name,age,gender) values(%s,%s,%s)"
        val = (myname , myage, mygender)
        # SQL 쿼리를 실행합니다.
        cursor.execute(sql, val)

        # 변경 사항을 커밋합니다.
        conn.commit()
        
        # 연결을 닫습니다.
        cursor.close()
        conn.close()

        # 성공 메시지를 표시합니다.
        print("Data inserted successfully!")
        #입력한 결과 출력
        fetch_data()
        messagebox.showinfo("Info", "입력이 완료되었습니다!!")        
    except pymysql.MySQLError as err:
        # 에러 메시지를 표시합니다.
        print(f"Error: {err}")
    except Exception as e:
        # 일반 에러 메시지를 표시합니다.
        print(f"Unexpected error: {e}")

def fetch_data():
    try:
        # 데이터베이스에 연결합니다.
        conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            database=mysql_info["database"],
            cursorclass=pymysql.cursors.DictCursor 
        )

        cursor = conn.cursor()
        
        # SELECT 쿼리를 준비합니다.
        sql = "select * from user"
        
        # SQL 쿼리를 실행합니다.
        cursor.execute(sql)  
        # 결과를 가져옵니다.
        results = cursor.fetchall()

        # 기존 데이터 삭제
        for row in table.get_children():
            table.delete(row)
        
        # 결과를 출력합니다.
        for row in results:
            #print(row)  # 각 행이 딕셔너리 형태로 출력됩니다.
            table.insert("", "end", values=(row["num"],row["name"],row["age"],row["gender"]))

       
        # 연결을 닫습니다.
        cursor.close()
        conn.close()

    except pymysql.MySQLError as err:
        # 에러 메시지를 표시합니다.
        print(f"Error: {err}")
    except Exception as e:
        # 일반 에러 메시지를 표시합니다.
        print(f"Unexpected error: {e}")
      
def search_data():
    try:
        # 데이터베이스에 연결합니다.
        conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            database=mysql_info["database"],
            cursorclass=pymysql.cursors.DictCursor 
        )

        cursor = conn.cursor()
        
        # SELECT 쿼리를 준비합니다.
        name = '%'+search_entry.get() + '%'
        sql = "select * from user where name like %s"
        
        # SQL 쿼리를 실행합니다.
        cursor.execute(sql, (name,))
        # 결과를 가져옵니다.
        results = cursor.fetchall()

        # 기존 데이터 삭제
        for row in table.get_children():
            table.delete(row)
        
        # 결과를 출력합니다.
        for row in results:
            #print(row)  # 각 행이 딕셔너리 형태로 출력됩니다.
            table.insert("", "end", values=(row["num"],row["name"],row["age"],row["gender"]))

       
        # 연결을 닫습니다.
        cursor.close()
        conn.close()

    except pymysql.MySQLError as err:
        # 에러 메시지를 표시합니다.
        print(f"Error: {err}")
    except Exception as e:
        # 일반 에러 메시지를 표시합니다.
        print(f"Unexpected error: {e}")

def user_selection():
    selected_item = table.selection()  # 선택된 항목 가져오기
    if selected_item:
        item = table.item(selected_item)  # 선택된 항목의 데이터 가져오기
        values = item['values']
        num_to_delete = values[0]  # num 값 추출 (삭제할 기준)

        print(f"선택함! {num_to_delete}")
        delete_data(num_to_delete)
    else:
        print("선택한 항목이 없음!")

def delete_data(num):
    try:
        conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            database=mysql_info["database"],
            cursorclass=pymysql.cursors.DictCursor 
        )
        cursor = conn.cursor()

        # DELETE 쿼리 실행
        sql = "delete from user where num=%s"
        cursor.execute(sql, (num,))
        # 변경 사항 커밋 및 연결 종료
        conn.commit()
        cursor.close()
        conn.close()
           
        #입력한 결과 출력
        fetch_data() 
        # 성공 메시지 출력
        print("Data deleted successfully!")
        messagebox.showinfo("Info", f"선택한 {num}번의 데이터가 삭제되었습니다!!")        
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
  
def all_delete():
    # 삭제 확인 메시지박스 표시
    result = messagebox.askquestion("확인", "정말 삭제하겠습니까?")
    
    # 결과에 따라 터미널에 출력
    if result != 'yes':
        return;

    try:
        conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            database=mysql_info["database"],
            cursorclass=pymysql.cursors.DictCursor 
        )
        cursor = conn.cursor()

        # DELETE 쿼리 실행
        sql = "delete from user"
        cursor.execute(sql)
        # 변경 사항 커밋 및 연결 종료
        conn.commit()
        cursor.close()
        conn.close()
           
        #입력한 결과 출력
        fetch_data() 
        # 성공 메시지 출력
        print("Data deleted successfully!")
        messagebox.showinfo("Info", "전체삭제가 되었습니다!!")
            
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# 선택된 항목 출력 함수
def on_item_selected(event):
    selected_item = table.selection()  # 선택된 항목 가져오기
    if selected_item:
        item = table.item(selected_item)  # 선택된 항목의 데이터 가져오기
        values = item['values']  # 항목의 값을 가져옴
        unum_entry.config(state="normal")
        unum_entry.delete(0, tk.END)
        unum_entry.insert(0, values[0])
        unum_entry.config(state="readonly")

        uname_entry.delete(0, tk.END)
        uname_entry.insert(0, values[1])

        uage_entry.delete(0, tk.END)
        uage_entry.insert(0, values[2])

        ugender_entry.delete(0, tk.END)
        ugender_entry.insert(0, values[3])
 
def update_data():
    num = unum_entry.get()
    myname = uname_entry.get()
    myage = uage_entry.get()
    mygender = ugender_entry.get()

    if not num:
        messagebox.showinfo("Info", "수정할 항목을 선택해주세요!")
        return

    try:
        conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            database=mysql_info["database"],
            cursorclass=pymysql.cursors.DictCursor 
        )
        cursor = conn.cursor()
        # UPDATE 쿼리 실행
        sql = "update user set name=%s, age=%s, gender=%s where num=%s"
        cursor.execute(sql, (myname, myage, mygender, num))
        
        # 변경 사항 커밋 및 연결 종료
        conn.commit()
        cursor.close()
        conn.close()

        # 성공 메시지 출력
        print("Data updated successfully!")
        fetch_data() 
        messagebox.showinfo("Info", "수정이 완료되었습니다!")        
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# tkinter 윈도우 설정
root = tk.Tk()
root.title("정보 입력")
root.geometry("1000x800")

selected_gender = tk.StringVar(value="남성")  # "남성"으로 초기화

# 이름 입력 필드
tk.Label(root, text="이름:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# 나이 입력 필드
tk.Label(root, text="나이:").grid(row=1, column=0, padx=10, pady=10)
# 나이 선택을 위한 Combobox 생성
age_var = tk.StringVar()
age_combobox = ttk.Combobox(root, textvariable=age_var, state="readonly")

# 18부터 100까지의 나이 목록 생성
age_list = [str(i) for i in range(18, 101)]
age_combobox['values'] = age_list
age_combobox.current(0)  # 기본 선택을 18로 설정
age_combobox.grid(row=1, column=1, padx=10, pady=10)

# 성별 입력 필드
tk.Label(root, text="성별:").grid(row=2, column=0, padx=10, pady=10)

# 남성 Radiobutton
male_radio = tk.Radiobutton(root, text="남성", variable=selected_gender, value="남성")
male_radio.grid(row=2, column=1, padx=10, pady=10)

# 여성 Radiobutton
female_radio = tk.Radiobutton(root, text="여성", variable=selected_gender, value="여성")
female_radio.grid(row=2, column=2, padx=10, pady=10)

# 입력 버튼
submit_button = tk.Button(root, text="입력", command=insert_data)
submit_button.grid(row=3, columnspan=2, pady=5)

# 조회 버튼
show_button = tk.Button(root, text="조회", command=fetch_data)
show_button.grid(row=4, columnspan=2, pady=5)

# 테이블 생성
columns = ("num", "name", "age", "gender")
table = ttk.Treeview(root, columns=columns, show="headings")
table.heading("num", text="번호")
table.heading("name", text="이름")
table.heading("age", text="나이")
table.heading("gender", text="성별")

# 테이블 배치
table.grid(row=5, columnspan=2, pady=20)
# 테이블 항목 클릭 이벤트 바인딩
table.bind("<<TreeviewSelect>>", on_item_selected)

search_entry = tk.Entry(root)
search_entry.grid(row=6, column=0, padx=10, pady=5)
search_button = tk.Button(root, text="이름검색", command=search_data)
search_button.grid(row=6, column=1, pady=5)

# 삭제 버튼
delete_button = tk.Button(root, text="삭제", command=user_selection)
delete_button.grid(row=7, columnspan=2, pady=5)

# 전체삭제 버튼
all_delete_button = tk.Button(root, text="전체삭제", command=all_delete)
all_delete_button.grid(row=8, columnspan=2, pady=5)

tk.Label(root, text="번호:").grid(row=9, column=0, padx=10, pady=10)
unum_entry = tk.Entry(root, state="readonly")
unum_entry.grid(row=9, column=1, padx=10, pady=10)

tk.Label(root, text="이름:").grid(row=10, column=0, padx=10, pady=10)
uname_entry = tk.Entry(root)
uname_entry.grid(row=10, column=1, padx=10, pady=10)

tk.Label(root, text="나이:").grid(row=11, column=0, padx=10, pady=10)
uage_entry = tk.Entry(root)
uage_entry.grid(row=11, column=1, padx=10, pady=10)

tk.Label(root, text="성별:").grid(row=12, column=0, padx=10, pady=10)
ugender_entry = tk.Entry(root)
ugender_entry.grid(row=12, column=1, padx=10, pady=10)

# 수정 버튼
update_button = tk.Button(root, text="수정하기", command=update_data)
update_button.grid(row=13, columnspan=2, pady=5)

# tkinter 메인 루프 실행
root.mainloop()
