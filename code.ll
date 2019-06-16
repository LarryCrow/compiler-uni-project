
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@.13 = private constant [4 x i8] c"%d\0A\00" 

@.32 = private constant [4 x i8] c"%d\0A\00" 


define i32 @main() { 
%.1 = alloca [5 x i32]
%.2 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i8 0, i8 0 
store i32 1, i32* %.2 
%.3 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i8 0, i8 1 
store i32 2, i32* %.3 
%.4 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i8 0, i8 2 
store i32 3, i32* %.4 
%.5 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i8 0, i8 3 
store i32 4, i32* %.5 
%.6 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i8 0, i8 4 
store i32 5, i32* %.6 
%.7 = alloca i32
store i32 2, i32* %.7
%.8 = load i32, i32* %.7
%.9 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i32 0, i32 %.8
%.10 = load i32, i32* %.9
%.11 = alloca i32
store i32 %.10, i32* %.11
%.12 = load i32, i32* %.11
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.13, i32 0, i32 0), i32 %.12) 
%.14 = alloca i32
store i32 2, i32* %.14
%.16 = load i32, i32* %.14
%.17 = alloca i32
store i32 2, i32* %.17
%.18 = load i32, i32* %.17
%.19 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i32 0, i32 %.18
%.20 = load i32, i32* %.19
%.21 = alloca i32
store i32 %.20, i32* %.21
%.22 = load i32, i32* %.21
%.23 = sub i32 0, %.22
%.24 = alloca i32
store i32 %.23, i32* %.24
%.25 = load i32, i32* %.24
%.15 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i32 0, i32 %.16
store i32 %.25, i32* %.15
%.26 = alloca i32
store i32 2, i32* %.26
%.27 = load i32, i32* %.26
%.28 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i32 0, i32 %.27
%.29 = load i32, i32* %.28
%.30 = alloca i32
store i32 %.29, i32* %.30
%.31 = load i32, i32* %.30
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.32, i32 0, i32 0), i32 %.31) 

ret i32 0
}