/* 
 * gcc -fno-stack-protector pwn.c -o .../dist/pwn -O0 -fPIE -pie
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int init(void) {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(60);
    return 0;
}

int getshell() {
    system("/bin/sh");
}

int exchange(char *a, int x, int y) {
    int i, j;
    char t;
    for(i = 0; i < x; ++i) {
        for (j = 0; j < y; ++j) {
            t = a[x * i + j];
            a[x * i + j] = a[i + j * y];
            a[i + j * y] = t;
        }
    }
}

int main(void) {
    int x, y;
    int i, j;
    char map[0x400];
    int (*handler)(char *a, int x, int y);
    char t;
    handler = exchange;
    init();
    printf("input map size:");
    scanf("%d %d", &x, &y);
    if(x > 0x400 || y > 0x400 || x*y > 0x400) {
        printf("size too large.");
        exit(0);
    }
    while ((t = getchar()) == '\n') ;
    i = 0, j = 0;
    while (i<=x) {
        while(j<=y){
            map[i*x + j] = t;
            t = getchar();
            ++j;
        }
        ++i;
    }

    handler(map, x, y);
    
    exit(0);
    return 0;
}