#include <iostream>

int main() {
    char word[] = "hello";
    
    int len = sizeof(word) - 1;
    char* pStart = word;
    char* pEnd = word + len - 1;

    while(pStart < pEnd) {
        char save = *pStart;
        *pStart = *pEnd;
        *pEnd = save;

        pStart++;
        pEnd--;
    }

    std::cout << word << std::endl;
}
/*

hello *s=h, *e=o 04
oellh *s=e, *e=l 13
olleh *s=l, *e=l 22
*/