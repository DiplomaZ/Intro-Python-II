import shutil

# 100 screen width, 11char text, 90 whitespace-chars
# ----------------------------------------------------
# divide total screen width by 2 (50-5)
# assign 45th character as beginning of center string
#
screen_width, screen_height = shutil.get_terminal_size()
mid_screen = screen_width//2


def mapFormatter(new_line: str, width=0, char=" "):
    spaces = mid_screen-(len(new_line)//2)
    if(width):
        spaces = width//2-(len(new_line)//2)
    new_str = char * spaces

    return new_str + new_line

# center the middle word, relatively format the babies (KAREN TOOK THE KIDS)

# format center word by calling mapFormatter, then overwrite/insert/etc. outside words over existing whitespace


def three_args_center(new_words: list):
    word1, word2, word3 = new_words

    spaces = mid_screen-(len(word2)//2)-2
    leftWord = mapFormatter(word1+" ", spaces) + \
        ((spaces//2 - ((len(word1)//2)))*"-")
    leftWord += " " + word2 + " " + mapFormatter(" "+word3, spaces, "-")
    # try space len minus length of word (after subtracting by 2 spaces)

    return leftWord
