#!/opt/ruby3.0/bin/ruby

doubles = Regexp.new (0..9).map { |n| n.to_s + n.to_s }.join("|")
a, b = File.read("04-input.txt").chomp.split("-").map(&:to_i)
numbers = (a..b).map(&:to_s).filter { |n| n.split("").each_cons(2).all? { |x,y| x<=y } } 
p numbers.grep(doubles).length

p numbers.select { |n| n.split('').slice_when { |x,y| x != y }.map(&:length).include?(2) }.length

