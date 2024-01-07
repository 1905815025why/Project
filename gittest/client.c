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
    int    sock, n;
    char    recvline[4096], sendline[4096];
    struct sockAddr_in    servAddr;
 
    if( argc != 2){
    printf("usage: ./client <ipaddress>\n");
    exit(0);
    }
 
    if( (sock = socket(AF_INET, SOCK_STREAM, 0)) < 0){
    printf("create socket error: %s(errno: %d)\n", strerror(errno),errno);
    exit(0);
    }
 
    memset(&servAddr, 0, sizeof(servAddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(6666);                     
    if( inet_pton(AF_INET, argv[1], &servAddr.sin_Addr) <= 0){
    printf("inet_pton error for %s\n",argv[1]);
    exit(0);
    }
 
    if( connect(sock, (struct sockAddr*)&servAddr, sizeof(servAddr)) < 0){
    printf("connect error: %s(errno: %d)\n",strerror(errno),errno);
    exit(0);
    }
    printf("send message to server: \n");
    message= fgets(sendline, 4096, stdin);
    if(strcmp(message,"bye")==0)
	break;
    if( send(sock, sendline, strlen(sendline), 0) < 0)
    {
    printf("send message error: %s(errno: %d)\n", strerror(errno), errno);
    exit(0);
    }
 
    close(sock);
    exit(0);
