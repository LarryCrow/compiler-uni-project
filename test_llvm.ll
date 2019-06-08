declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
@.2 = constant [6 x i8] c"test\0A\00"
%Person = type { i32, i1 }


define i32 @test() {
  ret i32 1
}
define i32 @a() {
  ret i32 1
}

define i32 @main(i32 %argc, i8** nocapture %argv) {
%.1 = alloca i32
store i32 0, i32* %.1
%.2 = alloca i32
store i32 1, i32* %.2
br label %lab1 
lab1: 
%.47 = alloca i32
%.46 = load i32, i32* %.1
store i32 %.46, i32* %.47
%.48 = alloca i32
store i32 10, i32* %.48
%.49 = load i32, i32* %.47
%.50 = load i32, i32* %.48
%.51 = alloca i1
%.52 = icmp slt i32 %.49, %.50
store i1 %.52, i1* %.51
 
%.53 = load i1, i1* %.51
br i1 %.53, label %lab2, label %lab3 
lab2: 
%.4 = alloca i32
store i32 0, i32* %.4
br label %lab4 
lab4: 
%.31 = alloca i32
%.30 = load i32, i32* %.4
store i32 %.30, i32* %.31
%.32 = alloca i32
store i32 5, i32* %.32
%.33 = load i32, i32* %.31
%.34 = load i32, i32* %.32
%.35 = alloca i1
%.36 = icmp slt i32 %.33, %.34
store i1 %.36, i1* %.35
 
%.37 = load i1, i1* %.35
br i1 %.37, label %lab5, label %lab6 
lab5: 
%.15 = alloca i32
%.14 = load i32, i32* %.4
store i32 %.14, i32* %.15
%.16 = alloca i32
store i32 3, i32* %.16
%.17 = load i32, i32* %.15
%.18 = load i32, i32* %.16
%.19 = alloca i1
%.20 = icmp slt i32 %.17, %.18
store i1 %.20, i1* %.19
%.21 = load i1, i1* %.19
br i1 %.21, label %lab7, label %lab8 
lab7: 
%.8 = alloca i32
%.7 = load i32, i32* %.2
store i32 %.7, i32* %.8
%.9 = alloca i32
store i32 1, i32* %.9
%.10 = load i32, i32* %.8
%.11 = load i32, i32* %.9
%.12 = add i32 %.10, %.11
store i32 %.12, i32* %.2
br label %lab8 
lab8: 
%.24 = alloca i32
%.23 = load i32, i32* %.4
store i32 %.23, i32* %.24
%.25 = alloca i32
store i32 1, i32* %.25
%.26 = load i32, i32* %.24
%.27 = load i32, i32* %.25
%.28 = add i32 %.26, %.27
store i32 %.28, i32* %.4
br label %lab4 
lab6: 
%.40 = alloca i32
%.39 = load i32, i32* %.1
store i32 %.39, i32* %.40
%.41 = alloca i32
store i32 1, i32* %.41
%.42 = load i32, i32* %.40
%.43 = load i32, i32* %.41
%.44 = add i32 %.42, %.43
store i32 %.44, i32* %.1
br label %lab1 
lab3: 


%.100 = load i32, i32* %.2

  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
  %str = getelementptr inbounds [6 x i8], [6 x i8]* @.2, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.100)

  ret i32 0
}