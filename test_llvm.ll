declare i32 @printf(i8*, ...)
declare double @llvm.powi.f64(double %Val, i32 %power)

@.result = private constant [13 x i8] c"Result = %d\0A\00"
@.2 = constant [6 x i8] c"test\0A\00"

%Person = type {i32}

define %Person @func.a() {
  %.1 = alloca %Person
  %.2 = getelementptr inbounds %Person, %Person* %.1, i32 0, i32 0
  store i32 3, i32* %.2

  %p.1 = load %Person, %Person* %.1
  ret %Person %p.1 
} 

define i32 @main() {
  %.10 = alloca %Person
  %.11 = call %Person @func.a()
  store %Person %.11, %Person* %.10

  %.12 = getelementptr inbounds %Person, %Person* %.10, i32 0, i32 0

%.1000 = load i32, i32* %.12

  %out = getelementptr inbounds [13 x i8], [13 x i8]* @.result, i32 0, i32 0
	call i32 (i8*, ...) @printf(i8* %out, i32 %.1000)

  ret i32 0
}