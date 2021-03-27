#!/opt/ruby3.0/bin/ruby

matrix = File.open("02-input.txt").readlines().map { |x| x.split.map(&:to_i).sort }
puts matrix.map { |m| m[-1] - m[0] }.sum
p matrix.map { |m| m.combination(2).filter { |a,b| b % a == 0 }.map { |a,b| b / a } }.flatten.sum
