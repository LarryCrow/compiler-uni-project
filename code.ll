
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@.2 = private constant [4 x i8] c"%d\00\0A"
@.5 = private constant [5 x i8] c"%lf\00\0A"
@.11 = private constant [8 x i8] c"a = %d\0A\00" 

@.16 = private constant [9 x i8] c"b = %lf\0A\00" 


define i32 @main() { 
%.1 = alloca i32
store i32 1, i32* %.1
%.3 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.2, i32 0, i32 0), i32* %.1)
%.4 = alloca double
store double 2.0, double* %.4
%.6 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.5, i32 0, i32 0), double* %.4)
%.9 = alloca i32
%.8 = load i32, i32* %.1
store i32 %.8, i32* %.9
%.10 = load i32, i32* %.9
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.11, i32 0, i32 0), i32 %.10) 
%.14 = alloca double
%.13 = load double, double* %.4
store double %.13, double* %.14
%.15 = load double, double* %.14
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.16, i32 0, i32 0), double %.15) 

ret i32 0
}