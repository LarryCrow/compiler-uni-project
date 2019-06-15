
declare i32 @printf(i8*, ...)
@.2 = constant [5 x i8] c"123\0A\00"


define i32 @main() { 
%.1 = alloca i8*
store i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.2, i32 0, i32 0), i8** %.1
%.5 = alloca i8*
%.4 = load i8*, i8** %.1
store i8* %.4, i8** %.5

ret i32 0
}