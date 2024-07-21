import asyncio

power_delay={5:1, 4:2, 3:3, 2:4, 1:5}

async def start_strongman(name, power, ball):
    print(f'Силач {name} начал соревнования')
    for num_ball in range (1, ball +1):
        await asyncio.sleep(power_delay[power])
        print(f'Силач {name} поднял {num_ball}')
    print(f'Силач {name} закончил соревнования')



async def start_tournament():
    print("Добро пожаловать на олимпиаду!")
    task1 = asyncio.create_task(start_strongman('Pasha', 3, 5))
    task2 = asyncio.create_task(start_strongman('Denis', 4, 5))
    task3 = asyncio.create_task(start_strongman( 'Apollon', 5, 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())