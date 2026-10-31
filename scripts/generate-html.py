def main():
    print("""
<!DOCTYPE html>
<html>
<head>
<style>
</style>
</head>
<body>
""")
    fileLines = open("colors", "r").read().strip().splitlines();
    print("<pre style=\"font-family: monospace; font-size: 16px\">", end = "")
    for rawLine in fileLines:
        line            = rawLine.split()
        colorschemeName = line[9]
        bg              = line[0]
        fg              = line[7]
        output = ""
        output += "<span style=\"background: #{}; color: #{};\">".format(bg, fg)
        for i in range(8):
            color = line[1 + i]
            output += "<span style=\"color: #{};\">#{} </span>".format(color, color)
        output += "     {:<40}".format(colorschemeName)
        output += "</span>"
        print(output)
    print("</pre>")
    print("""
</body>
</html>
""")
    

main()
