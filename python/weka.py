from os import listdir
from os.path import isfile, join
from read_image import ReadImage
from logger import Logger


class Weka():
    def __init__(self, images_directory):
        self.images_directory = images_directory
        self.header = '''
                        @relation caracteristicas\n
                        @attribute bob_hair real
                        @attribute bob_pants real
                        @attribute bob_shirt real
                        @attribute krusty_hair real
                        @attribute krusty_pants real
                        @attribute krusty_shirt real
                        @attribute classe {Bob, Krusty}\n
                        @data\n
                      '''
        self.body = ''

    def list_directory_files(self):
        Logger.log('Reading all folder files')
        only_files = [f for f in listdir(self.images_directory) if isfile(
            join(self.images_directory, f))]
        Logger.log(
            f'\n{len(only_files)} images found in {self.images_directory} directory!', True)

        return only_files[610:630]
        # return only_files

    def extractTo(self, fileName):
        output_filename = fileName + '.arff'
        images_data = []

        for index, image in enumerate(list(self.list_directory_files())):
            Logger.log(f'Extracting characteristics from {image}')

            features = ReadImage().read(f'{self.images_directory}/{image}')
            features[6] = "Bob" if features[6] == 0.0 else "Krusty"
            images_data.append(features)

            Logger.log(f'Data added to index {index}')
            Logger.log('Extracted Features:')
            Logger.log(f'Bob hair = {features[0]}')
            Logger.log(f'Bob pants = {features[1]}')
            Logger.log(f'Bob shirt = {features[2]}')
            Logger.log(f'Krusty hair = {features[3]}')
            Logger.log(f'Krusty pants = {features[4]}')
            Logger.log(f'Krusty shirt = {features[5]}')
            Logger.log(f'Class = {features[6]}', True)

            self.body += ','.join(map(str, features)) + "\n"

        Logger.log(f'Writing the ARFF file {output_filename} to disk')
        with open(output_filename, 'w') as fp:
            fp.write(self.header)
            fp.write(self.body)

        Logger.log('All Done!')
        return images_data
