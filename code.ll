
declare i32 @printf(i8*, ...)
@.17 = private constant [4 x i8] c"%d\0A\00" 


define i32 @main() { 
%.1 = alloca i32
store i32 5, i32* %.1
%.2 = alloca i32
store i32 2, i32* %.2
%.5 = alloca i32
%.4 = load i32, i32* %.1
store i32 %.4, i32* %.5
%.8 = alloca i32
%.7 = load i32, i32* %.2
store i32 %.7, i32* %.8
%.9 = load i32, i32* %.5
%.10 = load i32, i32* %.8
%.11 = alloca i32
%.12 = srem i32 %.9, %.10
store i32 %.12, i32* %.11
%.15 = alloca i32
%.14 = load i32, i32* %.11
store i32 %.14, i32* %.15
%.16 = load i32, i32* %.15
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.17, i32 0, i32 0), i32 %.16) 

ret i32 0
}