## Playman

### Running it

1. Install [VLC media player](https://www.videolan.org/vlc/)
2. Run in terminal:

```
git clone https://github.com/webavant/playman && cd playman
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 playman.py
```

### What is it?

Listening to live radio, music, and podcasts involves too much software, too many fees. Playman is an all-in-one streaming audio hub that runs directly in your terminal. You can find and listen to podcasts, music, and live radio stations with a few keystrokes.

### Why terminal?

However niche the use-case seems in the generation of touch screen and mobile apps, I'm still spending enough time in my terminal that I'd usually rather stay focused and not fiddle with my phone or my web browser.

### Planning

Years of obsessive terminal abuse, a few days of full bore coding, rethinking, total rewrites, and plenty more to come! 

Some library choices were made for the sake of simplicity, heavily relying on several more tried-and-true standards, like `youtube-dl`, `pafy`, and `vlc`.

### Issues

The basic feature set and UI are the result of a quick and dirty three days of work. 

1. I scrapped a ton of code that tried to implement a custom UI
2. I found a basic UI library to cobble togeether the minimum viable product

### Vision

I considerably reduced the original and intended level of complexity for immediate release and presentation. My envisioning of this projects often began with too lofty goals, which included the following...

### Features On Hold

1. bookmarks - save results from previous searches
2. import playlists from M3U and OPML standard formats
3. slider interface for seeking audio/stream track

### Kudos

I love working in the terminal.

### Complaints

I dread researching and sifting through out-of-date and buggy libraries.
