from properties.p import Property


class ReadFiles(object):
    prop = Property()

    def __init__(self, link):
        self.link = link

    def read_properties(self):
        property_line = self.prop.load_property_files(self.link)
        return property_line

    def get_datalink(self):
        dict_ = self.read_properties()
        return dict_['database_link']


if __name__ == '__main__':
    file_obj = ReadFiles('resource.properties')
    print(file_obj.get_datalink())
