
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@.2 = constant [2 x i8] c"\0A\00"

@.3 = private constant [20 x i8] c"What is your name?\0A\00" 

@.4 = private constant [4 x i8] c"%s\00\0A"
@.10 = private constant [12 x i8] c"Hello, %s!\0A\00" 


define i32 @main() { 
%.1 = alloca i8*
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.2, i32 0, i32 0), i8** %.1
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.3, i32 0, i32 0)) 
%.5 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.4, i32 0, i32 0), i8** %.1)
%.8 = alloca i8*
%.7 = load i8*, i8** %.1
store i8* %.7, i8** %.8
%.9 = load i8*, i8** %.8
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.10, i32 0, i32 0), i8* %.9) 

ret i32 0
}