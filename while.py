count = 1
while count < 11:
    print(count, end=' ')
    count += 1
else:   # 정상적인 루트가 끝났을 때 작동한다.
    print('ok')

# break, continue, else문 적용
i = 0
while i < 10:
    i += 1

    if i < 5:
        continue
    if i >= 10:
        break
    print(i, end=' ')
else:
    print('ok')
print()
# 무한루프
i = 0
while True:
    print(i, end=' ')
    if i > 5:
        break
    i += 1
else:
    print('else block')