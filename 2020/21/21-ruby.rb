#!/opt/ruby3.0/bin/ruby

p File.readlines("21-input.txt").map { |x| 
    x.strip.match(/(.*) \(contains (.*)\)/).to_a[1..-1].map { |y| y.index(",") ? y.split(", ") : y.split }
}
    

