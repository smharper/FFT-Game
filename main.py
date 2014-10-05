import random

import input as inp
import output as out
import transform as trans


if __name__ == '__main__':
    # Print the welcome message.
    print("Let's play the FFT game!\n")

    # Print the rules.
    print("If you think you've identified the image, enter its number.")
    print("If you don't know the image, enter a '?' to get a better image.")
    print("If you are done with the game, enter a 'q' to leave.\n")

    # Read the data and make a list of keys.
    data = inp.read_data()
    keys = list(data.keys())

    # Let the user know the image options.
    message_parts = ['The possible images for this game are:']
    for i in range(len(keys)):
        message_parts.append(' [{0:d}] {1}'.format(i, data[keys[i]][1]))
    message = '\n'.join(message_parts)
    print(message)

    # Play rounds until the user quits the program.
    while True:
        key = random.choice(keys)
        selection = data[key]

        res = 0.01
        base_img = inp.read_image(selection[0])
        img = trans.transform(base_img, res)
        disp = out.display_image(img)
        print('The image for this round should be displayed now.')

        for res in [0.02, 0.04, 0.06, 0.08, 0.1, 0.2, 0.5, 1]:
            ans = input("Please enter a number, a '?', or a 'q'.\n")

            if ans.isdigit():
                if key == keys[int(ans)]:
                    print('Correct!  Moving on to the next round.\n')
                    break
                else:
                    print(":( That's wrong.  Moving on to the next round.\n")
                    break
            elif ans == '?':
                img = inp.read_image(selection[0])
                img = trans.transform(img, res)
                out.update_image(disp, img)
            elif ans == 'q':
                exit()
            #TODO add else for unexepcted options.
        out.clean_image()
