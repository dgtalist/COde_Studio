'''chapter11_CA_crawling_google.py v1.0'''

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {
    'keywords':'방탄소년단',
    'limit':20,
    'print_urls':True,
    'format':'jpg'
    }

paths = response.download(arguments)

print(paths)
