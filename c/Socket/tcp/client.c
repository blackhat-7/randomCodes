#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/socket.h>

#include <netinet/in.h>

#include <unistd.h>

int main() {
	// Create socket
	int network_socket;
	network_socket = socket(AF_INET, SOCK_STREAM, 0);

	// Specify an address for the socket
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(9002);
	server_address.sin_addr.s_addr = INADDR_ANY;

	int connections_status = connect(network_socket, (struct sockaddr_in*) &server_address, sizeof(server_address));
	
	// Check for error with the connection
	if (connections_status == -1) {
		printf("There was n error making a connection to the remote socket \n\n");
	}
	
	// Receive data from the server
	char server_response[256];
	recv(network_socket, &server_response, sizeof(server_response), 0);

	// Print out the server's response
	printf("Server says: %s\n", server_response);
	
	// Close the socket
	close(network_socket);
	return 0;
}

	 
