import youtube_dl


def get_input_url(url: str) -> str:
    ydl_opts = {}
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info_dict = ydl.extract_info(url, download=False)
    formats = info_dict.get('formats', None)

    input_url = formats[-1]['url']

    return input_url
