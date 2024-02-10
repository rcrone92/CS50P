import re

s = "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/xvFZjo5PgG0\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"

out = re.search(r"src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]*)\"", s)

print(out)
print(f"https://youtu.be/{out.group(2)}")
