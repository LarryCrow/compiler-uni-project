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
store i32 10, i32* %.1
%.2 = icmp eq i32 10, 100 
br i1 %.2, label %lab1, label %lab2 
lab1: 
%.3 = alloca i32
store i32 0, i32* %.3
br label %lab3
lab2: 
%.4 = alloca i32
store i32 5, i32* %.4
br label %lab3 
lab3:

  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
  %str = getelementptr inbounds [6 x i8], [6 x i8]* @.2, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.11)

  ret i32 0
}