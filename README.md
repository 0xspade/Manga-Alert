# Manga-Alert

Since I love Manga, I created an alert for Manga updates once they have a latest manga release for One Punch Man and One Piece. I'm currently reading Mangas in w10.mangafreak.net :)

## Requirements

`pip3 install datetime cfscrape requests`

## Installation
`git clone https://github.com/phspade/Manga-Alert.git`

## Usage
Schedule the script to your crontab. mine is every 8hrs.

`0 */8 * * * python3 /home/<your username>/Manga-Alert/manga.py`

and It will send you an alert via Telegram every 8hrs. 

Make sure to put your own bot key and telegram id in manga.py script :)

### Credits to MangaFreak.net :)
