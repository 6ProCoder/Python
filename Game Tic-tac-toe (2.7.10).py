import Tkinter as tk  # Note the capital 'T' in 'Tkinter'

# Create the main window
root = tk.Tk()
root.title("Mini Game")
# Create a 3x3 grid of buttons
buttons = []
for row in range(3):
    for col in range(3):
        button_text = ' '
        button = tk.Button(root, text=button_text, font=('Helvetica', 24), width=5, height=2)
        button.grid(row=row, column=col)
        button_row, button_col = row, col
        button.config(command=lambda row=button_row, col=button_col: play_move(row, col) if get_button(row, col)['text'] == ' ' else None)
        buttons.append(button)

# Keep track of whose turn it is
current_player = 'X'

def get_button(row, col):
    return buttons[row * 3 + col]

# Function to play a move
def play_move(row, col):
    global current_player
    buttons[row * 3 + col]['text'] = current_player
    buttons[row * 3 + col]['state'] = 'disabled'
    if check_win(row, col, current_player):
        print('Player %s wins!' % current_player)
    current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a win
def check_win(row, col, player):
    return (
        # Check rows
        all([get_button(row, idx)['text'] == player for idx in range(3)]) or
        # Check columns
        all([get_button(idx, col)['text'] == player for idx in range(3)]) or
        # Check diagonals
        (row == col and all([get_button(idx, idx)['text'] == player for idx in range(3)])) or
        (row + col == 2 and all([get_button(idx, 2 - idx)['text'] == player for idx in range(3)]))
    )

# Function to clear the existing board
def clear_board():
    for button in buttons:
        button['text'] = ' '
        button['state'] = 'normal'

# Create and place the "Replay" button
replay_button = tk.Button(root, text="Replay", command=clear_board, font=('Helvetica', 24), width=10, height=2)
replay_button.grid(row=3, column=0, columnspan=3)

# Disable all buttons to start the game
for button in buttons:
    button['state'] = 'disabled'

# Start the main loop
root.mainloop()
