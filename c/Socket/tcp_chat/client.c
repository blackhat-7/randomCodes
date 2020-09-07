#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <string.h>

#define PORT 9001

int main() {
    int network_socket;
    network_socket = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = INADDR_ANY;

    int connection_status = connect(network_socket, (struct sockaddr*) &server_address, sizeof(server_address));

    if (connection_status == -1) {
        printf("Error in connecting to server\n");
    }
    
    char buffer[256];
    while (1) {
        bzero(buffer, 256);
        if (read(network_socket, buffer, 256) < 0) {
            printf("Fail\n");
            return -1;
        }
        printf("Server: %s", buffer);
        bzero(buffer, 256);
        printf("Client: ");
        fgets(buffer, 256, stdin);
        if (write(network_socket, buffer, strlen(buffer)) < 0) {
            printf("Fail\n");
            return -2;
        }
        if (strncmp(buffer, "bye", 3) == 0) {
            break;
        }
    }

    close(network_socket);

    return 0;

}
