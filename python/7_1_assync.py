import asyncio

async def say_hello():
    print("Привет")
    await asyncio.sleep(1)  # ждем 1 секунду, но не блокируем всё
    print("Через секунду!")

asyncio.run(say_hello())


async def task(name, delay):
    print(f"{name} стартует")
    await asyncio.sleep(delay)
    print(f"{name} завершена")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )

asyncio.run(main())
