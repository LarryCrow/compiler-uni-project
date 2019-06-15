
declare i32 @printf(i8*, ...)
@.7 = private constant [4 x i8] c"%d\0A\00" 


define i32 @main() { 
label2:
%.1 = alloca i32
store i32 5, i32* %.1
br label %label
%.2 = alloca i32
store i32 6, i32* %.2
label:
br label %label2
%.5 = alloca i32
%.4 = load i32, i32* %.1
store i32 %.4, i32* %.5
%.6 = load i32, i32* %.5
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.7, i32 0, i32 0), i32 %.6) 

ret i32 0
}