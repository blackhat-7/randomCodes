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
	if (listening < 0 {
		cerr << "Cannot create socket";
		return -1;
	}

	// Bind the socket to IP/Port
	sockaddr_in hint;
	cout << hint << endl;
	hint.sin_family = AF_INET;
	hint.sin_port = htons(9002);
	inet_pton(AF_INET, "0.0.0.0", hint);
	return 0;
}
