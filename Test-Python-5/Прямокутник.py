def draw_rectangle(width=6, height=4, border_symbol='@', fill_symbol='&'):
    
    if width < 3 or height < 3:
        print("Сторони мають бути не меньш чим 3 ! ")
        return

    print(border_symbol * width)

    for _ in range(height - 2):
        print(border_symbol + fill_symbol * (width - 2) + border_symbol)

    print(border_symbol * width)

draw_rectangle(8, 6, '+', '-')

print("Прямокутник за замовчуванням:")
draw_rectangle()
