#!/opt/ruby3.0/bin/ruby

visited = [0]
dir = 0
moves = [ -1i, 1, 1i, -1 ]
pos = 0

def taxicab(p) 
    return p.real.abs + p.imag.abs
end

File.open("01-input.txt").read().strip.split(", ").each do |move|
    turn, steps = move[0], move[1..-1].to_i
    dir = (dir + (turn == "R" ? 1 : -1)) % 4
    (1..steps).each { |x| pos += moves[dir]; visited.push(pos) }
end

puts taxicab(pos)
puts taxicab(visited.select { |n| visited.count(n) > 1 }.uniq[0])
