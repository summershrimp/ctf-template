# ctf-template
A template repo for CTF organizer collect and distribute Challenges

[中文版](README-zh.md)

## Usage

### Project structure
```
ctf-template/
├── challenges                  // challenges your contest have.
│   ├── challenge-short-name1   // challenge short name as folder (should only contains /[a-zA-Z0-9_-]/.)
│   │   ├── challenge.yaml      // challenge configuration file.
│   │   ├── dist                // Distribution files players can directly download.
│   │   │   └── file
│   │   ├── Dockerfile          // Dockerfile that build images for server end.
│   │   ├── src                 // Source code and files not distributed to players.
│   │   │   ├── flag
│   │   │   ├── pwn.c
│   │   │   └── pwn.xinetd
│   │   └── writeup             // Writeup for current challenge
│   │       ├── images
│   │       └── README.md
│   ├── challenge-short-name2   // Another challenge.
.....
├── examples                    // Contains some example challenge to help understand.
├── LICENSE
├── contest.yaml                // (not finished) Contest configuration file.
├── build.sh                    // (not finished) Script to generate contest configuration.
└── README.md                   // This file.
```

### challenge.yaml
```
# Challenge configuration
name: simple pwn                # Challenge name
type: pwn                       # Challenge type (web,pwn,misc,rev,mobile,crypto etc.)
description: >
        This is a single line description
        and will fold to one line.
flag: flag{s1mple_pwn_fl@g}     # Correct flag
hints:                          # Hints for current challenge
    - The first hint.
    - The second hint.
image: true                     # Shoule build docker image for this challenge

```
