def draw_line(length, symbol, horizontal):
    
    if horizontal:
        print(symbol * length)
    else:
        for _ in range(length):
            print(symbol)

draw_line(20, '@', True)
draw_line(20, '@', False)