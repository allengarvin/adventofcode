#!/opt/ruby3.0/bin/ruby
    
class Forest
    def initialize(a)
        @my_map = a.map { |x|
            x.chomp.split("").map { |c| c == "#" ? true : false }
        }
    end

    def length
        return @my_map.length
    end

    def tree? (x,y)
        return @my_map[y][x % @my_map[0].length]
    end

    def traverse (slope)
        return (0..self.length-1).step(slope[1]).select { |y| tree?( slope[0] * y / slope[1], y) }.length
    end
end

f = Forest.new(File.open("03-input.txt").readlines)

part1 = f.traverse([3,1])
part2 = [[1,1], [3,1], [5,1], [7,1], [1,2]].map { |x| f.traverse(x) }.inject(:*)

puts part1, part2

