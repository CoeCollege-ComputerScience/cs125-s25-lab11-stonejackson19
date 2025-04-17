blue = {"a", "b", "c", "d", "k", "l", "m", "i", "j"}
red = {"e", "f", "g", "h", "d", "n", "o", "p", "i", "j"}
green = {"q", "r", "s", "t", "k", "l", "m", "n", "o", "p", "i", "j"}

i = blue.intersection(red, green)
ii = blue - (red.union(green))
iii = red.intersection(green).union(blue.intersection(red, green))
iv = blue.intersection(red) - green
v = green.intersection(blue.union(red))

print(i)
print(ii)
print(iii)
print(iv)
print(v)