#!/opt/ruby3.0/bin/ruby

require 'set'

numbers = File.open("01-input.txt").readlines().map(&:to_i)
puts numbers.sum

freq = 0
seen = Set.new

(0..Float::INFINITY).each do |i|
    freq += numbers[i % numbers.length]
    if seen.member?(freq)
        puts freq
        exit
    else
        seen.add(freq)
    end
end
