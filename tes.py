import time
def test_time():
    start_time = time.time()
    print('start')
    time.sleep(2)
    print('end')
    end_time = time.time()
    mesc = (end_time - start_time) * 1000
    print('time is %d  ms' %mesc)

test_time()