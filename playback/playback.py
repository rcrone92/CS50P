in_str = input()
out_str = ""
for char in in_str:
    if char == " ":
        out_str += "..."
    else:
        out_str += char


print(out_str)
