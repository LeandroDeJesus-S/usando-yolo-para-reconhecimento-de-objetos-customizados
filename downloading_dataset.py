from bing_image_downloader import downlod  # pip install bing-image-downloader

# apos baixado entre na pasta e ajuste as imagens como necessario pois
# sera criada um outra pasta com o nome do filtro
downloader.download(
    query_string, 
    limit=100, 
    output_dir='build/darknet/x64/data/myprog/', 
    adult_filter_off=True, 
    force_replace=False, 
    timeout=60, 
    verbose=True
)
