#!/opt/ruby3.0/bin/ruby

numbers = File.open("01-input.txt").readlines.map(&:to_i)
puts [2,3].map { |n| numbers.combination(n).to_a.select {|x| 2020 == x.sum}[0].inject(:*) }
