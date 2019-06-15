
declare i32 @printf(i8*, ...)
@.2 = constant [5 x i8] c"123\0A\00"

@.4 = constant [5 x i8] c"456\0A\00"

@.11 = private constant [4 x i8] c"%s\0A\00" 


define i32 @main() { 
%.1 = alloca i8*
store i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.2, i32 0, i32 0), i8** %.1
%.3 = alloca i8*
store i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.4, i32 0, i32 0), i8** %.3
%.6 = load i8*, i8** %.3
store i8* %.6, i8** %.1
%.9 = alloca i8*
%.8 = load i8*, i8** %.1
store i8* %.8, i8** %.9
%.10 = load i8*, i8** %.9
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.11, i32 0, i32 0), i8* %.10) 

ret i32 0
}