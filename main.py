from guizero import App, Box, Text

WIDTH = 200
HEIGHT = WIDTH

BAR_WIDTH = WIDTH / 20
CELL_WIDTH = int((WIDTH - 2 * BAR_WIDTH) // 3)

BAR_COLOUR = "pink"
CELL_COLOUR = "azure"

is_X = True
cells = []


def map_grid(cells):
    mapped_cells = []
    for row in cells:
        mapped_row = []
        for item in row:
            mapped_row.append(item.value)
        mapped_cells.append(mapped_row)
    return mapped_cells


def clear_grid():
    for row in cells:
        for item in row:
            item.value = ""


def end_game(winner=None):
    if winner != None:
        app.info("Game over!", f"{winner} wins the game.")
    else:
        app.info("Game Over", "The Game is a Draw")

    clear_grid()


def check_draw():
    for row in cells:
        for cell in row:
            if cell.value == "":
                return False
    end_game()


def check_winner():
    state = map_grid(cells)
    print(state)

    row0 = state[0]
    row1 = state[1]
    row2 = state[2]
    col0 = [row0[0], row1[0], row2[0]]
    col1 = [row0[1], row1[1], row2[1]]
    col2 = [row0[2], row1[2], row2[2]]
    diag1 = [row0[0], row1[1], row2[2]]
    diag2 = [row2[0], row1[1], row0[2]]

    for axis in [row0, row1, row2, col0, col1, col2, diag1, diag2]:
        if axis[0] != "" and axis[0] == axis[1] == axis[2]:
            return end_game(axis[0])

    check_draw()


def mark_cell(event):
    global is_X
    cell_text = event.widget
    if cell_text.value == "":
        if is_X:
            cell_text.value = "X"
        else:
            cell_text.value = "O"
        check_winner()
        is_X = not is_X


def create_cell(container, width, height, grid, colour):
    cell = Box(container, width=width, height=height, grid=grid)
    cell.bg = colour
    return cell











app = App(width=WIDTH, height=HEIGHT)
app.bg = "white"

board = Box(app, width=WIDTH, height=HEIGHT, layout="grid")

for y in range(5):
    if y % 2 == 0:
        row = []
        for x in range(5):
            if x % 2 == 0:
                cell = create_cell(board, CELL_WIDTH, CELL_WIDTH, [x, y],
                                   CELL_COLOUR)
                cell_text = Text(cell,
                                 text="",
                                 width=CELL_WIDTH,
                                 height=CELL_WIDTH,
                                 size=WIDTH // 10)
                cell_text.when_clicked = mark_cell
                row.append(cell_text)
            else:
                create_cell(board, BAR_WIDTH, CELL_WIDTH, [x, y], BAR_COLOUR)
        cells.append(row)
    else:
        create_cell(board, WIDTH, BAR_WIDTH, [0, y, 5, 1], BAR_COLOUR)

app.display()
