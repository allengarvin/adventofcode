#!/opt/ruby3.0/bin/ruby
    
require 'set'

answers = File.open("06-input.txt").read.split("\n\n").map { |x| x.split("\n").map { |y| y.split("").to_set }}

part1 = answers.map { |x| x.reduce(:|).length }.sum
part2 = answers.map { |x| x.reduce(:&).length }.sum

puts part1, part2

