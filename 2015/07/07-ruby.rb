#!/opt/ruby3.0/bin/ruby

ops = { 'NOT' => '~', 'AND' => '&', 'OR' => '|', 'LSHIFT' => '<<', 'RSHIFT' => '>>' }

# The input is VERY specifically oriented. 
instructions = File.open("07-input.txt").readlines.map { 
    |x| x.strip.gsub(Regexp.union(ops.keys), ops).split(" -> ").reverse
}.sort_by { |a,b| "%2s" % a }.rotate

part1 = {}
part2 = {}

instructions.map { |x|
    eval x.map{ |y| y.gsub(/([a-z]+)/, 'part1["\1"]') }.join(" = ")
}
puts part1["a"]
instructions[0][1] = part1["a"].to_s

instructions.map { |x|
    eval x.map{ |y| y.gsub(/([a-z]+)/, 'part2["\1"]') }.join(" = ")
}
puts part2["a"]

