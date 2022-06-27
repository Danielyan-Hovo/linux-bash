#tcl gcayin havasarum
puts "grel havasarman a-i gorcakicy: "
gets stdin a
puts "grel havasarman b-i gorcakicy: "
gets stdin b

proc gcayin {a b} {
    set x 0
    puts "trvac havasarumn e $a*X = $b"
    if {$a!=0} {
	set x [expr ($b/$a)]
    	puts "X = $x"
    } elseif { [$a] == 0 && [$b] == 0} {
        puts "antiv qanaki lucumner"
    } else {
    	puts "havasarumy lucum chuni"
    }

}

gcayin ($a $b) 
