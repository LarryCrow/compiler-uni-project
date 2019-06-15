
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@.2 = private constant [3 x i8] c"%d\00"

define i32 @main() { 
%.1 = alloca i32
store i32 10, i32* %.1
%.3 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.2, i32 0, i32 0), i32* %.1)
ret i32 0
}