#!/opt/ruby3.0/bin/ruby

shifts = { "v" => 1i, "^" => -1i, ">" => 1, "<" => -1 }
dirs = File.read("03-input.txt").chomp.split("").map { |x| shifts[x] }

part1, pos1 = {}, 0i
part2, pos2a, pos2b = {}, 0i, 0i

dirs.each { |x| part1[pos1 += x] = 1 }
dirs.each_with_index { |x, i| part2[i % 2 == 1 ? pos2b += x : pos2a += x] = 1 }

puts part1.length, part2.length
