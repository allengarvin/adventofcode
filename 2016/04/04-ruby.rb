#!/opt/ruby3.0/bin/ruby

rooms = File.open("04-input.txt").readlines.map { |x| 
    a, b, c = /(.*)-(\d+)\[([a-z]+)\]/.match(x).to_a[1..-1] 
    [a, b.to_i, c]
}

valid = rooms.filter do |a,b,c| 
    grp = a.tr('-', '').chars.group_by { |x| x }.sort_by { |k,v| [v.length, 123 - k.ord ] }.map(&:first)[-5..-1].join("").reverse == c
end

puts valid.map { |x| x[1] }.sum

ciphered = valid.map { |a,b,_| 
    [a.chars.map { |c| c == '-' ? ' ' : ((((c.ord - 97) + b) % 26) + 97).chr }.join(), b] }.filter { |x,y| x.include? "northpole" }

puts ciphered[0][1]
