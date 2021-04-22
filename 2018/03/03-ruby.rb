#!/opt/ruby3.0/bin/ruby

claims = File.open("03-input.txt").readlines.map { |s| 
    /^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/.match(s).to_a[1..].map(&:to_i)
}

grid = Array.new(1000) { Array.new(1000) { 0 } }
cnt = 0

claims.each do |cl,x1,y1,x2,y2|
    x1.upto(x1 + x2 - 1) do |x|
        y1.upto(y1 + y2 - 1) { |y| grid[y][x] += 1 }
    end
end

p grid.map { |row| row.filter { |n| n > 1 }.length }.sum

p claims.filter { |cl,x1,y1,x2,y2|
    claim = true
    x1.upto(x1 + x2 - 1) do |x|
        y1.upto(y1 + y2 - 1) { |y| claim = false if grid[y][x] > 1 }
    end
    claim
}.map(&:first)[0]


