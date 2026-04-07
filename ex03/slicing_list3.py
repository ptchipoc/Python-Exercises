# pylint: disable=missing-module-docstring, invalid-name

items = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = int(len(items) / 3)
start = 0
end = chunk_size

for i in range(3):
    index = slice(start, end)

    chunk = items[index]
    print("Chunk", i, chunk)

    chunk.reverse()
    print("After reversing it", chunk)

    start = end
    end += chunk_size
