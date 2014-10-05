import glob

import matplotlib.pyplot as plt


def read_data():
    # Read the descritpion file.
    descriptions = _read_descriptions()

    # Get the names of the image files.
    img_names = glob.glob('data/*.png')

    # Make a copy of the names without the 'data' and '.png'.
    img_names_simple = [path[5:-4] for path in img_names]

    #TODO exception if img_names_simple and descriptions[0] do not match.

    # Write the data dictionary.
    data = dict()
    for i in range(len(img_names)):
        key = img_names_simple[i]

        # Get the description for this key.
        desc = None
        for desc in descriptions:
            if desc[0] == key: break
        assert desc != None

        # Add the key and description to the dictionary.
        data[key] = desc[1:]

        # Add the image name to the dictionary.
        data[key].insert(0, img_names[i])

    # Return the data dictionary.
    return data


def read_image(file_name):
    return plt.imread(file_name)


def _read_descriptions():
    # Read the raw information.
    fin = open('data/descriptions.tsv')
    raw = fin.readlines()
    fin.close()

    # Check the header and delete it.
    assert raw[0] == 'Image number\tShort description\tBonus information\n'
    del raw[0]

    # Seperate each line into it's elements.
    split = [line.split('\t') for line in raw]

    # TODO add an exception if any line doesn't have 3 elements.

    # TODO exception if there is a key collision.

    # Return the descriptions.
    return split
