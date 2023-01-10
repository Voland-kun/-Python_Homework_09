# Доделывать "интеллект" в старой домашней работе не стал, оставил только "мультиплеер".

from tkinter import *
from random import randint

game_flag = False
turn_count = 0
field=[]
player1 = 'Игрок1'
player2 = 'Игрок2'
players = [player1, player2]
player_count = 0
char = ['X', 'O']

def click(row, col):
    global turn_count 
    global player_count
    if game_flag and field[row][col]['text'] == ' ':
        field[row][col]['text'] = char[turn_count%2]
        turn_count += 1
        player_count += 1
        if game_flag and turn_count > 4:
            win_condition()
        player_name = Label(root, text=f'Ходит {players[(player_count)%2]}')
        player_name.grid(row=0, column=0, columnspan=3, sticky='nsew')

def win_condition():
    global game_flag
    for i in char:
        if field[0][0]['text']==field[0][1]['text']==field[0][2]['text']==i\
            or field[1][0]['text']==field[1][1]['text']==field[1][2]['text']==i\
            or field[2][0]['text']==field[2][1]['text']==field[2][2]['text']==i\
            or field[0][0]['text']==field[1][0]['text']==field[2][0]['text']==i\
            or field[0][1]['text']==field[1][1]['text']==field[2][1]['text']==i\
            or field[0][2]['text']==field[1][2]['text']==field[2][2]['text']==i\
            or field[0][0]['text']==field[1][1]['text']==field[2][2]['text']==i\
            or field[0][2]['text']==field[1][1]['text']==field[2][0]['text']==i:
            winwin = Toplevel()
            winwin.geometry('200x150')
            winwin['bg'] = 'grey'
            winwin.overrideredirect(True)
            Label(winwin, text=f'Победил {players[(player_count+1)%2]}', bg='gray', font =("Arial", 14))\
            .pack(expand=1)
            Button(winwin, text = 'OK', command = winwin.destroy)\
                .pack()
            x = root.winfo_x()
            y = root.winfo_y()
            winwin.geometry("+%d+%d" % (x + 35, y + 105))
            game_flag = False
        else:
            if turn_count == 9:
                drawwin = Toplevel()
                drawwin.geometry('200x150')
                drawwin['bg'] = 'grey'
                drawwin.overrideredirect(True)
                Label(drawwin, text=f'Ничья', bg='gray', font =("Arial", 14))\
                .pack(expand=1)
                Button(drawwin, text = 'OK', command = drawwin.destroy)\
                    .pack()
                x = root.winfo_x()
                y = root.winfo_y()
                drawwin.geometry("+%d+%d" % (x + 35, y + 105))
                game_flag = False

def start_game():
    a.destroy()
    global game_flag 
    game_flag = True

def new_game():
    global player_count
    global a
    global turn_count
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    player_count = randint(0, 1)
    if player_count == 1:
        coin_text = f'Выпала решка,\n первым ходит {players[(player_count)%2]}'
    else:
        coin_text = f'Выпал орёл,\n первым ходит {players[(player_count)%2]}'
    Label(a, text=coin_text, bg='gray', font =("Arial", 14))\
        .pack(expand=1)
    Button(a, text = 'OK', command = start_game)\
        .pack()
    x = root.winfo_x()
    y = root.winfo_y()
    a.geometry("+%d+%d" % (x + 35, y + 105))
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
    turn_count = 0
    player_name.config(text=f'Ходит {players[(player_count)%2]}')

root = Tk()
root.title('Крестики-нолики')
root.geometry('+600+300')
root.resizable(False, False)
player_name = Label(root, text='Имя игрока')
player_name.grid(row=0, column=0, columnspan=3, sticky='nsew')
for row in range(1,4):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='#e8e8e8',
                        bd=1,
                        command=lambda row=row-1, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='Новая игра', command = new_game)
new_button.grid(row=4, column=0, columnspan=3, sticky='nsew')

root.mainloop()