#!/opt/ruby3.0/bin/ruby

class VM
    def initialize(prog)
        @pc, @acc = 0, 0
        @program = prog
        @executed = {}
        @halted = false
        (0..prog.length).each { |i| @executed[i] = false }
    end

    def halted?
        @halted
    end

    def accumulator
        @acc
    end

    def halt
        @halted = true
    end

    def execute
        if @executed[@pc] 
            halt
            return
        else
            @executed[@pc] = true
        end
        
        instr, val = @program[@pc]
        case instr
            when "jmp" 
                @pc += val
            when "nop" 
                @pc += 1
            when "acc" 
                @acc += val; @pc += 1
        end
        if @pc >= @program.length
            puts accumulator
            exit
        end
    end

    def run
        while !halted?
            execute
        end
    end
end

program = File.readlines("input/08-input.txt").map(&:chomp).map(&:split).map { |a,b| [a, b.to_i] }

v = VM.new(program)

v.run
puts v.accumulator

def toggle(x)
    x == "jmp" ? "nop" : "jmp"
end

changes = (0..program.length-1).select { |i| program[i][0] == "nop" or program[i][0] == "jmp" }

changes.each do |c| 
    program[c][0] = toggle(program[c][0])
    v = VM.new(program)
    v.run
    program[c][0] = toggle(program[c][0])
end
