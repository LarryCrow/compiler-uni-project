declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
%Person = type { i32, i8* }


define i32 @main(i32 %argc, i8** nocapture %argv) {
%.1 = alloca i32
store i32 1, i32* %.1
%.2 = alloca i32
store i32 2, i32* %.2
%.3 = load i32, i32* %.1
%.4 = load i32, i32* %.2
%.5 = alloca i32
%.6 = add i32 %.3, %.4
store i32 %.6, i32* %.5
%.7 = alloca i32
store i32 4, i32* %.7
%.8 = alloca i32
store i32 3, i32* %.8
%.9 = load i32, i32* %.7
%.10 = load i32, i32* %.8
%.11 = alloca i32
%.12 = sub i32 %.9, %.10
store i32 %.12, i32* %.11
%.13 = alloca i32
store i32 4, i32* %.13
%.14 = alloca i32
store i32 2, i32* %.14
%.15 = load i32, i32* %.13
%.16 = load i32, i32* %.14
%.17 = alloca i32
%.18 = sdiv i32 %.15, %.16
store i32 %.18, i32* %.17


  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.18)

  ret i32 0
}