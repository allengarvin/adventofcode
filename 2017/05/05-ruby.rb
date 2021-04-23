#!/opt/ruby3.0/bin/ruby

program = File.open("05-input.txt").readlines().map(&:to_i)

def run_machine(prog, part2)
    pc = 0

    (0..Float::INFINITY).each do |n|
        return n if pc < 0 || pc >= prog.length
        prev = pc
        pc += prog[pc]
        prog[prev] += (prog[prev] >= 3 && part2) ? -1 : 1
    end
end

puts run_machine(program.dup, false)
puts run_machine(program.dup, true)
    

