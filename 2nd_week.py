import asyncio
import random


async def do_async():
    pass

# 비동기 프로그래밍을 위한 라이브러리 : 코루틴 이용


async def fetch_data():
    print("데이터를 가져오는 중...")
    await asyncio.sleep(1)  # 데이터를 가져오는데 1초가 걸린다고 가정
    return random.randint(1, 100)


async def main():
    data = await fetch_data()
    print(f"가져온 데이터: {data}")

asyncio.run(main())

phone_book = {
    "John": "123-4567",
    "Jane": "234-5678",
    "Max": "345-6789"
}


def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "Cannot find the name in the phone book"
        name = yield phone_number


search_coroutune = search()
next(search_coroutune)

result = search_coroutune.send("John")
print(result)  # 123-4567
result = search_coroutune.send("Jane")
print(result)  # 234-5678
result = search_coroutune.send("Sarah")
print(result)  # Cannot find the name in the phone book