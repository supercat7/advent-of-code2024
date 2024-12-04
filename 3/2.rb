text =  File.read(File.join(File.dirname(__FILE__), 'input.txt'))
mul_pattern = /mul\((\d+),(\d+)\)/
do_pattern = /do\(\)/
dont_pattern = /don't\(\)/

total = 0
enabled = true

full_pattern = /do\(\)|don't\(\)|mul\(\d+,\d+\)/

text.scan(full_pattern).each do |instruction|
    case instruction
    when do_pattern
        enabled = true
    when dont_pattern
        enabled = false
    when mul_pattern
        if enabled == true
            x, y = instruction.match(mul_pattern).captures.map(&:to_i)
            total += x * y
        end
    end
end
puts total