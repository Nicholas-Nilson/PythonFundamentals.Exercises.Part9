import json, os, pickle, sys


def read_json(file_path):
    file = open(file_path)
    data = json.loads(file.read())
    return data

def is_json(file_name):
    return '.json' in file_name

def is_pickle(file_name):
    return '.pickle' in file_name

def is_directory(file_path):
    return os.path.isdir(file_path)

def get_pickle_title(file_path):
    dir_list = file_path.split("/")
    if file_path[-1] == "/":
        return dir_list[-2]
    else:
        return dir_list[-1]



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
    json_files = []
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


def write_pickle(file_path, file_name, data_to_pickle):
    with open(file_path + '/' + str(file_name), 'wb') as f:
        pickle.dump(data_to_pickle, f)


def load_pickle(file_path):
    pickle_data = []
    with open(file_path, 'rb') as f:
        while True:
            try:
                pickle_data.append(pickle.load(f))
            except EOFError:
                break
    return pickle_data


data_to_write = {"name:": "Goku", "race": "Saiyan", "Family": "ChiChi and Gohan", "hype move": "spirit bomb"}
path_to_write = '/Users/nick/Python/Labs/PythonFundamentals.Exercises.Part9/data/dragon_ball_z/'

print(get_pickle_title(path_to_write))


with open(path_to_write + 'Goku.json', 'w') as file_to_write:
    json.dump(data_to_write, file_to_write)

file_path = '/Users/nick/Python/Labs/PythonFundamentals.Exercises.Part9/data'
# print(read_all_json_files(file_path))
# data = read_all_json(file_path)
# pickle_path = "/Users/nick/Python/Labs/PythonFundamentals.Exercises.Part9/data/super_smash_bros"
# write_pickle(pickle_path, data)
# pickle_name = "/Users/nick/Python/Labs/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle"
# print(load_pickle(pickle_name))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please include path/filename or path")
        exit()
    if len(sys.argv) == 2:
        if is_json(sys.argv[1]):
            print(read_json(sys.argv[1]))
        elif is_pickle(sys.argv[1]):
            print(load_pickle(sys.argv[1]))
        elif is_directory(sys.argv[1]):
            data = read_all_json(sys.argv[1])
            file_name = get_pickle_title(sys.argv[1])
            write_pickle(sys.argv[1], file_name, data)
            print("pickling complete!")
        else:
            print("please select file with valid extension")
