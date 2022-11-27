from PIL import Image, ImageDraw, ImageFont

import Board as b


def getmax(board):
    MAX = 0
    for line in board.horizontalVector:
        MAX = max(MAX, len(line))
    for line in board.verticalVector:
        MAX = max(MAX, len(line))
    return MAX


def draw(board):
    linewidth = 4

    maxlen = getmax(board)

    SIDE = (max(board.rows, board.cols) + maxlen) * 40
    image = Image.new('RGB', (SIDE + int(linewidth / 2), SIDE + int(linewidth / 2)), (255, 255, 255))

    img = ImageDraw.Draw(image)

    side = SIDE / (maxlen + board.rows)

    for row in range(board.rows + 1):
        img.line((0, side * (maxlen + row), image.size[0], side * (maxlen + row)), fill=0, width=linewidth)
    for col in range(board.cols + 1):
        img.line((side * (maxlen + col), 0, side * (maxlen + col), image.size[1]), fill=0, width=linewidth)

    font = ImageFont.truetype("arial.ttf", 30)
    for n, line in enumerate(board.verticalVector):
        for c, num in enumerate(line):
            _, _, w, h = img.textbbox((0, 0), str(num), font=font)
            img.text(((n + maxlen) * side + (side - w) / 2, (maxlen - len(line) + c) * side + (side - h) / 2), str(num),
                     (0, 0, 0),
                     font=font)

    for n, line in enumerate(board.horizontalVector):
        for r, num in enumerate(line):
            _, _, w, h = img.textbbox((0, 0), str(num), font=font)
            img.text((((maxlen - len(line) + r) * side) + (side - w) / 2, (n + maxlen) * side + (side - h) / 2),
                     str(num), (0, 0, 0),
                     font=font)

    image.show()
    image.save("image.png", "PNG")


def drawSudoku(sudoku):
    linewidth = 4
    linewidth2 = 2

    SIDE = 9 * 40
    image = Image.new('RGB', (SIDE + int(linewidth / 2), SIDE + int(linewidth / 2)), (255, 255, 255))
    img = ImageDraw.Draw(image)

    side = SIDE / 9

    for row in range(10):
        if row % 3 == 0:
            img.line((0, side * row, image.size[0], side * row), fill=0, width=linewidth)
        else:
            img.line((0, side * row, image.size[0], side * row), fill=0, width=linewidth2)
    for col in range(10):
        if col % 3 == 0:
            img.line((side * col, 0, side * col, image.size[1]), fill=0, width=linewidth)
        else:
            img.line((side * col, 0, side * col, image.size[1]), fill=0, width=linewidth2)


    font = ImageFont.truetype("arial.ttf", 30)
    for n, line in enumerate(sudoku):
        for c, num in enumerate(line):
            if num != 0:
                _, _, w, h = img.textbbox((0, 0), str(num), font=font)
                img.text((n * side + (side - w) / 2, c * side + (side - h) / 2), str(num), (0, 0, 0), font=font)

    image.save("sudoku.png", "PNG")
