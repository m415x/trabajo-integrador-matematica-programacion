from time import sleep

for i in range(16):
    print(f"{bin(i)[2:].zfill(4)}")
    sleep(1)
