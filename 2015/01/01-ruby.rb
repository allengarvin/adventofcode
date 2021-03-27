#!/opt/ruby3.0/bin/ruby

floors = [0]
parens = File.read("01-input.txt").chomp.split("").each { |x| floors << floors[-1] + (x == "(" ? 1 : -1) }

puts floors[-1], floors.index(-1)
