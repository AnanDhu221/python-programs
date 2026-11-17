# a={}
# b=set()

# print(type(a))
# print(type(b))

# -------------------------------

# colors={"red","green","blue"}

# print(colors[1])  = error

# -----------------------------------

# colors={"red","green","blue"}

# print(colors[1])  

# for color in colors:
#     print(color)

# colors.add("yellow")
# print(colors)

# colors.update(["orange","pink","magenta"])
# print(colors)

# colors.remove("orange")
# print(colors)

# colors.discard("black")
# print(colors)

# removed=colors.pop()
# print(colors)
# print(removed)

# colors.clear()
# print(colors)

# print("red" in colors)
# print("black in colors")
# print("black not in colors")

# --------------------------------------

# batch05={"pawan","edwin","joshwa"}
# batch06={"jac","anjana","nandana"}
# batch0506=batch05|batch06
# print(batch0506)

# batch0506=batch05.union(batch06)
# print(batch0506)

# batch0506=batch05.intersection(batch06)
# print(batch0506)

# result=batch05.difference(batch06)
# print(result)

# result=batch05.symmetric_difference(batch06)
# print(result)

# -----------------------------------

# frozenset

# colors={"red","green","blue"}
# freezed_colors=frozenset(colors)

# freezed_colors.add("black")
# print(freezed_colors)

# --------------------------------------

# batch={
# frozenset({"Anu","Bhavaya"}):"batch05",
# frozenset({"Jose","Karthika"}):"batch06"
 
# }
# print(batch[frozenset({"Anu","Bhavaya"})])
