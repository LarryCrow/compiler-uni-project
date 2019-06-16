
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@.2 = constant [2 x i8] c"\0A\00"


define i32 @main() { 
%.1 = alloca i8*
store i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.2, i32 0, i32 0), i8** %.1

ret i32 0
}