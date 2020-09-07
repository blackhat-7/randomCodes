#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <string.h>
#include <ctype.h>

#define PORT 9005


// Global variables
unsigned char buffer[1024];
int bytes_received = 0;
char fname[256];
int network_socket;
struct sockaddr_in server_address;

int receive_data() {

    printf("Filename: %s", fname);
    FILE *f = fopen(fname, "ab");

    if (f == NULL) {
        perror("Error opening file\n");
        return 0;
    }

    bzero(buffer, 1024);
    long double num_bytes_received = 0;
    
    while ((bytes_received = read(network_socket, buffer, 1024)) > 0) {
        num_bytes_received++;
        printf("Received : %llf MB\n", (num_bytes_received/1024));
        fwrite(buffer, 1, bytes_received, f);
        if (bytes_received < 1024) {
            printf("EOF reached");
            break;
        }
        bzero(buffer, 1024);
    }
    
    if (bytes_received < 0) {
        perror("Error reading file\n");
        return 0;
    }
    printf("File has been received!\n");

    return 1;
}


int main(int argc, char* argv[]) {
    if ((network_socket = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Failed to obtain socket descriptor\n");
    }

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = INADDR_ANY;

    int connection_status = connect(network_socket, (struct sockaddr*) &server_address, sizeof(server_address));

    if (connection_status == -1) {
        perror("Error in connecting to server\n");
    }
    
    strcpy(fname, argv[1]);
    write(network_socket, fname, 256);

    if (receive_data() == 0) {
        perror("Error receiving file\n");
    }
    else {
        printf("File has been received successfully!\n");
    }

    close(network_socket);
    return 0;

}
