#!/opt/ruby3.0/bin/ruby

relations = File.open("06-input.txt").readlines().map { |n| n.chomp.split(')') }
obs = relations.map(&:first).uniq
o_map = Hash[obs.zip obs.map { |o| relations.filter { |a,b| a == o }.map(&:last) } ]
parents = Hash[relations.map(&:reverse)]

orbits = {}
parents.each do |k, v|
    orbits[k] = [v]
    p = parents[v]
    while p
        orbits[k].push(p)
        p = parents[p]
    end
end

puts orbits.values.map(&:length).sum

a, b, c = parents['YOU'], parents['SAN'], orbits['YOU'].intersection(orbits['SAN']).first 

puts orbits['YOU'].length + orbits['SAN'].length - 2 * orbits[c].length - 2

