#!/opt/ruby3.0/bin/ruby

relationships = {}

File.readlines("13-input.txt").map { |x| x.sub("would gain ", "").sub("would lose ", "-").chomp(".\n").split.rotate(-1)[0..2] }.each do
    |p1,p2,r|
        relationships[[p1,p2]] = r.to_i
end

people = relationships.keys.map(&:first).uniq
people.each { |p| relationships[[p, "you"]] = relationships[["you", p]] = 0 }

optimum = ->(x) { x.permutation.map { |p| p.zip(p.rotate(1)).map { |a,b| relationships[[a,b]] + relationships[[b,a]] }.sum }.max }
puts optimum.(people), optimum.(people + ["you"])
