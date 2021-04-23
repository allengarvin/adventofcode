#!/opt/ruby3.0/bin/ruby

require 'set'

class Memory < Array
    def redistribute
        ndx = self.index(self.max)
        bank = self[ndx]
        self[ndx] = 0
        while bank > 0
            ndx += 1
            self[ndx % self.length] += 1
            bank -= 1
        end
    end
end

mem = Memory.new(File.open("06-input.txt").read().split.map(&:to_i))

states = Set.new([mem.dup])
part2 = 0

(1..Float::INFINITY).each do |n|
    mem.redistribute
    if states.include?(mem)
        if part2 > 0
            puts n - part2
            break
        else
            puts n
            states = Set.new([mem.dup])
            part2 = n
        end
    else
        states.add(mem.dup)
    end
end
