import streamlit as st

# 메인 앱 함수
def main():
    st.title("서버 주소 입력 폼")
    
    # 서버 주소 입력 받기
    server_url = st.text_input('서버 주소를 입력하세요:', 'http://172.30.1.177:8501')

    # 서버로 이동할 링크 생성 버튼
    if st.button('서버로 이동하기'):
        st.markdown(f'[서버로 이동하기]({server_url})', unsafe_allow_html=True)

# Streamlit 앱 실행
if __name__ == '__main__':
    main()
