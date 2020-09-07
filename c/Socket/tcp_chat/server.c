#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <string.h>

#define PORT 9001

int main() {
    int network_socket, client_socket;
    network_socket = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in server_address, client_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = INADDR_ANY;

    if (bind(network_socket, (struct sockaddr*) &server_address, sizeof(server_address)) < 0) {
        printf("Error binding\n");
        return -3;
    }

    if (listen(network_socket, 1) < 0) {
        printf("Error listening\n");
    }
    socklen_t clilen = sizeof(client_address);
    client_socket = accept(network_socket, (struct sockaddr*) &client_address, &clilen);
    if (client_socket < 0) {
        printf("Error accepting\n");
    }
    printf("Client connected\n");
    
    char buffer[256];
    while (1) {
        bzero(buffer, 256);
        printf("Server: ");
        fgets(buffer, 256, stdin);
        if (write(client_socket, buffer, strlen(buffer)) < 0) {
            printf("Error writing to client\n");
            return -1;
        }
        bzero(buffer, 256);
        if (read(client_socket, buffer, 256) < 0) {
            printf("Error reading from client\n");
            return -2;
        }
        printf("Client: %s", buffer);
        if (strncmp(buffer, "bye", 3) == 0) {
            break;
        }
    }

    close(network_socket);
    
    return 0;
    
}

