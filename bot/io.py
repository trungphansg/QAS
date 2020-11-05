def load_dictionary(data_file_path, delimiter='\t', skip_header=False):
    """
    Load data from a file into a dictionary
    :param data_file_path: path of the file
    :param delimiter: field delimiter
    :return: the dictionary
    """
    file = open(data_file_path, mode='rt', encoding='utf8')
    if skip_header: next(file)
    result = {}
    for line in file:
        label, sentence = line.strip().split(delimiter)
        result[label] = sentence
    file.close()
    return result


def load_text_label_pairs(data_file_path, delimiter='\t', skip_header=False):
    """
    Load data from a file into an array
    :param data_file_path: path of the file
    :param delimiter: field delimiter
    :return: the array
    """
    file = open(data_file_path, mode='rt', encoding='utf8')
    if skip_header: next(file)
    result = []
    for line in file:
        label, sentence = line.strip().split(delimiter)
        result.append((sentence, label))
    file.close()
    return result


def load_array(data_file_path, skip_header=False):
    """
    Load data line by line from a file into an array
    :param data_file_path: path of the file
    :return: the array
    """
    file = open(data_file_path, mode='rt', encoding='utf8')
    if skip_header: next(file)
    result = []
    for line in file:
        result.append(line.replace("\n",""))
    file.close()
    return result


def load_array_from_column(data_file_path, delimiter='\t',column_index=0, skip_header=False):
    """
    Load data line by line from a file into an array
    :param data_file_path: path of the file
    :param delimiter: field delimiter
    :param column_index: index of column to laod data
    :param skip_header: whether to skip header row or not
    :return: the array
    """
    file = open(data_file_path, mode='rt', encoding='utf8')
    if skip_header: next(file)
    result = []
    for line in file:
        result.append(line.replace("\n","").split(delimiter)[column_index])
    file.close()
    return result


def load_array_from_columns(data_file_path, delimiter='\t', from_column_index=0, to_column_index=0, skip_header=False):
    """
    Load data line by line from a file into an array
    :param data_file_path: path of the file
    :param delimiter: field delimiter
    :param from_column_index:
    :param to_column_index:
    :param skip_header: whether to skip header row or not
    :return: the array
    """
    file = open(data_file_path, mode='rt', encoding='utf8')
    if skip_header: next(file)
    result = []
    for line in file:
        parts = line.replace("\n", "").split(delimiter)[from_column_index:to_column_index + 1]
        result.append(" ".join(parts))
    file.close()
    return result