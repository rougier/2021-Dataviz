from requests import get  # to make GET request


def download(url, filename):
    with open(filename, "wb") as file:
        response = get(url)
        file.write(response.content)
        

basename = "http://telechargement.insee.fr/fichiersdetail/etatcivil2012/dbase/"
filenames = ["etatcivil2016_nais2016_dbase.zip",
             "etatcivil2016_dec2016_dbase.zip",
             "etatcivil2016_mar2016_dbase.zip" ]

for filename in filenames:
    download(basename+filename, filename)

# from urllib.error import URLError
# import pyensae
# from pyensae.datasource import dBase2df, DownloadDataException

# try:
#     pyensae.download_data(files[-1],
#                           website='
# except (DownloadDataException, URLError, TimeoutError):
#     # backup plan
#     pyensae.download_data(files[-1], website="xd")

# df = dBase2df("mar2012.dbf")
# print(df.shape, df.columns)
# df.head()

