import streamlit as st
import pandas as pd
import subprocess

# Flask 서버 시작
def start_flask_server():
    subprocess.Popen(['python', 'flask_server.py'])

start_flask_server()

# 조회수 데이터를 저장할 리스트
view = [100, 150, 30]

# 조회수 데이터를 업데이트하는 함수
def update_views(new_value):
    try:
        new_value = int(new_value)
        view.append(new_value)
        st.success(f"{new_value} 조회수가 추가되었습니다!")
    except ValueError:
        st.error("숫자를 입력해 주세요.")

# 메인 앱 함수
def main():
    st.write('# YouTube 조회수')

    # 기존 조회수 데이터 표시
    st.write('## 원본 데이터')
    st.write(view)

    # 바 차트 표시
    st.write('## 바 차트')
    st.bar_chart(view)

    # 사용자가 입력할 수 있는 텍스트 박스
    new_value = st.text_input('새로운 조회수를 입력하세요:', '')

    # 입력된 값이 있을 때 업데이트 함수 호출
    if st.button('조회수 추가'):
        update_views(new_value)

    # 서버 주소 입력 받기
    server_url = st.text_input('서버 주소를 입력하세요:', 'https://USERNAME.github.io/REPOSITORY_NAME/')

    # 서버로 이동할 링크 생성
    st.markdown(f'[서버로 이동하기]({server_url})')

    # 업데이트된 데이터를 판다스 시리즈로 변환하여 표시
    sview = pd.Series(view)
    st.write('## 판다스 시리즈')
    st.write(sview)

# 앱 실행
if __name__ == '__main__':
    main()
