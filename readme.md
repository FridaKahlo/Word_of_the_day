# Overview

The *Word of the day* project facilitates learning new words, by bla bla bla.


# Requirements

* Windows 10
* Python 3.5+ x64
* Pillow 4.0 Pillow-4.0.0-cp35-cp35m-win_amd64.whl
* requests==2.11.1

# Installation instructions

1. Install dependencies with `C:\Users\[username]\AppData\Local\Programs\Python\Python35\Scripts\pip3.5.exe install Pillow`




# Various stuff

1. install git for Windows
2. create account on GitHub (lucru individual)
3. write a basic `readme` guide using Markdown
4. install required Python libraries



# References

* Online Markdown editor: https://stackedit.io/editor
* Markdown syntax cheatsheet: https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
* Image of the day API: http://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day
* Diagram editor https://www.planttext.com/

## Quick git reference

Command      |   Description
----------------|-------------------------------------------------------------------------------------------
git init          | The git init command creates a new Git repository
git add         | The git add command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit. However, git add doesn't really affect the repository in any significant way—changes are not actually recorded until you run git commit.
Git status     |The command checks the status and reports that there’s nothing to commit.
Git commit <file> –m <message> | to save your work into Git version control
Git config     | lets you get and set configuration variables that control all aspects of how Git looks and operates
Git diff  | displays the differences between two versions in detail
Git log | lists the commits made in that repository in reverse chronological order – that is, the most recent commits show up first.


# Tasks

* Read about the `JSON` format and the Python `json` module



# Features

1. Retrieve Bing image of the day
2. Retrieve a word from a file one after another
3. Search the transalation of the word
4. Overlay the word and its translation on the image
5. Set the image as the desktop background



# Notes

* Bing image of the day URL `http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US`
* Example of response:
	```
	{
  "images": [
    {
      "startdate": "20170218",
      "fullstartdate": "201702180800",
      "enddate": "20170219",
      "url": "\/az\/hprichbg\/rb\/Vieste_EN-US8673772243_1920x1080.jpg",
      "urlbase": "\/az\/hprichbg\/rb\/Vieste_EN-US8673772243",
      "copyright": "Vieste on the Adriatic coast of Italy (\u00a9 Peter Adams Photography Ltd\/Alamy)",
      "copyrightlink": "http:\/\/www.bing.com\/search?q=Vieste&form=hpcapt&filters=HpDate:%2220170218_0800%22",
      "quiz": "\/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20170218_Vieste%22&FORM=HPQUIZ",
      "wp": true,
      "hsh": "0816755ca309baf41aaddc1f80cf9919",
      "drk": 1,
      "top": 1,
      "bot": 1,
      "hs": [
        
      ]
    }
  ],
  "tooltips": {
    "loading": "Loading...",
    "previous": "Previous image",
    "next": "Next image",
    "walle": "This image is not available to download as wallpaper.",
    "walls": "Download this image. Use of this image is restricted to wallpaper only."
  }
}
```


# Sequence diagram

```
            ┌───────┐                      ┌──────┐     
            │program│                      │server│     
            └───┬───┘                      └──┬───┘     
                │                             │         
                ╔══════════════════════╗      │         
════════════════╣ Obtain image address ╠══════╪═════════
                ╚══════════════════════╝      │         
                │                             │         
                │  GET /image-of-the-day-URL  │         
                │─────────────────────────────>         
                │                             │         
                │        JSON response        │         
                │<─────────────────────────────         
                │                             │         
                ────┐                         │         
                    │ extract url             │         
                <───┘                         │         
                │                             │         
     ╔══════════╧═══════════╗                 │         
     ║it is in images[url] ░║                 │         
     ╚══════════╤═══════════╝                 │         
                │                             │         
             ╔══╧════════════════════════╗    │         
═════════════╣ Download the image itself ╠════╪═════════
             ╚══╤════════════════════════╝    │         
                │                             │         
      ╔═════════╧═════════╗                   │         
      ║use URL from JSON ░║                   │         
      ╚═════════╤═════════╝                   │         
                │     GET bing.com/[url]      │         
                │─────────────────────────────>         
                │                             │         
                │            image            │         
                │<─────────────────────────────         
                │                             │         
                ────┐                         │         
                    │ save image to file      │         
                <───┘                         │         
                │                             │         
                │                             │         
             ╔══╧═════════════════════════╗   │         
═════════════╣ Retrieve the word from file╠═══╪═════════
             ╚══╤═════════════════════════╝   │         
                │                             │         
                ────┐                                   
                    │ open the file "Words.txt"         
                <───┘                                   
                │                             │         
                ────┐                         │         
                    │ select a random word    │         
                <───┘                         │         
                │                             │         
  ╔═════════════╧═══════════════╗             │         
  ║import translation function ░║             │         
  ║from the previous project    ║             │         
  ╚═════════════╤═══════════════╝             │         
                │  request word translation   │         
                │─────────────────────────────>         
                │                             │         
                │         translation         │         
                │<─────────────────────────────         
            ┌───┴───┐                      ┌──┴───┐     
            │program│                      │server│     
            └───────┘                      └──────┘     
```


## Diagram source code
```
@startuml

title "Word of the day"

== Obtain image address ==
program->server: GET /image-of-the-day-URL
server->program: JSON response
program->program: extract url
note over program: it is in images[url]

== Download the image itself ==
note over program: use URL from JSON
program->server: GET bing.com/[url]
server->program: image
program->program: save image to file

==Retrieve the word from file==
program->program: open the file "Words.txt"
program->program: select a random word
note over program: import translation function\nfrom the previous project
program->server: request word translation
server->program: translation



@enduml
```
