def split_file(file_name):
    size_block = 1024 * 1024  # размер блока которыми читаем из файла
    file_size = 1024 * 1024 * 512  # проебразуем в байты
    current_volume = 1  # текущий номер тома
    bytes_written = 0  # сколько байт записали
    with open(f'{file_name}', 'rb') as src:
        while True:
            output_file_name = '{}.{}'.format(f'{file_name}', str(current_volume).zfill(3))
            output = open(output_file_name, 'wb')
            while bytes_written < file_size:
                data = src.read(size_block)
                if data == b'':
                    break
                output.write(data)
                bytes_written += len(data)
                print('write', len(data), 'bytes to', output_file_name)
            else:
                output.close()
                current_volume += 1
                bytes_written = 0
                continue
            output.close()
            break
