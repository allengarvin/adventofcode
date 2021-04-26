#!/opt/ruby3.0/bin/ruby

class String
    def abba
        (0..self.length-4).map { |n| self[n..(n+3)] }.filter { |x| x[0] == x[3] && x[1] == x[2] && x[0] != x[1] }.length > 0
    end

    def aba
        (0..self.length-3).map { |n| self[n..(n+2)] }.filter { |x| x[0] == x[2] && x[0] != x[1] }.map { |s| s[1] + s[0] + s[1] }
    end
end

ip_addresses = File.open("07-input.txt").readlines.map(&:chomp).map { |ip| 
    [ip.split(/\[[a-z]+\]/), ip.scan(/\[([a-z]+)\]/).map { |x| x.first }]
}

puts ip_addresses.filter { |a,b| a.filter(&:abba).length > 0 && b.filter(&:abba).length == 0 }.length, 
     ip_addresses.filter { |outs,ins| 
    outs.map { |s| s.aba }.reduce(&:+).filter { |bab| ins.filter { |i| i.include? bab }.length > 0 }.length > 0
}.to_a.length

