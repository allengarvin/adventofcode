#!/opt/ruby3.0/bin/ruby

commands = File.open("06-input.txt").readlines().map { |s| 
    /(.*) (\d+),(\d+) through (\d+),(\d+)/.match(s.chomp).to_a[1..] 
}
    
$grid1 = Array.new(1000) { Array.new(1000, 0) }
$grid2 = Array.new(1000) { Array.new(1000, 0) }

def turn_on(x1, y1, x2, y2, part2)
    (y1..y2).each do |y| 
        (x1..x2).each do |x|
            if part2
               $grid2[y][x] += 1
            else
               $grid1[y][x] = 1
            end
        end
    end
end

def turn_off(x1, y1, x2, y2, part2)
    (y1..y2).each do |y| 
        (x1..x2).each do |x|
            if part2
                $grid2[y][x] -= 1 if $grid2[y][x] > 0
            else
                $grid1[y][x] = 0
            end
        end
    end
end

def toggle(x1, y1, x2, y2, part2)
    (y1..y2).each do |y| 
        (x1..x2).each do |x|
            if part2
                $grid2[y][x] += 2
            else
                $grid1[y][x] = 1 - $grid1[y][x]
            end
        end
    end
end

commands.each do |c|
   eval ("%s(%d,%d,%d,%d,false)" % ([c.first.tr(" ", "_")] + c[1..].map(&:to_i)))
   eval ("%s(%d,%d,%d,%d,true)" % ([c.first.tr(" ", "_")] + c[1..].map(&:to_i)))
end

puts $grid1.map { |r| r.sum }.sum
puts $grid2.map { |r| r.sum }.sum
    
