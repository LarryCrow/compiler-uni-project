declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
@.2 = constant [6 x i8] c"test\0A\00"
%Person = type { i32, i8* }


define i32 @test() {
  ret i32 1
}

define i32 @main(i32 %argc, i8** nocapture %argv) {
%.1 = alloca i32
store i32 1, i32* %.1
%.2 = alloca i32
store i32 2, i32* %.2
%.3 = alloca i32
store i32 5, i32* %.3
%.4 = alloca i32
%.5 = load i32, i32* %.2
store i32 %.5, i32* %.4
%.6 = alloca i32
%.7 = load i32, i32* %.3
store i32 %.7, i32* %.6
%.8 = load i32, i32* %.4
%.9 = load i32, i32* %.6
%.10 = alloca i32
%.11 = add i32 %.8, %.9
store i32 %.11, i32* %.10
%.13 = alloca i32
%.12 = call i32 @test()
store i32 %.12, i32* %.13
%.14 = alloca i32
%.15 = load i32, i32* %.2
store i32 %.15, i32* %.14
%.17 = alloca i32
%.16 = call i32 @test()
store i32 %.16, i32* %.17
%.18 = load i32, i32* %.14
%.19 = load i32, i32* %.17
%.20 = alloca i32
%.21 = add i32 %.18, %.19
store i32 %.21, i32* %.20


  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
  %str = getelementptr inbounds [6 x i8], [6 x i8]* @.2, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.21)

  ret i32 0
}