from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

def unzipfile(path_to_zip_file:str, directory_to_extract_to:str):
    """
        Unzip files
    """
    resp = urlopen(path_to_zip_file)
    # zipfile = ZipFile(BytesIO(resp.read()))
    with ZipFile(BytesIO(resp.read())) as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    
    # zipfile = ZipFile(BytesIO(resp.read()))
    # for line in zipfile.open(file).readlines():
    #     print(line.decode('utf-8'))

    # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    #     zip_ref.extractall(directory_to_extract_to)

unzipfile("https://github.com/ScudraServicos/data-engineer-code-challenge/raw/main/payments.zip",
            "./dags/data/")