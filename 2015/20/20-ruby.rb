#!/opt/ruby3.0/bin/ruby

bound = File.open("20-input.txt").read.strip.to_i

def run(n, p2)
    limit = n / 20
    gifts = Array.new(limit+1) { 0 } 
    1.upto(limit).each { |i| 
        i.step(p2 ? (i*50 < limit ? i*50 + 1 : limit) : limit, i ).each { |j| gifts[j] += p2 ? i * 11 : i * 10 }
    }
    0.upto(limit).detect { |i| i if gifts[i] > n }
end

puts run(bound, false)
puts run(bound, true)

