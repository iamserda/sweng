import time

start_time = time.time()
arr = list()
for i in iter(list(range(1000000))):
    arr.append(time.time(), next(i))
print(arr)

end_time = time.time()

time_span = end_time - start_time
ctime_spent = time.ctime(time_span)
print(ctime_spent)
