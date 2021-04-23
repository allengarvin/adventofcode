#!/opt/ruby3.0/bin/ruby

programs = File.open("07-input.txt").readlines().map do |line|
    if line.include? " -> "
        _, a, b, c = /([a-z]+) \((\d+)\) -> (.*)/.match(line.chomp).to_a
        [a, [b.to_i, 0, c.split(", ")]]
    else
        _, a, b = /([a-z]+) \((\d+)\)/.match(line.chomp).to_a
        [a, [b.to_i, 0, [] ]]
    end
end.to_h

def generate_weights(root, progs, depth)
    wt = progs[root][0]
    my_wt = wt

    progs[root][2].each { |n| wt += generate_weights(n, progs, depth + 1) }
    progs[root][1] = wt
    return wt
end

def drill_down(root, progs, wt)
    groups = progs[root][2].group_by { |i| progs[i][1] }
    if groups.length == 2
        diff = groups.keys.sort { |n| groups[n].length }.reverse.reduce(:-)
        return drill_down(groups.filter { |k,v| v.length == 1 }.to_a[0][1][0], progs, diff)
    else
        return progs[root][0] + wt
    end
end

root = programs.keys.filter { |i| programs.keys.filter { |j| programs[j][2].include?(i) }.length == 0 }[0]

generate_weights(root, programs, -1)
puts root, drill_down(root, programs, 0)


