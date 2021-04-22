#!/opt/ruby3.0/bin/ruby

class String
    def counting(n)
        self.chars.tally.values.member?(n)
    end
end

ids = File.open("02-input.txt").readlines.map(&:chomp)

puts ids.count { |x| x.counting(2) } * ids.count { |x| x.counting(3) }

puts ids.combination(2).map { |a,b| 
    c = a.chars.each_with_index.map { |c,i| c == b[i] ? c : "" }.join
    c.length == a.length - 1 ? c : false
}.filter { |x| x }[0]


