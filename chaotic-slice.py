import argparse
import pygame as pg
import random
import time
from tqdm import tqdm

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--width",
                help="output image width (in px)", default=800)
ap.add_argument("-d", "--height",
                help="output image height (in px)", default=600)
ap.add_argument("-c", "--count", help="number of points used in generation",
                default=random.randint(1, 50))
ap.add_argument("-o", "--output-dir", help="directory to place images",
                default=".")
args = ap.parse_args()

# format args
args.width = int(args.width)
args.height = int(args.height)

# Construct a pygame window for rendering
win = pg.display.set_mode((args.width, args.height))
pg.display.set_caption("Chaotic Slice. By: Evan Pratten")
win.fill((0, 0, 0))

# generate plotting equations


def genEQN():
    # Define valid chars
    valid_chars = ["y", "x", "t"]
    valid_delims = ["-", "+"]

    # Generte a random number of "modifiers" to be used
    mods_count = random.randint(1, 3)

    output = ""
    for i in range(mods_count):
        # choose a random number of chars to use in this mod
        chars_count = random.randint(1, len(valid_chars))

        for j in range(chars_count):
            # add a random char
            output += valid_chars[random.randint(1,
                                                 len(valid_chars)) - 1] + "*"

        # slice off the extra multiplication
        output = output[:-1]

        # add a random delim
        output += valid_delims[random.randint(1, len(valid_delims)) - 1]

    # slice off the extra delim
    output = output[:-1]

    return output


def randColor():
    return (
        random.randint(0, 0),
        random.randint(0, 0),
        random.randint(0, 255)
    )


y_eq = genEQN()
x_eq = genEQN()

print(x_eq.replace("*", ""), y_eq.replace("*", ""))

# Start and end *1000
start_t = 0
end_t = 1

# iter each t
for t in range(end_t - start_t):
    t -= end_t

    # iter screen x and y
    for x in tqdm(range(args.width)):
        for y in range(args.height):
            pt_x = eval(x_eq) + args.width//2
            pt_y = eval(y_eq) + args.height//2

            # Check if the points are drawable
            if 0 <= pt_x <= args.width and 0 <= pt_y <= args.height:
                # print(pt_x, pt_y)
                pg.draw.circle(win, randColor(), (pt_x, pt_y), 3, 0)
        pg.display.flip()

# save the image
pg.image.save(win, args.output_dir + str(time.time()) + ".png")