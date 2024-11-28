import time
from datetime import date, datetime, timedelta

# 오늘날짜와 년,월,일 출력
today = date.today()
print('오늘날짜', today, today.year, today.month, today.day)

print("="*30)

# 현재시각 
dtime = datetime.now()
print('현재시각', dtime)
print('년/월/일',dtime.year, dtime.month, dtime.day)
print('시/분/초/밀리셐ㄴ즈',dtime.hour, dtime.minute, dtime.second, dtime.microsecond)

print("="*30)

#날짜계산1
one_day = timedelta(days = 1)
yesterday = today - one_day
tomorrow = today + one_day
print("어제와오늘",yesterday,tomorrow)

# 날짜계산2
date_diff = today = yesterday
print("날짜차이",date_diff)

#날짜형식
date_str = today.strftime('%Y-%m-%d')
print("형식지정", date_str)

#크리스마스까지 남은 날짜 계산

#올해 크리스마스 지정
xmas_str = f'{today.year}-12-25'
#str -> datetime 타입으로 형식 변환
xmas_datetime = datetime.strptime(xmas_str, '%Y-%m-%d')
#datetime -> date 타입으로 형식 변환
xmas_date = datetime.date(xmas_datetime)
#값과 타입 확인
print(xmas_str, xmas_datetime, xmas_date)
print(type(xmas_str),type(xmas_datetime),type(xmas_date))
#크리스마스에서 오늘날짜를 빼면 남은 날짜를 계산할 수 있음.
date_diff = xmas_date - today
print("크리스마스까지1", date_diff)
print("크리스마스까지2", date_diff.days)

