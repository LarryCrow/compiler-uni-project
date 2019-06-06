declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
%Person = type { i32, i8* }


define i32 @main(i32 %argc, i8** nocapture %argv) {
%.1 = alloca i32
store i32 1, i32* %.1
%.2 = alloca i32
store i32 5, i32* %.2
%.3 = alloca i32
store i32 25, i32* %.3
%.4 = load i32, i32* %.2
%.5 = load i32, i32* %.3
%.6 = alloca i32
%.7 = add i32 %.4, %.5
store i32 %.7, i32* %.6
%.8 = alloca i32
%.9 = load i32, i32* %.1
store i32 %.9, i32* %.8
%.10 = alloca i32
%.11 = load i32, i32* %.6
store i32 %.11, i32* %.10
%.12 = load i32, i32* %.8
%.13 = load i32, i32* %.10
%.14 = alloca i32
%.15 = add i32 %.12, %.13
store i32 %.15, i32* %.14

  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.15)

  ret i32 0
}