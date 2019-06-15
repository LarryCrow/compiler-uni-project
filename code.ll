
declare i32 @printf(i8*, ...)
@.11 = private constant [4 x i8] c"%d\0A\00" 


define i32 @main() { 
%.1 = alloca i32
store i32 6, i32* %.1
%.2 = alloca i32
store i32 2, i32* %.2
%.3 = load i32, i32* %.1
%.4 = load i32, i32* %.2
%.5 = alloca i32
%.6 = srem i32 %.3, %.4
store i32 %.6, i32* %.5
%.9 = alloca i32
%.8 = load i32, i32* %.5
store i32 %.8, i32* %.9
%.10 = load i32, i32* %.9
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.11, i32 0, i32 0), i32 %.10) 

ret i32 0
}