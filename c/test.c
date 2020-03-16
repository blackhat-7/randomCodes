#include <stdio.h>

#define PI 3.1415


void search(char *line, char *parameter, int *found) {
    int x = 0;
    for (int i=0; line[i]!='\0'; ++i) {
        printf("%c,%c\n", line[i], parameter[x]);
        if (line[i]==parameter[x]) {
            x++;
            if (parameter[x]=='\0') {
                *found = 1;
                break;
            }
        }
        else {
            x = 0;
        }
    }
}

int main(void) {
    // char *name = "Shaunak";
    // int age;
    // printf("Hello %s!\n", name);
    // printf("The value of pi defined in pre processor directive is : %f\n", PI);
    // scanf("%d", &age);
    // printf("So your age is %d\n", age);
    
    int found = 0;
    char word[150]; 
    char parameter[150];
    scanf("%s %s", word, parameter);
    search(word, parameter, &found);
    printf("%d\n", found);
    return 0;
}