#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h> // Include this for wait()
int main() {
    int pipe_fd[2]; // File descriptors for the pipe
    pid_t pid;   // stores process ID for fork(),
    char message[] = "Hello"; // Message to be sent through the pipe
    char buffer[100]; // Buffer to store received message
    // Create a pipe
    if (pipe(pipe_fd) == -1) {   // Creates a unidirectional pipe:
// On success, fills pipe_fd[] with file descriptors.
//On failure, returns -1

        perror("pipe");     // Prints an error message if pipe() fails.
        exit(EXIT_FAILURE);
    }
    // Fork a new process
    pid = fork();
    if (pid < 0) { // Error handling
        perror("fork");
        exit(EXIT_FAILURE);
    }
    if (pid == 0) { // Child process (Reader)
        close(pipe_fd[1]); // Close the write end of the pipe
        read(pipe_fd[0], buffer, sizeof(buffer)); // Read from pipe
        close(pipe_fd[0]); // Close the read end
        printf("%s\n", buffer); // Print received message
        exit(0);
    } else { // Parent process (Writer)
        close(pipe_fd[0]); // Close the read end of the pipe
        write(pipe_fd[1], message, strlen(message) + 1); // Write message
        close(pipe_fd[1]); // Close the write end
        wait(NULL); // Wait for child to finish
    }
    return 0;
}
