struct Title {
    int a;
    string b;
    boolean c;
}

function int test(){
    Title d = {
        a = 1;
        b = 'string';
        c = true;
    }
    if (true) {
        return d;
    } else {
        return null;
    }
}