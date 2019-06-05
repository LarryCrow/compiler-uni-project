declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"


define i32 @main(i32 %argc, i8** nocapture %argv) {
%.1 = alloca i32
store i32 4, i32* %.1
%.2 = alloca i32
store i32 2, i32* %.2
%.3 = load i32, i32* %.1
%.4 = load i32, i32* %.2
%.5 = alloca i32
%.6 = call double @llvm.powi.f64(double %.3, i32 %.4)
store i32 %.6, i32* %.5


  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.6)

  ret i32 0
}