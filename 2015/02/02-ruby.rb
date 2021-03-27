#!/opt/ruby3.0/bin/ruby

presents = File.open("02-input.txt").readlines.map { |x| x.split("x").map(&:to_i).sort }
part1 = presents.map { |x| x.combination(2).map { |y| y.inject(:*) * 2 }.sum + x[0] * x[1] }.sum
part2 = presents.map { |x| (x[0] + x[1]) * 2 + x.inject(:*) }.sum
puts part1, part2
