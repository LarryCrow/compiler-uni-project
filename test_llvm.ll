declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
@.2 = constant [6 x i8] c"test\0A\00"
%Person = type { i32, i1 }


define i32 @test() {
  ret i32 1
}

define i32 @main(i32 %argc, i8** nocapture %argv) {
%.1 = alloca %Person
%.2 = getelementptr inbounds %Person, %Person* %.1, i32 0, i32 0
%.3 = alloca i32
store i32 15, i32* %.3
%.4 = load i32, i32* %.3
store i32 %.4, i32* %.2
%.5 = load i32, i32* %.2



  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
  %str = getelementptr inbounds [6 x i8], [6 x i8]* @.2, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.5)

  ret i32 0
}