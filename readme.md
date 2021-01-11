## 1. setting virtualenv

<code>pip install virtualenv</code>
<code>virtualenv venv</code>

## 2. enter virtualenv

<code>. venv/scripts/activate</code>

## 3. install pip modules

<code>pip install -r requirements.txt</code>

## 3. About Project

- 파이썬상에서의 객체 직렬화/저장/불러오기를 테스트한다.
- faker모듈을 이용해 가상의 클래스와 객체를 대량 생산하고, 저장한다.
- 엑셀 형태의 데이터시트를 저장한다.
- 생산된 객체를 pickle 모듈을 이용해 저장한다.
- 생산된 객체를 Database를 이용해 저장한다. (PostgreSQL 이용)
- 생산된 객체 데이터를 프로그램 시작 시 불러오고, 직렬화한다.
