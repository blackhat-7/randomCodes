#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
#include <string>


using namespace std;

int main() {

	// Create a socket
	int listening = socket(AF_INET, SOCK_STREAM, 0);
	if (listening < 0) {
		cerr << "Cannot create socket";
		return -1;
	}
	// Bind the socket to IP/Port
	sockaddr_in hint;
	hint.sin_family = AF_INET;
	hint.sin_port = htons(9002);
	inet_pton(AF_INET, "0.0.0.0", &hint.sin_addr);
	if (bind(AF_INET, (sockaddr*) &hint, sizeof(hint)) == -1) {
		cerr << "Can't bind to IP/Port";
		return -2;
	}

	// MArk the socket for listening
	if (listen(listening, SOMAXCONN) == -1) {
		cerr << "Server can't listen";
		return -3;
	}

	//Accept a call
	sockaddr_in client;
	socklen_t clientSize;

	// Buffer to put host and server name
	char host[NI_MAXHOST];
	char svc[NI_MAXSERV];
	
	int clientSocket = accept(listening, (sockaddr*) &client, &clientSize);

	if (clientSocket == -1) {
		cerr << "Problem with client connecting";
		return -4;
	}
	
	close(listening);

	memset(host, 0, NO_MAXHOST);
	memset(svc, 0, NI_MAXSERV);

	return 0;
}
