# ex-0-10
Discuss

https://discuss.streamlit.io/

Explore

내가 만들고 싶은 것을 아두이노 프로그램 넣고 짜고요

파이썬 에서 프로그램를 짜고요

필요한 패키지 설치 시스템 쉘 열기 때려 넣고요

Thonny 쪽에 시스템 쉘 열기 에서 실행 프로그램 : streamlit run app1.py

요게 파이썬 에서 만들어진 HTML 폴더 입니다 주소죠 그래서 html 실행이 되는 것니다

https://ex-0-10-qejjha7ivbsvviacnp3b5d.streamlit.app/

또 한개 더 있는데요 

https://ex-0-10-kznsc5mtx9dpajsgtuintl.streamlit.app/

저게 LED PWM 프로그램 입니다 주소를 끌릭 그럼 여러분들은 제가 한 프로젝트를 

어디에 있든 조작 할수 있습니다


[여기](http://172.30.1.177:8501/) 

1.나의 mysql에 존재하는 모든 database목록을 출력해라!

show databases;

2.내가 python17이라는 이름의 데이터베이스를 사용하겠다!

use python4

3.python17이라는 DB안에있는 table목록을 조회하겠다!

show tables;

4.user라는 table이 있는데 이 table의 필드 구조를 출력해라

desc user;

1.user라는 테이블의 모든 레코드를 읽겠다!

select * from user;

새롭게 하나 더 입력 한다 그러면 2 개가 된니다

INSERT INTO user (name, age, gender) VALUES ('제네식스', 20, '남성');


2.user라는 테이블의 primary-key와 name만 읽겠다!

select num,name from user;

3.user라는 테이블의 name와 gender만 읽겠다!

select name,gender from user;

4.user라는 테이블의 primary-key가 1번인것을 조회하겠다!

select * from user where num=1;

5.user라는 테이블의 name이 제네식스인것을 조회하겠다!

select * from user where name=’제네식스’;

6.user라는 테이블의 이름이 홍으로 시작하는 사람을 조회하겠다!

select * from user where name like ‘홍%’;

7.홍길동, 홍길순이 있을때 가운데 글자가 길이 포함된 사람을 출력하겠다!

select * from user where name like ‘%길%’;

8.나이가 20~50사이인 것만 출력하스',age=30 where num=1;

1.user table에 있는 모든 데이터를 삭제하겠다!

delete from user;

2.key가 4인 레코드를 삭제하겠다!

delete from user where num=4;

3.key가 4~6범위인 레코드를 삭제하겠다!

delete from user where num>=4 and num<=6;





