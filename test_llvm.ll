declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [14 x i8] c"Result = %lf\0A\00"
@.2 = constant [6 x i8] c"test\0A\00"

%Person = type {i32}

define %Person @test(%Person* %.1) {
%.2 = getelementptr inbounds %Person, %Person* %.1, i32 0, i32 0
%.3 = getelementptr inbounds %Person, %Person* %.1, i32 0, i32 0
%.4 = alloca i32
%.5 = load i32, i32* %.3
store i32 %.5, i32* %.4%.6 = alloca i32
store i32 10, i32* %.6
%.7 = load i32, i32* %.4
%.8 = load i32, i32* %.6
%.9 = alloca i32
%.10 = mul i32 %.7, %.8
store i32 %.10, i32* %.9
%.11 = load i32, i32* %.9
store i32 %.11, i32* %.2
%.14 = alloca %Person
%.13 = load %Person, %Person* %.1
store %Person %.13, %Person* %.14

%.15 = load %Person, %Person* %.14
ret %Person %.15
}

define i32 @main() {

%.16 = alloca %Person
%.17 = getelementptr inbounds %Person, %Person* %.16, i32 0, i32 0
store i32 1, i32* %.17
%.18 = alloca %Person
%.19 = getelementptr inbounds %Person, %Person* %.18, i32 0, i32 0
store i32 10, i32* %.19
%.20 = getelementptr inbounds %Person, %Person* %.18, i32 0, i32 0
%.21 = getelementptr inbounds %Person, %Person* %.18, i32 0, i32 0
%.22 = alloca i32
%.23 = load i32, i32* %.21
store i32 %.23, i32* %.22%.24 = getelementptr inbounds %Person, %Person* %.16, i32 0, i32 0
%.25 = alloca i32
%.26 = load i32, i32* %.24
store i32 %.26, i32* %.25%.27 = load i32, i32* %.22
%.28 = load i32, i32* %.25
%.29 = alloca i32
%.30 = sub i32 %.27, %.28
store i32 %.30, i32* %.29
%.31 = load i32, i32* %.29
store i32 %.31, i32* %.20


%.100 = getelementptr inbounds %Person, %Person* %.18, i32 0, i32 0
%.1000 = load i32, i32* %.100

  %out = getelementptr inbounds [14 x i8], [14 x i8]* @.result, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, double 5.0)

  ret i32 0
}