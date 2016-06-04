#!/usr/bin/env python3

import shutil

class Pg:
    def __init__(self, name, title, submenu=None):
        self.name = name
        self.title = title
        self.submenu = submenu

br = '<br/>\n'
def li(text): return '<li>' + text + '</li>\n'

if __name__ == "__main__":
    shutil.rmtree("out", True)
    shutil.copytree("in", "out")
    with open("out/emai1.txt", "w") as fout:
        with open("emai1.txt", "r") as fin:
            fout.write(",".join(reversed([str((ord(c) - i * 42 - 1) % 256) for i, c in enumerate(fin.read())])))
    for pg in [
        Pg("index", "Andrew Downing's website"),
        Pg("flash", "Flash games by DowningGames"),
        Pg("pd", "Plausible Deniability"),
        Pg("afdarts", "Afdarts", submenu="afdarts"),
        Pg("afdartsdownload", "Afdarts downloads", submenu="afdarts"),
        Pg("afdartsdevelopment", "Afdarts development", submenu="afdarts"),
        Pg("afdartstheory", "Afdarts code theory", submenu="afdarts"),
        Pg("afdartsdevelopmentarchive", "Afdarts development archive", submenu="afdarts"),
        Pg("afdartsmusic", "Afdarts music", submenu="afdarts"),
        Pg("orts", "ORTS AI competition"),
        Pg("shootcity", "ShootCity", submenu="shootcity"),
        Pg("games", "other games"),
        Pg("interaction", "USC Interaction Lab", submenu="interaction"),
        Pg("interaction20133", "USC Interaction Lab, fall 2013", submenu="interaction"),
        Pg("interaction20122", "USC Interaction Lab, summer 2012", submenu="interaction"),
        Pg("pr", "PR Lite"),
        Pg("robomagellan", "Myrmecophaga tridactyla", submenu="robomagellan"),
        Pg("hackathon", "hackathon projects"),
        Pg("videorobots", "robot videos"),
        Pg("videogames", "computer game videos"),
        Pg("videomagic", "magic show videos"),
        Pg("video", "other videos"),
        Pg("physics", "favorite physics explanations"),
        Pg("skilift", "how accelerating ski lifts work"),
        Pg("resume", "Andrew Downing's resume"),
        Pg("links", "external links"),
        Pg("emai1", "Thanks!"),
    ]:
        def link(href, text): return '<a href="{}.htm"{}>{}</a>'.format(href, ' class="sel"' if href == pg.name else '', text)
        def submenu(name, text): return '<ul class="submenu">\n' + text + '</ul>\n' if name == pg.submenu else ''
        with open("out/" + pg.name + ".htm", "w") as fout:
            with open("in/" + pg.name + ".htm", "r") as fin:
                fout.write(
"""<!doctype html>
<html>
  <head>
    <title>""" + pg.title + """</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <link rel="stylesheet" type="text/css" href="style.css"/>
    <script type="text/javascript" src="script.js"></script>
  </head>
  <body onload="load()">
<div style="position: absolute; width: 150px; background-color: #e8e8e8">
""" + link("index", "home") + br +
br + "games:" + br +
link("flash", "Flash games") + br +
link("pd", "Plausible Deniability") + br +
link("afdarts", "Afdarts") + br +
submenu("afdarts",
    li(link("afdartsdownload", "download")) +
    li(link("afdartsdevelopment", "development")) +
    li(link("afdartstheory", "code theory")) +
    li(link("afdartsmusic", "custom music")) +
    li('project page at <a href="https://sourceforge.net/projects/downinga-rts"><img src="https://sourceforge.net/sflogo.php?group_id=205750&amp;type=10" alt="SourceForge"/></a>')) +
link("orts", "AI competition") + br +
link("shootcity", "ShootCity") + br +
submenu("shootcity",
    li('project page at <a href="https://sourceforge.net/projects/shootcity"><img src="https://sourceforge.net/sflogo.php?group_id=205748&amp;type=10" alt="SourceForge"/></a>')) +
link("games", "other games") + br +
br + "robotics:" + br +
link("interaction", "Interaction Lab") + br +
submenu("interaction",
    li(link("interaction20133", "fall 2013")) +
    li(link("interaction20122", "summer 2012"))) +
link("pr", "PR Lite") + br +
link("robomagellan", "RoboMagellan") + br +
submenu("robomagellan",
    li('project page at <a href="https://sourceforge.net/projects/anteaterbot"><img src="https://sourceforge.net/sflogo.php?group_id=331502&amp;type=10" alt="SourceForge"/></a>')) +
br + "other projects:" + br +
link("hackathon", "hackathons") + br +
br + "videos:" + br +
link("videorobots", "robots") + br +
link("videogames", "games") + br +
link("videomagic", "magic") + br +
link("video", "other videos") + br +
br + "commentary:" + br +
link("physics", "physics") + br +
link("skilift", "ski lifts") + br +
br + "other:" + br +
link("resume", "resume") + br +
link("links", "links") + br +
link("emai1", "&#x65;&#109;&#97;&#105;&#x6c; me") +
"""
</div>
<div style="border-width: 0 0 0 150px; border-style: solid; border-color: #e8e8e8; padding-left: 5px">
""" + fin.read() + """</div>
  </body>
</html>
""")
