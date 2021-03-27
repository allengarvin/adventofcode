#!/opt/ruby3.0/bin/ruby
    
seats = File.open("05-input.txt").readlines.map { |x| x.chomp.tr("BR", "1").tr("FL", "0").to_i(2) }.sort

part1 = seats[-1]
part2 = (seats[0]..seats[-1]).select { |x| !seats.member?(x) }

puts part1, part2

