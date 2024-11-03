# from cube import *
# from _scramblegen import *
# from colourscanning import *
# # from cube import *
# # from _scramblegen import *
# # from views import s
# # current_cube = scramble(current_scramble)
# # #print('the scramble', stringscramble(current_scramble))

# # def return_scanned_cube():
# #     from .colourscanning import scanned_cube
# #     for i in range (len(scanned_cube)):
# #         print(scanned_cube[i][4], ':', scanned_cube[i])
# #     return scanned_cube

# # def verifiying_scanned_cube(scanned_cube):
# #     if scanned_cube == current_cube:
# #         print('Cube scrambled correctly')
# #         return True
# #     else:
# #         return False

# def verification(current_cube, scanned_cube):
#     match_counter = 0
#     colours = ['g', 'o', 'b', 'r', 'w', 'y']
#     string_cube = stringcube(current_cube)
#     print('Original Cube', string_cube)
#     print('Scanned Cube', scanned_cube)
#     if string_cube == scanned_cube:
#         return 'Successfully Scrambled!'
#     else:
#         for i in range(len(colours)):
#             match = False
#             rotate = 0
#             while rotate <= 4 and not match:
#                 current_cube.clockwise_move(i)
#                 string_cube = stringcube(current_cube)
#                 print('after rotation', string_cube[i])
#                 print('scanned cube', scanned_cube[i])
#                 if string_cube[i] == scanned_cube[i]:
#                     match = True
#                     match_counter += 1
#                 else:
#                     rotate += 1
#         print(match_counter)
#         if match_counter == 6:
#             return 'Sucessfully Scrambled!'
#         else:
#             return 'Unsuccessful, Try Again!'