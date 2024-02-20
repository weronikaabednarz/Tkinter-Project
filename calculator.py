import tkinter

symbols = ['7','8','9','/','\u21BA','C','4','5','6','*','(',')','1','2','3','-','x^2','\u221A','0',',','%','+']

           
def window_initialisation():
    window = tkinter.Tk()
    window.configure(bg='light grey')
    window.geometry('430x390')
    window.title('Calculator')

    return window

def screen_initialisation(window):

    screen = [tkinter.Label(window, bg='#C0CBCB', width=60, anchor = 'w', borderwidth = 2) for i in range(3)]

    for i in range(len(screen)):
        screen[i].grid(row = i, columnspan = 6, ipady = 15, ipadx = 1)

    return screen

def data_field_initialisation(window,screen):
    data_field = tkinter.Entry(window, borderwidth = 0)
    data_field.grid(row = len(screen), columnspan = 6, ipadx = 154, ipady = 10)

    info = tkinter.Label(window, bg = 'white', width = 60, anchor = 'w', borderwidth = 2)
    info.grid(row = len(screen) + 1, columnspan = 6, ipady = 15, ipadx = 1)

    return data_field, info

def button_click(data_field, symbol):
    def f():

        if symbol == '\u21BA':
            buffer = data_field.get()[:-1]
            data_field.delete(0, tkinter.END)
            data_field.insert(0, buffer)

        elif symbol == 'C':
            data_field.delete(0,tkinter.END)
        else:
            note = symbol if symbol != 'x^2' else '^2'
            data_field.insert(tkinter.END,note)
    
    return f

def count(data_field, screen,info):

    def correct_last_sign(tekst):
        i = 1
        while tekst[-i] == ')':
            i+=1
        return tekst[-i].isdigit()
    
    def multiple_operators(tekst):
        for i in range(len(tekst)):
            if not tekst[i].isdigit() and not tekst[i+1].isdigit():
                return True
        return False
    
    def swap_sign(tekst):
        for i in range(len(tekst)):
            if tekst[i] =='^':
                tekst = tekst[: i] + '**' + tekst[i+1 :]
        return tekst
    
    def f():
        tekst = data_field.get()

        if not correct_last_sign(tekst) or multiple_operators(tekst):
            info['text'] = 'Wrong expression!!!'
        
        else:

            for i in range(1, len(screen)):
                if screen[i]['text']:
                    screen[i-1]['text'] = screen[i]['text']

            if '^' in tekst:
                expression = swap_sign(tekst)
                screen[-1]['text']= tekst + '=' + str(eval(expression))

            else:
                screen[-1]['text']= tekst + '=' + str(eval(tekst))

    return f

def buttons_initialisation(window, screen, info):
    buttons = [tkinter.Button(window,text=symbol,bg='light grey', borderwidth = 0) for symbol in symbols]

    j = len(screen) + 2
    for i in range(len(buttons)):
        if i % 6 == 0:
            j += 1
        margin = 21 if len(symbols[i]) == 1 else 5
        buttons[i].grid(row = j, column = i % 6, ipady = 5, ipadx = margin)
        buttons[i].configure(command=button_click(data_field, buttons[i]['text']))

    equal_button = tkinter.Button(window, text = '=', bg = '#00BFFF',borderwidth=0,command=count(data_field, screen,info))
    equal_button.grid(row=len(screen)+ 6, column = 4, columnspan = 2, ipady = 5, ipadx = 50)
    return buttons

if __name__ == '__main__':      
                                
    window = window_initialisation()
    screen = screen_initialisation(window)
    data_field, info = data_field_initialisation(window,screen)
    buttons = buttons_initialisation(window, screen, info)
    window.mainloop()