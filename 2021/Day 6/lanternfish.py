def part_1() -> None:
    with open('input') as file:
        batch = [int(x) for x in file.read().split(',')]
    
    def add_1_day(batch: list[int]) -> list[int]:
        batch = [x - 1 if x > 0 else 10 for x in batch]
        new_fish = batch.count(10)
        for _ in range(new_fish):
            batch.append(8)
        batch = [x if x < 9 else 6 for x in batch]

        return batch
    
    for i in range(1, 257):
        batch = add_1_day(batch)
        print(i)

    print('answer part 1:', len(batch))

part_1()