from pytube import YouTube


link = input('Enter link: ')
while link != 'Exit':
    yt = YouTube(link)

    print("Downloading: ", yt.title)

    yd = yt.streams.get_highest_resolution()

    # ADD FOLDER HERE
    yd.download('/Users/rohailramesh/Desktop')  
    link = input('Enter link: ')