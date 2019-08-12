import os
from properties.p import Property


class readFiles():
    prop = Property()

    def readproperties(self, link):
        propertyline = self.prop.load_property_files(link)
        return propertyline
