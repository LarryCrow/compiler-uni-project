define i32 @main() { 
%a.ptr = alloca i8* 
store i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.1, i32 0, i32 0), i8** %a.ptr 
%b.ptr = alloca i8* 
store i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str.2, i32 0, i32 0), i8** %b.ptr 
%b.1 = load i8*, i8** %b.ptr 
store i8* %b.1, i8** %a.ptr 
%a.2 = load i8*, i8** %a.ptr
%buffer4 = getelementptr inbounds [4 x i8], [4 x i8]* @.str.3, i32 0, i32 0 
call i32 (i8*, ...) @printf(i8* %buffer4, i8* %a.2)
ret i32 0 
} 

declare i32 @printf(i8*, ...) 
@.str.1 = private unnamed_addr constant [4 x i8] c"123\00", align 1 
@.str.2 = private unnamed_addr constant [13 x i8] c"123123123123\00", align 1 
@.str.3 = private unnamed_addr constant [4 x i8] c"%s\0A\00", align 1 