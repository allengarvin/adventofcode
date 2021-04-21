#!/opt/ruby3.0/bin/ruby

passphrases = File.open("04-input.txt").readlines().map { |s| s.chomp.split }
puts passphrases.filter { |xs| xs.uniq.length == xs.length }.length
puts passphrases.filter { |xs| xs.map { |wd| wd.chars.sort.join }.uniq.length == xs.length }.length
