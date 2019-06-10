define i32 @func.myfunc(i32* %a.ptr) {
    %a.1.ptr = getelementptr inbounds i32, i32* %a.ptr, i32 1
    store i32 10, i32* %a.1.ptr
    %a.2.ptr = getelementptr inbounds i32, i32* %a.ptr, i32 1
    %a.2.3 = load i32, i32* %a.2.ptr
    %buffer4 = add i32 %a.2.3, 5
    ret i32 %buffer4
}

define i32 @main() {
    %a.ptr = alloca [12 x i32]
    %a.5.ptr = getelementptr inbounds [12 x i32], [12 x i32]* %a.ptr, i32 0, i32 1
    store i32 5, i32* %a.5.ptr

    %a.6.ptr = getelementptr inbounds [12 x i32], [12 x i32]* %a.ptr, i32 0, i32 1
    %a.6.7 = load i32, i32* %a.6.ptr

    %buffer9 = getelementptr inbounds [16 x i8], [16 x i8]* @.str.4, i32 0, i32 0 
    call i32 (i8*, ...) @printf(i8* %buffer9, i32 %a.6.7)
    %result.ptr = alloca i32
    
    %a.10.ptr = getelementptr inbounds [12 x i32], [12 x i32]* %a.ptr, i32 0, i32 0
    %myfunc.11 = call i32 @func.myfunc(i32* %a.10.ptr)
    store i32 %myfunc.11, i32* %result.ptr
    %result.12 = load i32, i32* %result.ptr
    %buffer14 = getelementptr inbounds [14 x i8], [14 x i8]* @.str.5, i32 0, i32 0 
    call i32 (i8*, ...) @printf(i8* %buffer14, i32 %result.12)
    %a.15.ptr = getelementptr inbounds [12 x i32], [12 x i32]* %a.ptr, i32 0, i32 1
    %a.15.16 = load i32, i32* %a.15.ptr
    %buffer18 = getelementptr inbounds [16 x i8], [16 x i8]* @.str.6, i32 0, i32 0 
    call i32 (i8*, ...) @printf(i8* %buffer18, i32 %a.15.16)
    ret i32 0
}

declare i32 @printf(i8*, ...)
@.str.1 = private unnamed_addr constant [13 x i8] c"Old a[1] is \00", align 1
@.str.2 = private unnamed_addr constant [11 x i8] c"Result is \00", align 1
@.str.3 = private unnamed_addr constant [13 x i8] c"New a[1] is \00", align 1
@.str.4 = private unnamed_addr constant [16 x i8] c"Old a[1] is %d\0A\00", align 1
@.str.5 = private unnamed_addr constant [14 x i8] c"Result is %d\0A\00", align 1
@.str.6 = private unnamed_addr constant [16 x i8] c"New a[1] is %d\0A\00", align 1

