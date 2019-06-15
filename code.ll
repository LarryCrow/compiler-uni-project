%Person = type { i32, i8* }

declare i32 @printf(i8*, ...)


define i32 @main() { 
%.1 = alloca %Person
%.2 = getelementptr inbounds %Person, %Person* %.1, i32 0, i32 0
store i32 25, i32* %.2
%.3 = getelementptr inbounds %Person, %Person* %.1, i32 0, i32 1
store i8* John, i8** %.3

ret i32 0
}