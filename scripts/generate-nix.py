def main():
    print("{")
    fileLines = open("colors", "r").read().strip().splitlines();
    for i in fileLines:
        line = i.split();
        print("""  {} = {{
    colors = {{
      red     = "#{}";
      green   = "#{}";
      yellow  = "#{}";
      blue    = "#{}";
      magenta = "#{}";
      cyan    = "#{}";
      black   = "#{}";
      grey    = "#{}";
      white   = "#{}";
    }};
  }};
  """.format(line[9], line[1], line[2], line[3], line[4], \
             line[5], line[6], line[0], line[8], line[7]))
    print("}")
    

main()
