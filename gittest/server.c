#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<errno.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
 
#define MAXLINE 4096
 
int main(int argc, char** argv)
{
    int    listen1, conn;
    struct sockAddr_in     servAddr;
    char    buff[4096];
    int     n;
 
    if( (listen1 = socket(AF_INET, SOCK_STREAM, 0)) == -1 ){
    printf("create socket error: %s(errno: %d)\n",strerror(errno),errno);
    exit(0);
    }
 
    memset(&servAddr, 0, sizeof(servAddr));
    servAddr.sin_family = AF_INET;
    servAddr.sin_Addr.s_Addr = htonl(INADDR_ANY);
    servAddr.sin_port = htons(6666);
 
    if( bind(listen1, (struct sockaddr*)&servAddr, sizeof(servAddr)) == -1){
    printf("bind socket error: %s(errno: %d)\n",strerror(errno),errno);
    exit(0);
    }
 
    if( listen(listen1, 10) == -1){
    printf("listen socket error: %s(errno: %d)\n",strerror(errno),errno);
    exit(0);
    }
    printf("waiting for client's request......\n");
    while(1){
    if( (conn = accept(listen1, (struct sockAddr*)NULL, NULL)) == -1){
        printf("accept socket error: %s(errno: %d)",strerror(errno),errno);
        continue;
    }
    n = recv(conn, buff, MAXLINE, 0);
    buff[n] = '\0';
    printf("receive message from client: %s\n", buff);
    close(conn);
    }
 
    close(listen1);
}
