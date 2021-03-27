#!/opt/ruby3.0/bin/ruby

strings = File.readlines("08-input.txt").map(&:chomp)

tr = { "\\" => "\\\\", '"' => '\\"' }

puts strings.map { |x| x.length - eval(x).length }.sum
puts strings.map { |x| ('"' + x.split("").map { |c| tr.member?(c) ? tr[c] : c }.join("") + '"').length  - x.length}.sum


