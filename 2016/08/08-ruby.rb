#!/opt/ruby3.0/bin/ruby

arr = Array.new(6) { Array.new(50, 0) }

def display(a)
    a.map { |r| puts r.map(&:to_s).join.tr("01", " #") }
    puts "-" * 50
end

File.open("08-input.txt").readlines.map(&:chomp).each do |s|
    if s.start_with? "rect "
        x, y = /rect (\d+)x(\d+)/.match(s).to_a[1..].map(&:to_i)
        0.upto(y-1).each { |y1| 0.upto(x-1).each { |x1| arr[y1][x1] = 1 } }
    elsif s.start_with? "rotate row "
        y, n = /rotate row y=(\d+) by (\d+)/.match(s).to_a[1..].map(&:to_i)
        arr[y] = arr[y].rotate(-n)
    elsif s.start_with? "rotate column "
        x, n = /rotate column x=(\d+) by (\d+)/.match(s).to_a[1..].map(&:to_i)

        column = arr.map { |row| row[x] }.rotate(-n)
        arr.each_with_index { |row,ndx| row[x] = column[ndx] }
    end
end

puts arr.map { |r| r.sum }.sum
display(arr)
