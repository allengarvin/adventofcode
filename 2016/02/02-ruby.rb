#!/opt/ruby3.0/bin/ruby

grid1pos, grid1 = 1+1i, [ 0, 1, 2, 1i, 1+1i, 2+1i, 2i, 1+2i, 2+2i ]
grid2pos, grid2 = 2+2i, [ 2+0i, 1+1i, 2+1i, 3+1i, 0+2i, 1+2i, 2+2i, 3+2i, 4+2i, 1+3i, 2+3i, 3+3i, 2+4i ]

instructions = File.open("02-input.txt").readlines().map { |x| x.chomp.split('') }

def solve(i, g, pos)
    moves = { 'U' => -1i, 'D' => 1i, 'L' => -1, 'R' => 1 }
    i.map do |mv|
        mv.each { |m| pos += moves[m] if g.index(pos + moves[m]) }
        (g.index(pos)+1).to_s(g.length+1).upcase
    end.join("")
end

puts solve(instructions, grid1, grid1pos)
puts solve(instructions, grid2, grid2pos)
