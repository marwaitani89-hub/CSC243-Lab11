from ScubaTank import ScubaTank

t = ScubaTank("A", 80)

print(t)

t.fill(40)
print(t.get_bar())

t.set_bar(250)
print(t)

t.set_bar(400)
print(t.get_bar())

t.release(0)
t.release(100)
print(t) 