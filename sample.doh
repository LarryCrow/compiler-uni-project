// Example 1 (without error)
function void print(int num) {
    // As if this function prints number
    return;
}

int a = 1;
int b = 0;
while (a < 5) {
    b = b + 10;
    a = a + 1;
}
if (b > 40) {
    print(b);
} else {
    print(a);
}

// Example 2 (lex error)
int a = 1;
???
int b = 1;

// Example 3 (syntax error)
function int sum(int a, b c) {
    return a + b;
}


// Example 4 (semantic error)
function int sum(int a, int b) {
    int c = a + b;
    return "some_string";
}
