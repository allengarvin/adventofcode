#!/opt/ruby3.0/bin/ruby

def fuel(m, r)
  f = m / 3 - 2
  return 0 if f <= 0
  return r ? f + fuel(f, true) : f
end

n = File.open("01-input.txt").map(&:to_i)

puts n.map{ |n| fuel(n, false) }.sum, n.map{ |n| fuel(n, true) }.sum
