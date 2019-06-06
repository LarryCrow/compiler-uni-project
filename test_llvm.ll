declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
%Person = type { i32, i8* }


define i32 @main(i32 %argc, i8** nocapture %argv) {


  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.6)

  ret i32 0
}