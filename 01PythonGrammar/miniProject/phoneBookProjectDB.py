import sqlite3


# sqlite 연결 및 db파일 생성
conn = sqlite3.connect("./saveFiles/phoneBook.db")
# 커서 생성
curs = conn.cursor()

try:
    tb1cmd = "create table phoneBookList(pId integer primary key autoincrement, name char, phone char, addr char)"

    curs.execute(tb1cmd)
except Exception as e:
    print("[예외발생]테이블은 이미 생성되었습니다.", e)


pList = []


def menu():
    print("1.입력 2.출력 3. 검색 4.수정 5.삭제")
    print("6.종료")
    return input("번호선택:")


def insert(name, phone, addr):

    curs.execute(
        "INSERT INTO phoneBookList (name, phone, addr) VALUES (?, ?, ?)",
        (name, phone, addr),
    )
    conn.commit()
    print("입력 완료.")


def show():
    curs.execute("select * from phoneBookList")
    pList = curs.fetchall()

    if pList:
        print(f"{'번호':>3} {'이름':>6} {'전화번호':>15} {'주소':>17}")
        print(f"{'':-^74}")

        for data in pList:
            print(f"  {data[0]:<5}  {data[1]:<10}  {data[2]:<15}  {data[3]:<20}")
            print(f"{'':-^74}")


def search():
    word = input("검색할 이름 : ")

    curs.execute("select * from phoneBookList where name = ? ", (word,))
    pList = curs.fetchall()

    print(f"{'':-^74}")
    for data in pList:
        if word in data[1]:
            print(f"{'번호':>3} {'이름':>6} {'전화번호':>15} {'주소':>17}")
            print(f"{'':-^74}")
            print(f"  {data[0]:<5}  {data[1]:<10}  {data[2]:<15}  {data[3]:<20}")
            print(f"{'':-^74}")
    else:
        print("검색 결과가 없습니다.")


def modify(nName, nPhone, nAddr, word):

    curs.execute('SELECT name, phone, addr FROM phoneBookList WHERE name = ?', (word,))
    src_pList = curs.fetchone()

    if not src_pList:
        print(f"'{word}'의 데이터가 존재하지 않습니다.")
        return

    nName = nName if nName else src_pList[0]
    nPhone = nPhone if nPhone else src_pList[1]
    nAddr = nAddr if nAddr else src_pList[2]

    curs.execute(
        "update phoneBookList set name =?, phone = ?, addr = ? where name = ? ",
        (nName, nPhone, nAddr, word),
    )
    conn.commit()

    if curs.rowcount > 0:
        print(f"'{word}'의 데이터가 수정되었습니다.")
        print(f"{'':-^74}")
    else:
        print(f"'{word}'의 데이터가 존재하지 않거나 수정되지 않았습니다.")
        print(f"{'':-^74}")


def delete(word):

    curs.execute("delete from phoneBookList where name = ?", (word,))
    conn.commit()

    if curs.rowcount > 0:
        print(f"'{word}'의 데이터가 삭제되었습니다.")
        print(f"{'':-^74}")
    else:
        print(f"'{word}'의 데이터가 존재하지 않습니다.")
        print(f"{'':-^74}")


choice = 0

while True:

    choice = int(menu())

    if choice == 1:
        print(f"{'입력기능':-^70}")

        name = input("이름: ")
        phone = input("전화번호: ")
        addr = input("주소: ")
        insert(name, phone, addr)
        
    if choice == 2:
        print(f"{'출력기능':-^70}")
        show()

    if choice == 3:
        print(f"{'검색기능':-^70}")
        search()

    if choice == 4:
        print(f"{'수정기능':-^70}")

        word = input("수정할 전화번호부의 이름: ")
        nName = input("수정할 이름: ")
        nPhone = input("수정할 전화번호: ")
        nAddr = input("수정할 주소: ")

        modify(nName, nPhone, nAddr, word)

    if choice == 5:
        print(f"{'삭제기능':-^70}")

        word = input("삭제할 전화번호부의 이름: ")
        delete(word)

    if choice == 6:
        break

print("종료!")
