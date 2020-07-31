import os
from tqdm import tqdm
from shutil import copyfile

DIRS_PATH = os.path.join(os.getcwd(), 'OID/Dataset')
DIRS = os.listdir(DIRS_PATH)

print('List of datasets: %s' % ' '.join(DIRS))
print('\n')

for DIR in DIRS:
    DATASET_PATH = os.path.join(DIRS_PATH, '%s/AllClasses' % DIR)
    if os.path.isdir(DATASET_PATH):
        print('Processing dataset %s' % DIR.upper())

        DEST_IMG = os.path.join(
            DATASET_PATH, 'images')
        DEST_LABEL = os.path.join(
            DATASET_PATH, 'labels')

        if not os.path.exists(DEST_IMG):
            os.mkdir(DEST_IMG)
        if not os.path.exists(DEST_LABEL):
            os.mkdir(DEST_LABEL)

        files = os.listdir(DATASET_PATH)
        for filename in tqdm(files):
            if filename.endswith(".xml"):
                copyfile(os.path.join(DATASET_PATH, filename), os.path.join(
                    os.path.join(DEST_LABEL, filename)))
            if filename.endswith(".jpg"):
                copyfile(os.path.join(DATASET_PATH, filename),
                         os.path.join(DEST_IMG, filename))
        print('\n')
