#!/opt/ruby3.0/bin/ruby

def parse_pass(s)
    tmp, p = s.chomp.split(": ")
    tmp, let = tmp.split
    l, u = tmp.split("-").map(&:to_i)
    return [l, u, let, p]
end
    
passwords = File.open("02-input.txt").readlines.map { |x| parse_pass(x) }

part1 = passwords.select { |a|
    (a[0]..a[1]).member?(a[3].count(a[2]))
}.length

part2 = passwords.select { |a|
    (a[3][a[0]-1] == a[2]) ^ (a[3][a[1]-1] == a[2])
}.length

puts part1, part2

