def get_file_extension(filename, has_dot=False):
    """
    Get file's extension

    param:
    filename: 檔名
    has_dot: bool, 返回的字尾名是否需要帶點
    return: file's extension
    """
    pos = filename.rfind('.')

    if 0 < pos and pos < (len(filename) - 1):
        if has_dot:
            index = pos 
        else:
            index = pos + 1
        return filename[index:]
    else:
        return ''
    
    if __name__ == '__main__':
        get_file_extension()