import time

start_time = time.time()
arr = list()
for i in range(10000000):
    elem = (time.time(), i)
    arr.append(elem)

end_time = time.time()
time_span = end_time - start_time
print(f"started_at: {time.ctime(start_time)}")
print(f"finished_at: {time.ctime(end_time)}")
print(f"elapsed_time: {"{}".format(round(time_span, 2), )}")
