'''
Problem 2
You are given a file temperatures_c.txt containing temperatures in Celsius, one per line. Use two context managers on a single with line to read from temperatures_c.txt and write the converted Fahrenheit values to a new file called temperatures_f.txt.

The formula to convert Celsius to Fahrenheit is: F = C * 9/5 + 32

First, run the cell below to create temperatures_c.txt. Then write your solution in the next cell.

Sample output in temperatures_f.txt

32.0
98.6
212.0
72.5
-40.0
'''

with open("temperatures_c.txt", "a+") as input_file:
    input_file.write("0\n22.2\n100\n22.5\n-40\n")
    input_file.seek(0)
    content = input_file.read()

    with open('temperatures_f.txt', 'a+') as output_file:
        for i in content.splitlines():
            if i.strip() == ' ':
                continue
            f = float(i) * (9/5) + 32
            output_file.write(f'{f}\n')

            
        # output_file.seek(0)
        # op = output_file.read()
        # print(op)