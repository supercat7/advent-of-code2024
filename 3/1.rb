text =  File.read(File.join(File.dirname(__FILE__), 'input.txt'))
pattern = /mul\(\d+,\d+\)/
matches = text.scan(pattern)
total = 0

matches.each do |line|
    numbers = line.scan(/\d+/)
    x, y = numbers.map(&:to_i)
    total += x * y
    #puts "x: #{x}, y: #{y}"
end

puts total