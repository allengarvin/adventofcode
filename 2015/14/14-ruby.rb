#!/opt/ruby3.0/bin/ruby

deer = File.readlines("14-input.txt").map { |x| x.chomp.split }.to_h { |x| [x[0], [x[3].to_i] * x[6].to_i + [0] * x[13].to_i] }

puts deer.map { |k,v| (2503 / v.length) * v.sum + v[0..(2503 % v.length)-1].sum }.max

deer_distances = deer.keys.to_h { |x| [x, 0] }
deer_scores = deer.keys.to_h { |x| [x, 0] }

(0..2502).each do |i|
    deer.each { |d, v| deer_distances[d] += v[i % v.length] }
    deer_scores[deer_distances.max_by { |d,v| v }[0]] += 1
end
puts deer_scores.max_by { |d,v| v }[1]
