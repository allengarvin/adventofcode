#!/opt/ruby3.0/bin/ruby

words = File.open("06-input.txt").readlines.map(&:chomp)

columns = 0.upto(words.first.length-1).map { |i| 
    words.map { |w| w[i] }.group_by { |x| x }.map { |k,v| [v.length, k] }.sort
}

puts columns.map { |a| a.last[1] }.join
puts columns.map { |a| a.first[1] }.join
