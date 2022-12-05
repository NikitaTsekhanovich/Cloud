def split_file(file_name):
    size_block = 1024 * 1024
    semi_file_size = 1024 * 1024 * 512
    current_volume = 1
    bytes_written = 0
    with open(f'{file_name}', 'rb') as file:
        while True:
            output_file_name = '{}.{}'.format(f'{file_name}', str(current_volume).zfill(3))
            output = open(output_file_name, 'wb')
            while bytes_written < semi_file_size:
                data = file.read(size_block)
                if data == b'':
                    break
                output.write(data)
                bytes_written += len(data)
            else:
                output.close()
                current_volume += 1
                bytes_written = 0
                continue
            output.close()
            return current_volume
