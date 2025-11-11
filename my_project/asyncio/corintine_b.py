import aiofiles
import asyncio
import time

async def my_coroutine(name: str):
    print(f"{name} - Coroutine started")
    await asyncio.sleep(1)
    print(f"{name} - Writing to file")
    with open("sample.txt", mode="a") as f:
        f.write(f"{name} - Writing to file\n")
    with open("sample.txt", mode="a") as f:
        f.write(f"{name} - Writing to file\n")
    with open("sample.txt", mode="a") as f:
        f.write(f"{name} - Writing to file\n")
    with open("sample.txt", mode="a") as f:
        f.write(f"{name} - Writing to file\n")
    with open("sample.txt", mode="a") as f:
        f.write(f"{name} - Writing to file\n")

    print(f"{name} - Coroutine finished")
    return "Result from coroutine"

async def main():
    # a is a corinutine object
    # a =  my_coroutine("Direct Call")

    # task3 is a Task object
    # task3 = asyncio.create_task(a)
    # print(type(task3))
    
    start = time.time()
    task1 = asyncio.create_task(my_coroutine("Task 1"))
    task2 = asyncio.create_task(my_coroutine("Task 2"))
    c = asyncio.gather(task1, task2)
    print(type(c))
    results = await c
    print(results)
    print(f"Finished in {time.time() - start} seconds")
if __name__ == "__main__":
    asyncio.run(main())