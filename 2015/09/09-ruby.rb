#!/opt/ruby3.0/bin/ruby

dist = {}

File.open("09-input.txt").map(&:split).each do 
    |c1,_,c2,_,dst| 
    dist[[c1,c2]] = dist[[c2,c1]] = dst.to_i 
end

distances = dist.keys.map(&:first).uniq.permutation.map { |x| x.each_cons(2).map { |p| dist[p] }.sum }
p distances.min, distances.max
