import os
import numpy as np

# file1 = open(os.path.join(os.path.dirname(__file__), 'testinput.txt'), 'r')
file1 = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
lines = file1.readlines()


coordinate_pairs = []

max_x = 0
max_y = 0
for line in lines:
    start, end = line.strip().split("->")

    start_x_str, start_y_str = start.split(",")
    end_x_str, end_y_str = end.split(",")

    print("start: " + start_x_str + ", "+ start_y_str)
    print("end: " + end_x_str + ", " +end_y_str)


    start_x = int(start_x_str)
    start_y = int(start_y_str)

    end_x = int(end_x_str)
    end_y = int(end_y_str)

    if start_x > max_x:
        max_x = start_x
    if end_x > max_x:
        max_x = end_x

    if start_y > max_y:
        max_y = start_y
    if end_y > max_y:
        max_y = end_y

    coordinate_pairs.append(((start_x, start_y), (end_x, end_y)))

    # print(start)
    # print(end.strip())

print(max_x)
print(max_y)
print(coordinate_pairs)

grid = np.zeros((max_y + 1, max_x + 1))

print(grid)



for coordinate_pair in coordinate_pairs:
    # Either vertical or horizontal line only
    print(coordinate_pair)
    if (coordinate_pair[0][0] == coordinate_pair[1][0] or coordinate_pair[0][1] == coordinate_pair[1][1]):
        if (coordinate_pair[0][0] == coordinate_pair[1][0]):
            x_val = coordinate_pair[0][0]
            y_start = 0
            y_end = 0
            if (coordinate_pair[0][1] < coordinate_pair[1][1]):
                y_start = coordinate_pair[0][1]
                y_end = coordinate_pair[1][1]
            else : 
                y_start = coordinate_pair[1][1]
                y_end = coordinate_pair[0][1]
            print("vertical line! x val: " + str(coordinate_pair[0][0]))
            print("ystart: " + str(y_start) + " yend: " + str(y_end))

            for y in range(y_start, y_end + 1):
                grid[y][x_val] += 1


        elif(coordinate_pair[0][1] == coordinate_pair[1][1]):
            y_val = coordinate_pair[0][1]
            x_start = 0
            x_end = 0
            if (coordinate_pair[0][0] < coordinate_pair[1][0]):
                x_start = coordinate_pair[0][0]
                x_end = coordinate_pair[1][0]
            else : 
                x_start = coordinate_pair[1][0]
                x_end = coordinate_pair[0][0]
            print("horizontal line! y val: " + str(y_val))
            print("xstart: " + str(x_start) + " xend: " + str(x_end))

            for x in range(x_start, x_end + 1):
                grid[y_val][x] += 1
    else :
        print ("diagional line")








print(grid)





arr = np.array(grid)

count = np.count_nonzero(arr > 1)

print(count)






# def find_num_in_row(num, row):
#     for i in range(len(row)):
#         val = row[i]
#         if num == val:
#             return i
#     return -1


# def is_board_bingo(board):
#     for row in board:
#         print(row)
#         array = np.array(row)
#         num_zero = array.size - np.count_nonzero(array)
#         print(num_zero)
#         if num_zero == 5:
#             return True
    
#     rotated = list(zip(*board))[::-1]
#     for row in rotated:
#         print(row)
#         array = np.array(row)
#         num_zero = array.size - np.count_nonzero(array)
#         print(num_zero)
#         if num_zero == 5:
#             return True
#     return False

# # test_board = [[0, 0, 2, 0, 0], [10, 16, 15, 9, 0], [18, 8, 23, 26, 0], [0, 0, 2, 0, 0], [2, 0, 12, 3, 0]]
# # print("testboardbingo")
# # print(is_board_bingo(test_board))
        



# bingo_order = list( map( int, lines[0].strip().split(",")))
# print(bingo_order)

# # go through all remaining lines, build list of all 5x5 boards
# all_boards = []

# for line_index in range(2, len(lines), 6):
#     # print(str(line_index) + " - " + lines[line_index])

#     # Reset and build new board
#     current_board = []
#     current_board.append(list( map( int, lines[line_index].strip().split())))
#     current_board.append(list( map( int ,lines[line_index + 1].strip().split())))
#     current_board.append(list( map( int, lines[line_index + 2].strip().split())))
#     current_board.append(list( map( int, lines[line_index + 3].strip().split())))
#     current_board.append(list( map( int, lines[line_index + 4].strip().split())))

#     print(current_board)
#     all_boards.append(current_board)


# winning_board = None
# win_index = len(bingo_order)
# # For each board
# for board in all_boards:
#     print("playing bingo for board:")
#     print(board)
#     bingo_index = 0
#     win = False
#     # go through bingo numbers
#     while not win and bingo_index < win_index:
#         bingo_num = bingo_order[bingo_index]
        
#         # for each number, find index if it exists in a row
#         row_index = 0
#         for row in board:
#             in_row_index = find_num_in_row(bingo_num, row)
#             # if it's found, turn the element at index to 0
#             if in_row_index >= 0:
#                 row[in_row_index] = 0
#                 # check for bingo winner here
#                 if is_board_bingo(board):
#                     print("bingo found! board:")
#                     print(board)
#                     win = True
#                     break
#         if win :
#             break
#         bingo_index += 1
#     if (win and bingo_index < win_index):
#         win_index = bingo_index
#         winning_board = board

# print(winning_board)




# # play through bingo until it wins or takes more than a previous board, save the number of turns it took to win and the final board
# # if it doesn't win, don't save, or if it wins with more moves than previous then don't save

# # Calculate final score




# # for bingo_draw in bingo_order:
# #     print(bingo_draw)




# print(bingo_order)
# print('win_index: ' + str(win_index))



# board_score = sum(sum(winning_board,[]))
# winning_num = bingo_order[win_index]
# print("board score: " + str(board_score))
# print("winning number:" + str(winning_num))
# print("final_score: " + str(board_score * winning_num))