def get_folder_size_in_gb(directory):
    """
    Inspects a folder recursively and returns it size in gigabytes.
    """
    import os
    from os.path import join, getsize
    from os import walk
    total_size = 0
    for dirpath, dirnames, filenames in walk(directory):
        for filename in filenames:
            file_path = join(dirpath, filename)
            total_size += getsize(file_path)
    return total_size / (1024 ** 3)

def calculate_model_memory_in_gb(model):
    """
    Inspects a pytorch model and returns its size in memory in gigabytes.
    """
    total_size_in_bytes = sum(p.numel() * p.element_size() for p in model.parameters())
    size_in_mb = total_size_in_bytes / (1024 ** 3)
    return size_in_mb