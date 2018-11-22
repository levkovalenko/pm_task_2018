import asyncio

from news import News


@asyncio.coroutine
def read(file_name, code='utf-8'):
    """
    async generator to read file in with special delimeter
    :param file_name: the way to the file
    :param code: encoding of file (utf-8)
    :return: generator with all parts of file
    """
    with open(file_name, 'r', encoding=code) as file:
        for line in file:
            yield News(line)
        yield ""

