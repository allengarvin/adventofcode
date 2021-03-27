#!/opt/ruby3.0/bin/ruby

jolts = File.open("10-input.txt").readlines.map(&:to_i).sort
jolts = [0] + jolts + [jolts[-1]+3]
groups = jolts[0..-2].zip(jolts[1..-1]).map { |x| x.inject(&:-).abs }.group_by { |x| x }

part1 = groups[1].length * groups[3].length

contiguous = [[0]]

jolts[1..-1].each_with_index do |j, ndx|
    if j - jolts[ndx] == 1
        contiguous[-1].push(j)
    else
        contiguous.push([j])
    end
end

# Limited solution. A general solution should use a Tribonacci sequence generator
part2 = contiguous.map { |x| [1,1,2,4,7][x.length-1] }.inject(:*)

puts part1, part2

