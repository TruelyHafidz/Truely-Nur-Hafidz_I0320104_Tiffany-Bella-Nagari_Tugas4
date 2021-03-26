a = 4            # 4  = 0000 0100
b = 11           # 11 = 0000 1011

c = a | b;       # 15 = 0000 1111
print("line 1 - Value of c is", c)

c = a >> b;      # 0 = 0000 0000
print("line 2 - Value of c is", c)

c = a ^ b;       # 15 = 0000 1111
print("line 3 - Value of c is", c)

c = ~a;          # -5 = 1111 1011
print("line 4 - Value of c is", c)

c = a & b;       # 0 = 0000 0000
print("line 5 - value if c is", c)