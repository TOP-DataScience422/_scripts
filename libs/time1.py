from time import perf_counter, sleep

start = perf_counter()
sleep(0.015)
end = perf_counter()

print(f'время выполнения: {(end - start)*1000:.2f} мс')
