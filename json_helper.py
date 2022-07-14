import json, os, pickle


def read_json(file_path):
    file = open(file_path)
    data = json.loads(file.read())
    return data

def write_pickle(file_path, data_to_pickle):

    with open(file_path + '/super_smash_characters.pickle', 'wb') as f:
        pickle.dump(data_to_pickle, f)


#return a list w/ json objects
# def read_all_json_files(file_path):
#     list_of_jsons = []
#     for root, directory, files in os.walk(file_path):
#         for item in files:
#             fullPath = os.path.join(file_path, item)
#             if os.path.isdir(fullPath):
#                 if '.json' in item:
#                     list_of_jsons.append(str(fullPath))
#     return list_of_jsons


def read_all_json(dirName):
    # create a list of file and sub directories
    # names in the given directory
    list_of_files = os.listdir(dirName)
    json_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            json_files = json_files + read_all_json(fullPath)
        elif '.json' in entry:
            json_files.append(read_json(fullPath))

    return json_files


file_path = '/Users/nick/Python/Labs/PythonFundamentals.Exercises.Part9/data'
# print(read_all_json_files(file_path))
data = read_all_json(file_path)
pickle_path = "/Users/nick/Python/Labs/PythonFundamentals.Exercises.Part9/data/super_smash_bros"
write_pickle(pickle_path, data)