try:
    file1 = open('sample.txt','r')
    reading = file1.read()
    print(reading)
    file1.close()
except FileNotFoundError:
    print(f"The File ,{file1}, not found")
finally:
    file1.close()