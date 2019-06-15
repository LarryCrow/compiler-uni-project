define i32 @func.myfunc(i32* %a.ptr) {
    %a.1.ptr = getelementptr inbounds i32, i32* %a.ptr, i32 1
    store i32 10, i32* %a.1.ptr
    %a.2.ptr = getelementptr inbounds i32, i32* %a.ptr, i32 1
    %a.2.3 = load i32, i32* %a.2.ptr
    %buffer4 = add i32 %a.2.3, 5
    ret i32 %buffer4
}

define i32 @main() {
    ret i32 0
}

declare i32 @printf(i8*, ...)

