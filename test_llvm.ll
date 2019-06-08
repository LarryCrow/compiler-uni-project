declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
@.2 = constant [6 x i8] c"test\0A\00"
%Person = type { i32, i1 }

define i32 @main(i32 %argc, i8** nocapture %argv) {
%.1 = alloca i32
store i32 10, i32* %.1
br label %lab1 
lab1: 
%.21 = alloca i32
%.20 = load i32, i32* %.1
store i32 %.20, i32* %.21
%.22 = alloca i32
store i32 20, i32* %.22
%.23 = load i32, i32* %.21
%.24 = load i32, i32* %.22
%.25 = alloca i1
%.26 = icmp slt i32 %.23, %.24
store i1 %.26, i1* %.25
 
%.27 = load i1, i1* %.25
br i1 %.27, label %lab2, label %lab3 
lab2: 
%.5 = alloca i32
%.4 = load i32, i32* %.1
store i32 %.4, i32* %.5
%.6 = alloca i32
store i32 1, i32* %.6
%.7 = load i32, i32* %.5
%.8 = load i32, i32* %.6
%.9 = add i32 %.7, %.8
store i32 %.9, i32* %.1
%.12 = alloca i32
%.11 = load i32, i32* %.1
store i32 %.11, i32* %.12
%.13 = alloca i32
store i32 12, i32* %.13
%.14 = load i32, i32* %.12
%.15 = load i32, i32* %.13
%.16 = alloca i1
%.17 = icmp eq i32 %.14, %.15
store i1 %.17, i1* %.16
%.18 = load i1, i1* %.16
br i1 %.18, label %lab4, label %lab5 
lab4: 
br label %lab3 
br label %lab5 
lab5: 
br label %lab1 
lab3: 



; %.1001 = getelementptr inbounds [4 x i32], [4 x i32]* %.1, i32 0, i32 0
; %.1002 = load i32, i32* %.1001

; %.1003 = getelementptr inbounds [4 x i32], [4 x i32]* %.1, i32 0, i32 1
; %.1004 = load i32, i32* %.1003

; %.1005 = getelementptr inbounds [4 x i32], [4 x i32]* %.1, i32 0, i32 2
; %.1006 = load i32, i32* %.1005

; %.1007 = getelementptr inbounds [4 x i32], [4 x i32]* %.1, i32 0, i32 3
; %.1008 = load i32, i32* %.1007

  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
  %str = getelementptr inbounds [6 x i8], [6 x i8]* @.2, i32 0, i32 0
	; call i32 (i8*, ...) @printf(i8* %out, i32 %.1002)
	; call i32 (i8*, ...) @printf(i8* %out, i32 %.1004)
	; call i32 (i8*, ...) @printf(i8* %out, i32 %.1006)
	; call i32 (i8*, ...) @printf(i8* %out, i32 %.1008)

  ret i32 0
}