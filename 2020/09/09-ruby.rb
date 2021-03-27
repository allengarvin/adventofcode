#!/opt/ruby3.0/bin/ruby

xmas = File.readlines("09-input.txt").map(&:to_i)

(25..xmas.length-1).each do |i|
    if !xmas[i-25..i-1].combination(2).map(&:sum).member?(xmas[i])
        part1 = xmas[i]
        part2 = (0..i-1).to_a.combination(2).select { |a,b| xmas[a..b].sum == part1 }.map { |a,b| xmas[a..b].sort.rotate(-1)[0..1].sum }[0]
        puts part1, part2
    end
end

