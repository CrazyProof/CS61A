t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])

result = label(min(branches(max([t1, t2], key=label)), key=label))

# the answer is 6