import os
from tqdm import tqdm
from shutil import copyfile

DIRS_PATH = os.path.join(os.getcwd(), 'Download')
DIRS = os.listdir(DIRS_PATH)

print('List of datasets: %s' % ' '.join(DIRS))
print('\n')

for DIR in DIRS:
    DATASET_PATH = os.path.join(DIRS_PATH, DIR)
    if os.path.isdir(DATASET_PATH):
        print('Processing dataset %s' % DIR.upper())

        DEST_DATASET = os.path.join(os.getcwd(), 'OID/Dataset/%s' % DIR)

        if not os.path.exists(DEST_DATASET):
            os.mkdir(DEST_DATASET)
            os.mkdir(os.path.join(DEST_DATASET, 'Label'))

        LABEL_PATH = os.path.join(DEST_DATASET, 'Label')

        CLASS_DIRS = os.listdir(DATASET_PATH)
        print('Found %i Classes: %s' % (len(CLASS_DIRS), ' '.join(CLASS_DIRS)))

        for CLASS in CLASS_DIRS:
            CLASS_PATH = os.path.join(DATASET_PATH, CLASS)

            if os.path.isdir(CLASS_PATH):
                files = os.listdir(CLASS_PATH)

                print('Copying %s - Found %i files' %
                      (CLASS.upper(), len(files)))

                for filename in tqdm(files):
                    if filename.endswith(".txt"):
                        copyfile(os.path.join(CLASS_PATH, filename), os.path.join(
                            os.path.join(LABEL_PATH, filename)))
                    if filename.endswith(".jpg"):
                        copyfile(os.path.join(CLASS_PATH, filename),
                                 os.path.join(DEST_DATASET, filename))
                print('\n')
