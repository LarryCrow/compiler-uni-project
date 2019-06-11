%Person = type { i32, i1 }

declare i32 @printf(i8*, ...)
define double @arrSum(double* %.1) {
%.2 = alloca double
store double 0.0, double* %.2
%.3 = alloca i32
store i32 0, i32* %.3
br label %lab1 
lab1: 
%.29 = alloca i32
%.28 = load i32, i32* %.3
store i32 %.28, i32* %.29
%.30 = alloca i32
store i32 5, i32* %.30
%.31 = load i32, i32* %.29
%.32 = load i32, i32* %.30
%.33 = alloca i1
%.34 = icmp slt i32 %.31, %.32
store i1 %.34, i1* %.33
 
%.35 = load i1, i1* %.33
br i1 %.35, label %lab2, label %lab3 
lab2: 
%.7 = alloca double
%.6 = load double, double* %.2
store double %.6, double* %.7
%.8 = alloca i32
%.11 = alloca i32
%.10 = load i32, i32* %.3
store i32 %.10, i32* %.11
%.12 = load i32, i32* %.11
store i32 %.12, i32* %.8
%.13 = load i32, i32* %.8
%.14 = getelementptr inbounds double, double* %.1, i32 %.13
%.15 = load double, double* %.14
%.16 = alloca double
store double %.15, double* %.16
%.17 = load double, double* %.7
%.18 = load double, double* %.16
%.19 = fadd double %.17, %.18
store double %.19, double* %.2
%.22 = alloca i32
%.21 = load i32, i32* %.3
store i32 %.21, i32* %.22
%.23 = alloca i32
store i32 1, i32* %.23
%.24 = load i32, i32* %.22
%.25 = load i32, i32* %.23
%.26 = add i32 %.24, %.25
store i32 %.26, i32* %.3
br label %lab1 
lab3: 
%.38 = alloca double
%.37 = load double, double* %.2
store double %.37, double* %.38

%.39 = load double, double* %.38
ret double %.39
}

@.49 = private constant [19 x i8] c"Person is married\0A\00" 

@.59 = private constant [23 x i8] c"Person is not married\0A\00" 

@.69 = private constant [20 x i8] c"Sum of array = %lf\0A\00" 


define i32 @main() { 
%.40 = alloca [5 x double]
%.41 = getelementptr inbounds [5 x double], [5 x double]* %.40, i8 0, i8 0 
store double 1.0, double* %.41 
%.42 = getelementptr inbounds [5 x double], [5 x double]* %.40, i8 0, i8 1 
store double 4.5, double* %.42 
%.43 = getelementptr inbounds [5 x double], [5 x double]* %.40, i8 0, i8 2 
store double 2.333, double* %.43 
%.44 = getelementptr inbounds [5 x double], [5 x double]* %.40, i8 0, i8 3 
store double 3.12, double* %.44 
%.45 = getelementptr inbounds [5 x double], [5 x double]* %.40, i8 0, i8 4 
store double 0.0, double* %.45 
%.46 = alloca %Person
%.47 = getelementptr inbounds %Person, %Person* %.46, i32 0, i32 0
store i32 28, i32* %.47
%.48 = getelementptr inbounds %Person, %Person* %.46, i32 0, i32 1
store i1 1, i1* %.48
%.50 = getelementptr inbounds %Person, %Person* %.46, i32 0, i32 1
%.51 = alloca i1
%.52 = load i1, i1* %.50
store i1 %.52, i1* %.51%.53 = alloca i1
store i1 1, i1* %.53
%.54 = load i1, i1* %.51
%.55 = load i1, i1* %.53
%.56 = alloca i1
%.57 = icmp eq i1 %.54, %.55
store i1 %.57, i1* %.56
%.58 = load i1, i1* %.56
br i1 %.58, label %lab4, label %lab5 
lab4: 
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([19 x i8], [19 x i8]* @.49, i32 0, i32 0)) 
br label %lab6 
lab5: 
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([23 x i8], [23 x i8]* @.59, i32 0, i32 0)) 
br label %lab6 
lab6: 
%.62 = getelementptr inbounds [5 x double],[5 x double]* %.40, i32 0, i32 0
%.63 = alloca double
%.64 = call double @arrSum(double* %.62)
store double %.64, double* %.63
%.67 = alloca double
%.66 = load double, double* %.63
store double %.66, double* %.67
%.68 = load double, double* %.67
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.69, i32 0, i32 0), double %.68) 

ret i32 0
}