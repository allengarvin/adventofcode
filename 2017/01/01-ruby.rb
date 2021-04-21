#!/opt/ruby3.0/bin/ruby

p1, p2 = 0, 0
num = File.read("01-input.txt").chomp.split("")
num.each_with_index { |c,i| p1 += c.to_i if c == num[(i+1) % num.length] }
num.each_with_index { |c,i| p2 += c.to_i if c == num[(i+num.length/2) % num.length] }
puts p1, p2
