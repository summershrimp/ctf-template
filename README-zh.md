# ctf-template
用于办赛前协作收集CTF比赛题目

[English](README.md)

## 用法

### 项目结构
```
ctf-template/
├── challenges                  // 用于储存所有的赛题文件
│   ├── challenge-short-name1   // 赛题文件夹，并以赛题短名字命名 (只能包含 /[a-zA-Z0-9_-]/.)
│   │   ├── challenge.yaml      // 赛题配置文件
│   │   ├── dist                // 存放提供给选手的文件
│   │   │   └── file
│   │   ├── Dockerfile          // 用于构建赛题服务端的 Dockerfile 
│   │   ├── src                 // 源代码和不需要提供给选手的文件.
│   │   │   ├── flag
│   │   │   ├── pwn.c
│   │   │   └── pwn.xinetd
│   │   └── writeup             // 当前赛题的 Writeup
│   │       ├── images
│   │       └── README.md
│   ├── challenge-short-name2   // 另一个赛题文件夹
.....
├── examples                    // 样例文件夹，包括几个方便理解项目结构的示例赛题
├── LICENSE
├── contest.yaml                // (未完成) 比赛配置文件
├── build.sh                    // (未完成) 打包和分发脚本
└── README.md                   // 当前文件
```

### challenge.yaml
```
# Challenge configuration
name: simple pwn                # 赛题名称
type: pwn                       # 赛题类型 (web,pwn,misc,rev,mobile,crypto etc.)
description: >
        这是一个yaml折行文本，
        在这一项中写赛题说明
flag: flag{s1mple_pwn_fl@g}     # 正确的flag
hints:                          # 赛题提示
    - The first hint.
    - The second hint.
image: true                     # 赛题是否包含服务端Docker镜像

```
