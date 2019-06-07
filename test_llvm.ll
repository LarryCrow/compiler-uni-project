declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
@.2 = constant [6 x i8] c"test\0A\00"
%Person = type { i32, i8* }


define i32 @test() {
  ret i32 1
}

define i32 @main(i32 %argc, i8** nocapture %argv) {
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
%.8 = alloca i32
store i32 20, i32* %.8
%.9 = load i32, i32* %.8
%.7 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i8 0, i8 3
store i32 %.9, i32* %.7
%.10 = getelementptr inbounds [5 x i32], [5 x i32]* %.1, i8 0, i8 3
%.11 = load i32, i32* %.10

  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
  %str = getelementptr inbounds [6 x i8], [6 x i8]* @.2, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.11)

  ret i32 0
}