require_relative '../helpers.rb'
include Helpers


class Day1
    def self.formatter(input)
        array_left, array_right = Array.new, Array.new
        for each in input
            split_var = each.split(" ")
            array_left.push(Integer(split_var[0]))
            array_right.push(Integer(split_var[1]))
        end
        return array_left, array_right
    end
    def self.run
        left, right = formatter(open_input_file('input.txt'))
        puts "Part 1: #{part1(left, right)}"
        puts "Part 2: #{part2(left, right)}"
    end
    
    def self.part1(left, right)
        sum = 0
        sorted_left = left.sort
        sorted_right = right.sort
        sorted_left.each_with_index {|occurence, index|
            if sorted_left[index] > sorted_right[index] then
                difference = sorted_left[index] - sorted_right[index]
            else
                difference = sorted_right[index] - sorted_left[index]
            end
            sum += difference
        }
        sum
    end

    def self.part2(left, right)
        sum = 0
        left.each {|occurence| sum += occurence * right.count(occurence)}
        sum
    end
end

Day1.run