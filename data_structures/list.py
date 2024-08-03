days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# method

print(days_of_week.count("Wed"))
# count: list 내 특정 value의 개수 카운트
# result: 1

days_of_week.reverse()
print(days_of_week)
# reverse: list 순서를 거꾸로
# result: ['Fri', 'Thu', 'Wed', 'Tue', 'Mon']

days_of_week.append("Sun")
print(days_of_week)
# append: list의 끝에 새로운 value 추가
# result: ['Fri', 'Thu', 'Wed', 'Tue', 'Mon', 'Sun']

days_of_week.remove("Mon")
print(days_of_week)
# remove: list의 특정 value 삭제
# result: ['Fri', 'Thu', 'Wed', 'Tue', 'Sun']

days_of_week.clear()
print(days_of_week)
# clear: 닉값
# result: []