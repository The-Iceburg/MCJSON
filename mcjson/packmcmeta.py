# imports the json module
import json

# defines the packMcMeta Class
class packMcMeta:

    # outlines all the versions and their equivilent resource pack codes
    resourcePackFormatCodes = { "1.14": 4,   "1.14.1": 4, "1.14.2": 4, "1.14.3": 4, "1.14.4": 4,
                                "1.15": 5,   "1.15.1": 5, "1.15.2": 5, "1.16": 5,   "1.16.1": 5,
                                "1.16.2": 6, "1.16.3": 6, "1.16.4": 6, "1.16.5": 6,
                                "1.17": 7,   "1.17.1": 7,
                                "1.18": 8,   "1.18.1": 8, "1.18.2": 8,
                                "1.19": 9,   "1.19.1": 9, "1.19.2": 9                            }

    # defines the initialise function which takes vesion and description arguments
    def __init__(self, version, description):

        # sets the objects pack_format code to the appropriate number in relation to the parssed version
        self.pack_format = packMcMeta.resourcePackFormatCodes[version]

        # sets the desciption of the object as the parsed desciption
        self.description = description

    # defines the file output function taking output type and location arguments
    def fileOutput(self, OutputType, location):

        # outlines the base to be built upon
        packMetaDict = {"pack" : {"pack_format": 0, "description": ""}}

        # assigns the objects pack_format code to the pack_format key
        packMetaDict["pack"]["pack_format"] = self.pack_format

        # assigns the objects desciription code to the description key
        packMetaDict["pack"]["description"] = self.description

        # if the output type parsed is file
        if OutputType == "file":

            # creates a new file at the outlined location
            with open(location, "w+") as f:

                # writes the appropriate data to that file
                f.write(json.dumps(packMetaDict))

        # if the output type parsed is dictionary
        elif OutputType == "dict":

            # returns the dictionary
            return packMetaDict

        # if the output type parsed is string
        elif OutputType == "str":

            # returns the dictionary as a string
            return str(packMetaDict) 

    # defines the update version function taking the version number as an arguments
    def updateVersion(self, version):

        # sets the objects pack_format code to the appropriate number in relation to the parssed version
        self.pack_format = packMcMeta.resourcePackFormatCodes[version]

    # defines the update description function taking the description as an arguments
    def updateDescription(self, description):

        # sets the desciption of the object as the parsed desciption
        self.description = description