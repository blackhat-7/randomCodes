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
char fname[256];
int network_socket, client_socket;
struct sockaddr_in server_address, client_address;


int send_file() 
{
    read(client_socket, fname, 256);
    FILE *f = fopen(fname, "rb");

    if (f == NULL) 
    {
        perror("Could not open file\n");
        return 0;
    }

    while (1) 
    {
        bzero(buffer, 1024);
        int nread = fread(buffer, 1, 1024, f);
        if (nread > 0)
        {
            write(client_socket, buffer, nread);
        }
        if (nread < 1024) 
        {
            if (feof(f)) 
            {
                printf("End of file reached\n");
                sleep(1);
            }
            if (ferror(f)) 
            {
                perror("Error reading file\n");
                return 0;
            }
            break;
        }
    }

    return 1;
}


int main(int argc, char* argv[]) 
{

    // Establishing the connection

    if ((network_socket = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
    {
        perror("Failed to obtain socket descriptor\n");
    }

    socklen_t clilen = sizeof(client_address);
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = INADDR_ANY;

    if (bind(network_socket, (struct sockaddr*) &server_address, sizeof(server_address)) < 0) 
    {
        perror("Error binding\n");
        return -3;
    }

    if (listen(network_socket, 1) < 0) 
    {
        perror("Error listening\n");
    }
    client_socket = accept(network_socket, (struct sockaddr*) &client_address, &clilen);
    if (client_socket < 0) 
    {
        perror("Error accepting\n");
    }
    printf("Client connected\n");

    // Send the file

    if (send_file() == 0) 
    {
        perror("Failed to send file\n");
    }
    else 
    
    {
        printf("File has been sent successfully!\n");  
    }

    // Close connections

    close(client_socket);
    close(network_socket);
    printf("Connections closed\n");
    return 0;

}

