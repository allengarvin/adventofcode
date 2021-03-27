#!/opt/ruby3.0/bin/ruby

strings = File.readlines("05-input.txt")
alphabet = "a".upto("z").to_a

vowels = ['a', 'e', 'i', 'o', 'u']
doubles = alphabet.map { |x| x + x }
bad = ["ab", "cd", "pq", "xy"]

nice1 = strings.select do |x|
    x.split("").select { |v| vowels.member?(v) }.length >= 3 &&
    doubles.select { |dd| x.index(dd) }.length >= 1 && 
    bad.select { |bd| x.index(bd) }.length     == 0
end

alphabet_product = alphabet.product(alphabet)
rule1 = alphabet_product.map(&:join)
rule2 = alphabet_product.map { |x,y| x + y + x}

nice2 = strings.select { |x| rule1.any? { |r1| x.split(r1,-1).length > 2 } && rule2.any? { |r2| x.index(r2) } }

puts nice1.length, nice2.length
    
